"use strict";
angular.module("baseballApp")
  .controller("RosterController", function ($scope, $routeParams, $http, $location) {
    $scope.pk = $routeParams["pk"];
    $http.get("/api/teamview/" + $scope.pk + "/").
      success(function (data, status, headers, config) {
        $scope.data = data;
      }).
      error(function (data, status, headers, config) {
        console.log(data);
      })
  });
