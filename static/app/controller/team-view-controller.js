"use strict";
angular.module("baseballApp")
  .controller("TeamViewController", function ($scope, $http, $location) {
      $http.get("/api/teamview").
      success(function (data, status, headers, config) {
        $scope.teams = data;
      }).
      error(function (data, status, headers, config) {
        console.log(data);
      })
  });
