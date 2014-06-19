angular.module('WCGUA.GE')
  .controller('HomeController', ['$scope', function ($scope) {
    $scope.getAngleStyle = function() {
        return {
            '-webkit-transform': 'rotate(' + ($scope.match.percentage / 100) * 180 + 'deg)'
        };
    };

    $scope.match = {
        percentage: 50
    };

    $scope.set = function(input) {
        $scope.match.percentage = input;
    };
  }]);
