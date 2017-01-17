"use strict";
angular.module("baseballApp").config(function ($routeProvider) {
  $routeProvider
    .when("/", {
      templateUrl: "static/app/views/home.html",
      controller: "HomeController"
    })
    .when("/player", {
      templateUrl: "static/app/views/player.html",
      controller: "PlayerController"
    })
    .when("/player/:pk", {
      templateUrl: "static/app/views/ind-player.html",
      controller: "IndPlayerController"
    })
    .when("/game", {
      templateUrl: "static/app/views/game.html",
      controller: "GameController"
    })
    .when("/game/:pk", {
      templateUrl:"static/app/views/ind-game.html",
      controller: "IndGameController"
    })
    .when("/team", {
      templateUrl: "static/app/views/team.html",
      controller: "TeamController"
    })
    .when("/team/:pk", {
      templateUrl: "static/app/views/ind-team.html",
      controller: "IndTeamController"
    })
    .when("/inning/:pk", {
      templateUrl: "static/app/views/inning.html",
      controller: "InningController"
    })
    .when("/404", {
      templateUrl: "static/app/views/404.html",
      controller: "404Controller"
    })
    .otherwise({redirectTo: "/404"});
});
