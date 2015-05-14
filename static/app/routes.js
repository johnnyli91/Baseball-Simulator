'use strict';
angular.module('baseballApp').config(function ($routeProvider) {
    $routeProvider
        .when('/home', {
            templateUrl: 'app/views/home.html',
            controller: 'HomeController'
        })
        .otherwise({redirectTo: 'home'});
})