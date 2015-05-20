"use strict";
angular.module("baseballApp")
  .controller("HomeController", function ($scope, $http, $location) {
    $scope.playBall = function () {
      $http.post("http://localhost:8000/api/games/", {"name": $scope.gameName, "team": [2,3]}).
        success(function (data, status, headers, config) {
          var result_pk = data.pk;
          $location.path("/game/" + result_pk);
        }).
        error(function (data, status, headers, config) {
          console.log(data);
        });
    }
  })