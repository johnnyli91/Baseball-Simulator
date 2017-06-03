"use strict";
angular.module("baseballApp")
  .controller("IndGameController", function ($scope, $routeParams, $http, $location) {
    $scope.pk = $routeParams["pk"];
    $scope.inningNumber = [1, 2, 3, 4, 5, 6, 7, 8, 9];
    $http.get($location.host() + "/api/games/" + $scope.pk + "/").
      success(function (data, status, headers, config) {
        $scope.gameName = data.game_name;
        $scope.gameData = data.game_data;
      })
  });
