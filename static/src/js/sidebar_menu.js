/** @odoo-module **/

import { patch } from "@web/core/utils/patch";
import { WebClient } from "@web/webclient/webclient";
import { rpc } from "@web/core/network/rpc";
import { user } from "@web/core/user";
import { useState } from "@odoo/owl";

import { router, routerBus } from "@web/core/browser/router";

patch(WebClient.prototype, {
    async setup() {
        super.setup();

        this.menuService = this.env.services.menu;

        this.userId = user.userId;
        this.isAdmin = user.isAdmin;
        this.user = user;
        this.allowedMenus = [];
        this.allowedMenus = useState([]);

        this.state.currentAppId = this.menuService.getCurrentApp()?.id;
        this.env.bus.addEventListener(
            "MENU:CHANGED",
            this._onMenuChanged.bind(this)
        );


    },
    _onMenuChanged() {
        const currentApp = this.menuService.getCurrentApp();
        this.state.currentAppId = currentApp?.id || null;
    },

    onSidebarMenuSelection(menu) {
        if (!menu) return;

        const actionableMenu = this._findFirstActionMenu(menu);
        if (actionableMenu) {
            this.menuService.selectMenu(actionableMenu);

            if (actionableMenu.appID) {
                this.menuService.setCurrentMenu(actionableMenu.appID);
            }
            this.env.bus.trigger("MENU:CHANGED");
        }
    },

    _findFirstActionMenu(menu) {
        if (menu.actionID) {
            return menu;
        }
        if (!menu.childrenTree) {
            return null;
        }
        for (const child of menu.childrenTree) {
            const found = this._findFirstActionMenu(child);
            if (found) return found;
        }
        return null;
    },

    _getMenuIcon(menu) {
        if (menu.webIconData) {
            return menu.webIconData;
        }
        if (menu.webIcon) {
            return `/web/image/${menu.webIcon}`;
        }
        // fallback icon
        return "/web/static/img/menu_icon.svg";
    },


});
