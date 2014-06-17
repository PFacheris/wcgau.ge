'use strict';

angular.module('WCGUA.GE')
  .controller('MatchController', ['$scope', '$modal', 'resolvedMatch', 'Match',
    function ($scope, $modal, resolvedMatch, Match) {

      $scope.Matches = resolvedMatch;

      $scope.create = function () {
        $scope.clear();
        $scope.open();
      };

      $scope.update = function (id) {
        $scope.Match = Match.get({id: id});
        $scope.open(id);
      };

      $scope.delete = function (id) {
        Match.delete({id: id},
          function () {
            $scope.Matches = Match.query();
          });
      };

      $scope.save = function (id) {
        if (id) {
          Match.update({id: id}, $scope.Match,
            function () {
              $scope.Matches = Match.query();
              $scope.clear();
            });
        } else {
          Match.save($scope.Match,
            function () {
              $scope.Matches = Match.query();
              $scope.clear();
            });
        }
      };

      $scope.clear = function () {
        $scope.Match = {
          
          "HomeName": "",
          
          "AwayName": "",
          
          "Percentage": "",
          
          "TSAdded": "",
          
          "HomeScore": "",
          
          "AwayScore": "",
          
          "CurrentGameMinute": "",
          
          "StartTime": "",
          
          "AwayTeamID": "",
          
          "HomeTeamID": "",
          
          "MatchID": "",
          
          "id": ""
        };
      };

      $scope.open = function (id) {
        var MatchSave = $modal.open({
          templateUrl: 'Match-save.html',
          controller: MatchSaveController,
          resolve: {
            Match: function () {
              return $scope.Match;
            }
          }
        });

        MatchSave.result.then(function (entity) {
          $scope.Match = entity;
          $scope.save(id);
        });
      };
    }]);

var MatchSaveController =
  function ($scope, $modalInstance, Match) {
    $scope.Match = Match;

    
    $scope.TSAddedDateOptions = {
      dateFormat: 'yy-mm-dd',
      maxDate: -1
      
    };
    $scope.StartTimeDateOptions = {
      dateFormat: 'yy-mm-dd',
      maxDate: -1
      
    };

    $scope.ok = function () {
      $modalInstance.close($scope.Match);
    };

    $scope.cancel = function () {
      $modalInstance.dismiss('cancel');
    };
  };
