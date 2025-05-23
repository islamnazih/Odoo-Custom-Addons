/** @odoo-module **/
import {Component} from "@odoo/owl"

export class ActiveCallsTray extends Component {
    static template = 'asterisk_plus.active_calls_tray'
    static props = {
        bus: Object,
    }

    _onClick() {
        this.props.bus.trigger('active_calls_toggle_display')
    }
}

