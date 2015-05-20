"use strict";
angular.module("baseballApp")
  .controller("GameController", function ($scope, $http) {
    $http.get("http://localhost:8000/api/games").
      success(function (data, status, headers, config) {
        $scope.games = data;
      }).
      error(function (data, status, headers, config) {
        console.log(data);
      })
  })