"use strict";
angular.module("baseballApp")
  .controller("IndPlayerController", function ($scope, $routeParams, $http, $location) {
    $scope.pk = $routeParams["pk"];
    $http.get("/api/players/" + $scope.pk + "/").
      success(function (data, status, headers, config) {
        $scope.playerName = data.name;
        $scope.role = data.role === 0 ? 'Batter' : 'Pitcher';
        $scope.power = data.power;
        $scope.speed = data.speed;
      })
  });
