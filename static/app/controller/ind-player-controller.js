"use strict";
angular.module("baseballApp")
  .controller("IndPlayerController", function ($scope, $routeParams, $http) {
    $scope.pk = $routeParams["pk"];
    $http.get("http://localhost:8000/api/players/" + $scope.pk + "/").
      success(function (data, status, headers, config) {
        $scope.playerName = data.name;
        $scope.role = data.role;
        $scope.power = data.power;
        $scope.contact = data.eye;
        $scope.speed = data.speed;
        $scope.pitchControl = data.pitcher_control;
        $scope.pitchPower = data.pitcher_power;
        $scope.pitchMovement = data.pitcher_movement;
      }).error(function (data, status, headers, config) {
        console.log(data);
      })
  })