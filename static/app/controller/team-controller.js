"use strict";
angular.module("baseballApp")
  .controller("TeamController", function ($scope, $http, $location) {
      $http.get($location.host() + "/api/teams").
      success(function (data, status, headers, config) {
        $scope.teams = data;
      }).
      error(function (data, status, headers, config) {
        console.log(data);
      })
  });
