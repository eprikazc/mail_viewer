(function () {
  "use strict";

  var gmailViewerModule = angular.module('GmailViewer', ['ngRoute']);
  gmailViewerModule.controller('MainController', function($scope, $http) {
    $scope.messages = [];
    $http.get("/email/")
    .then(function(response) {
      $scope.messages = response.data.messages;
    });
  });

  gmailViewerModule.config(function($routeProvider) {
    $routeProvider
     .when('/', {
      templateUrl: '/static/core/templates/messages.html',
      controller: 'MainController',
    });
  });
} ());
