"use strict";
angular.module("baseballApp")
  .controller("InningController", function ($scope, $routeParams, $http) {
    $scope.pk = $routeParams["pk"];
    $http.get("http://localhost:8000/api/innings/" + $scope.pk + "/").
      success(function (data, status, headers, config) {
        $scope.team = data.team
        $scope.game = data.game
        $scope.number = data.number
        $scope.score = data.score
      }).error(function (data, status, headers, config) {
        console.log(data);
      })
  })