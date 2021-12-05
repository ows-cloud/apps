odoo.define('custom.field_utils', function (require) {
    "use strict";

    var field_utils = require('web.field_utils');
    var fieldRegistry = require('web.field_registry');
    var basic_fields = require('web.basic_fields');
    var core = require('web.core');
    var _lt = core._lt;
    var dom = require('web.dom');

    // Extend the field_utils with json formatting and parsing,
    // otherwise views will fail when trying to display the json fields
    field_utils.format.json = function(value) { return JSON.stringify(value); };
    field_utils.parse.json = function(value) { return JSON.parse(value); };

    // Use a Textarea widget to edit json fields in the form view
    var JsonTextField = basic_fields.InputField.extend({
        description: _lt("Json"),
        className: 'o_field_json',
        supportedFieldTypes: ['json'],
        tagName: 'span',

        init: function () {
            this._super.apply(this, arguments);

            if (this.mode === 'edit') {
                this.tagName = 'textarea';
            }
            this.autoResizeOptions = {parent: this};
        },
        /**
         * As it it done in the start function, the autoresize is done only once.
         *
         * @override
         */
        start: function () {
            if (this.mode === 'edit') {
                dom.autoresize(this.$el, this.autoResizeOptions);
            }
            return this._super();
        },
        /**
         * Override to force a resize of the textarea when its value has changed
         *
         * @override
         */
        reset: function () {
            var self = this;
            return Promise.resolve(this._super.apply(this, arguments)).then(function () {
                if (self.mode === 'edit') {
                    self.$input.trigger('change');
                }
            });
        },
        /**
         * @override
         * @private
         * @param {object} value
         * @returns {boolean}
         */
        _isSameValue: function (value) {
            // Use deep equals (from underscore.js) for json objects to avoid infinite loops
            // Because we `JSON.parse and JSON.strigify` the value in `field_utils` it will be a different instance on every check,
            // so the default check with triple equals will report changes ad infinitum => infinite loop on change
            return _.isEqual(value, this.value);
        },
        //--------------------------------------------------------------------------
        // Handlers
        //--------------------------------------------------------------------------

        /**
         * Stops the enter navigation in a text area.
         *
         * @private
         * @param {OdooEvent} ev
         */
        _onKeydown: function (ev) {
            if (ev.which === $.ui.keyCode.ENTER) {
                ev.stopPropagation();
                return;
            }
            this._super.apply(this, arguments);
        },
    });
    fieldRegistry.add('json', JsonTextField);

});
