"use strict";
angular.module("baseballApp")
  .controller("HomeController", function ($scope, $http, $location) {
    $http.get($location.host() + "/api/teams").
      success(function (data, status, headers, config) {
        $scope.teams = data;
      }).
      error(function (data, status, headers, config) {
        console.log(data);
      });
    $scope.playBall = function () {
      $http.post($location.host() + "/api/games/", {"name": $scope.gameName, "team": [$scope.awayTeam.pk, $scope.homeTeam.pk]}).
        success(function (data, status, headers, config) {
          var result_pk = data.pk;
          $location.path("/game/" + result_pk);
        }).
        error(function (data, status, headers, config) {
          console.log(data);
        });
    };
    $scope.makeTeam = function() {
      $http.post($location.host() + "/api/teams/", {"name":$scope.teamName, "team_player": []}).
        success(function (data, status, headers, config) {
          var result_pk = data.pk;
          $location.path("/team/" + result_pk);
        }).
        error(function (data, status, headers, config) {
          console.log(data);
        });
    }
  });
