"use strict";

var gmailViewerModule = angular.module('GmailViewer', ['ngRoute']);

gmailViewerModule.config(function($routeProvider) {
  $routeProvider
   .when('/', {
     templateUrl: '/static/app/partials/messages.html',
    controller: 'MainController',
  });
});
