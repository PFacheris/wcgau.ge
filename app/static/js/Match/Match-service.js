'use strict';

angular.module('WCGUA.GE')
  .factory('Match', ['$resource', function ($resource) {
    return $resource('WCGUA.GE/Matches/:id', {}, {
      'query': { method: 'GET', isArray: true},
      'get': { method: 'GET'},
      'update': { method: 'PUT'}
    });
  }]);
