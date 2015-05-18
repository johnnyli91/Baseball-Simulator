"use strict";
angular.module("baseballApp")
  .controller("HomeController", function ($scope, $http) {
    $scope.playBall = function () {
      $http.post("http://localhost:8000/api/games/", {"name": $scope.gameName, "team": [2,3]}).
        success(function (data, status, headers, config) {
          var result_name = data.name;
          var score = data.game_score;
          var score_arr = [];
          for (var i = 0; i < score.length; i++) {
            score_arr.push(score[i]["team"]["name"] + ": " + score[i]["score"].toString() + "\n");
          }
          $scope.results = result_name + "\n" + score_arr[0] + score_arr[1];
          console.log(data);
        }).
        error(function (data, status, headers, config) {
          console.log(data);
        });
    }
  })