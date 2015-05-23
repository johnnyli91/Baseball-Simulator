"use strict";
angular.module("baseballApp")
  .controller("IndTeamController", function ($scope, $routeParams, $http) {
    $scope.pk = $routeParams["pk"];
    $http.get("http://localhost:8000/api/teams/" + $scope.pk + "/").
      success(function (data, status, headers, config) {
        $scope.teamName = data.name;
        $scope.players = data.team_player;
      }).error(function (data, status, headers, config) {
        console.log(data);
      })
  })