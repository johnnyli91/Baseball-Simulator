"use strict";
var app = angular.module("baseballApp", ["ngRoute", "mgcrea.ngStrap"]);
app.config(['$httpProvider', function($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
}]);
