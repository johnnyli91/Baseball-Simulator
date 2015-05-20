"use strict";
angular.module("baseballApp")
  .controller("GameController", function ($scope) {
    $http.get("http://localhost:8000/api/games").
      success(function (data, status, headers, config) {
        $scope.players = data;
      }).
      error(function (data, status, headers, config) {
        console.log(data);
      })
  })