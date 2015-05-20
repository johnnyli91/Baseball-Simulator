"use strict";
angular.module("baseballApp")
  .controller("TeamController", function ($scope, $http) {
      $http.get("http://localhost:8000/api/teams").
      success(function (data, status, headers, config) {
        $scope.teams = data;
      }).
      error(function (data, status, headers, config) {
        console.log(data);
      })
  })