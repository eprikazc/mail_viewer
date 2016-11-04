var gmailViewerModule = angular.module('GmailViewer', []);
gmailViewerModule.controller('MainController', function($scope, $http) {
  $scope.messages = [];
  $http.get("/email/")
  .then(function(response) {
    $scope.messages = response.data.messages;
    console.log($scope.messages);
  });
});
