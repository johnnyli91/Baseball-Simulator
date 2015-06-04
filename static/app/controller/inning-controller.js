"use strict";
angular.module("baseballApp")
  .controller("InningController", function ($scope, $routeParams, $http) {
    $scope.pk = $routeParams["pk"];
    $http.get("http://localhost:8000/api/innings/" + $scope.pk + "/").
      success(function (data, status, headers, config) {
        console.log(data);
      }).error(function (data, status, headers, config) {
        console.log(data);
      })
  })