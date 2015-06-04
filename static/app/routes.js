"use strict";
angular.module("baseballApp").config(function ($routeProvider) {
  $routeProvider
    .when("/", {
      templateUrl: "app/views/home.html",
      controller: "HomeController"
    })
    .when("/player", {
      templateUrl: "app/views/player.html",
      controller: "PlayerController"
    })
    .when("/player/:pk", {
      templateUrl: "app/views/ind-player.html",
      controller: "IndPlayerController"
    })
    .when("/game", {
      templateUrl: "app/views/game.html",
      controller: "GameController"
    })
    .when("/game/:pk", {
      templateUrl:"app/views/ind-game.html",
      controller: "IndGameController"
    })
    .when("/team", {
      templateUrl: "app/views/team.html",
      controller: "TeamController"
    })
    .when("/team/:pk", {
      templateUrl: "app/views/ind-team.html",
      controller: "IndTeamController"
    })
    .when("/inning/:pk", {
      templateUrl: "app/views/inning.html",
      controller: "InningController"
    })
    .when("/404", {
      templateUrl: "app/views/404.html",
      controller: "404Controller"
    })
    .otherwise({redirectTo: "/404"});
})