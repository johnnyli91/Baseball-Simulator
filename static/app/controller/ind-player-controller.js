"use strict";
angular.module("baseballApp")
  .controller("IndPlayerController", function ($scope, $routeParams, $http) {
    $scope.pk = $routeParams["pk"];
    $http.get("http://localhost:8000/api/players/" + $scope.pk + "/").
      success(function (data, status, headers, config) {
        $scope.playerName = data.name;
        $scope.power = data.power;
        $scope.contact = data.contact;
        $scope.speed = data.speed;
        $scope.pitch = data.pitch
      }).error(function (data, status, headers, config) {
        console.log(data);
      })
  })