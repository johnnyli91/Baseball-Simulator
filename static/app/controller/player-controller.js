"use strict";
angular.module("baseballApp")
  .controller("PlayerController", function ($scope, $http) {
    $http.get("http://localhost:8000/api/players").
      success(function (data, status, headers, config) {
        $scope.players = data;
      }).
      error(function (data, status, headers, config) {
        console.log(data);
      })
  })