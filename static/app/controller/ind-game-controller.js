"use strict";
angular.module("baseballApp")
  .controller("IndGameController", function ($scope, $routeParams, $http) {
    $scope.pk = $routeParams["pk"];
    $http.get("http://localhost:8000/api/games/" + $scope.pk + "/").
      success(function (data, status, headers, config) {
        console.log(data);
      }).error(function (data, status, headers, config) {
        console.log(data);
      })
  })