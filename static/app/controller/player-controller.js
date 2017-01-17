"use strict";
angular.module("baseballApp")
  .controller("PlayerController", function ($scope, $http, $location) {
    $http.get($location.host() + "/api/players").
      success(function (data, status, headers, config) {
        $scope.players = data;
      }).
      error(function (data, status, headers, config) {
        console.log(data);
      })
  });
