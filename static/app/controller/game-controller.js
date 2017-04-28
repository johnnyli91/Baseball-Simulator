"use strict";
angular.module("baseballApp")
  .controller("GameController", function ($scope, $http, $location) {
    $http.get($location.host() + "/api/games").
      success(function (data, status, headers, config) {
        $scope.games = data;
      }).
      error(function (data, status, headers, config) {
        console.log(data);
      })
  });
