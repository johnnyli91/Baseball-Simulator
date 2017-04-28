"use strict";
angular.module("baseballApp")
  .controller("IndTeamController", function ($scope, $routeParams, $http, $location) {
    $scope.pk = $routeParams["pk"];
    $http.get($location.host() + "/api/teams/" + $scope.pk + "/").
      success(function (data, status, headers, config) {
        $scope.teamName = data.name;
        $scope.players = data.team_player;
      }).error(function (data, status, headers, config) {
        console.log(data);
      })
  });
