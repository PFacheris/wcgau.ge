'use strict';

angular.module('WCGUA.GE')
  .config(['$routeProvider', function ($routeProvider) {
    $routeProvider
      .when('/Matches', {
        templateUrl: 'views/Match/Matches.html',
        controller: 'MatchController',
        resolve:{
          resolvedMatch: ['Match', function (Match) {
            return Match.query();
          }]
        }
      })
    }]);
