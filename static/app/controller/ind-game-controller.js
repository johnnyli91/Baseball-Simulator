"use strict";
angular.module("baseballApp")
  .controller("IndGameController", function ($scope, $routeParams, $http) {
    $scope.pk = $routeParams["pk"];
    $scope.inningNumber = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    $http.get("http://localhost:8000/api/games/" + $scope.pk + "/").
      success(function (data, status, headers, config) {
        $scope.gameName = data.name;
        $scope.scores = data.game_score;
        $scope.innings = data.inning;
      }).error(function (data, status, headers, config) {
        console.log(data);
      })
  })