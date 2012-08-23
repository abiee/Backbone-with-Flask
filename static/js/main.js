(function() {
    "use strict";

    require.config({
        shim: {
            'underscore': {
                exports: "_"
            },

            'backbone': {
                deps: ['jquery', 'underscore'],
                exports: 'Backbone'
            },

            'marionette': {
                deps: ['backbone'],
                exports: 'Backbone.Marionette'
            },

            'mustache': {
                exports: 'Mustache'
            }
        },

        paths: {
            backbone: "libs/Backbone/backbone-min",
            marionette: "libs/Backbone/backbone.marionette.min",
            underscore: "libs/Underscore/underscore-min",
            mustache: "libs/Mustache/mustache",
            jquery: 'libs/jQuery/jquery-1.7.2.min',
            text: "libs/require/text",
            templates: "../templates"
        }

    });

    require(["backbone"], function() {
        if(typeof Backbone === "object")
            alert("Backbone loaded");
    });

})();
