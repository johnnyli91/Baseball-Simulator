"use strict";
angular.module("baseballApp")
  .controller("InningController", function ($scope, $routeParams, $http, $location) {
    $scope.pk = $routeParams["pk"];
    $http.get($location.host() + "/api/innings/" + $scope.pk + "/").
      success(function (data, status, headers, config) {
        $scope.team = data.team;
        $scope.game = data.game;
        $scope.number = data.number;
        $scope.score = data.score;
        $scope.bat_inning = data.bat_inning;
      }).error(function (data, status, headers, config) {
        console.log(data);
      })
  });
