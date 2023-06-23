/** @odoo-module **/

import options from 'web_editor.snippets.options';

options.registry.OdometerOptions = options.Class.extend({
    start() {
        let odometerRow = this.$target.find('#odometer-row-dis')

        if (odometerRow){

        }
    },
})

export default {
    OdometerOptions: options.registry.OdometerOptions,
};