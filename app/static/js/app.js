// Declare app level module which depends on filters, and services
var app = angular.module('WCGUA.GE', ['ngResource', 'ngRoute', 'ui.bootstrap', 'ui.date']);

app.config(['$routeProvider', function ($routeProvider) {
    $routeProvider
      .when('/', {
        templateUrl: 'views/home/home.html',
        controller: 'HomeController'})
      .otherwise({redirectTo: '/'});
}]);

app.directive('gaugeCircle', function() {
    return {
        link: function(scope, elem, attrs) {
            var resizeElem;
            (resizeElem = function () {
                elem.css('height', (elem.width() / 2) + parseInt(elem.css('border-top-width')));
                var width = elem.width();
                elem.css('border-radius', width + 'px ' + width + 'px 0 0');
            })();

            angular.element(window).bind('resize', resizeElem);
        }
    };
});

app.directive('body', function() {
    return {
        restrict: 'E',
        link: function(scope, elem, attrs) {
            var resizeElem;
            (resizeElem = function () {
                elem.css('height', angular.element(window).height());
            })();

            angular.element(window).bind('resize', resizeElem);
        }
    };
})