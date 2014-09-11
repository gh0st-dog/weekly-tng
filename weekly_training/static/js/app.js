/**
 * Created by buyvich on 01.09.14.
 */

app = angular.module("MainApp", ["ngGrid", "ngRoute"]);

app.config(function($interpolateProvider, $httpProvider) {
    $httpProvider.defaults.useXDomain = true;
    $httpProvider.defaults.xsrfHeaderName = 'X-XSRFToken';
    $httpProvider.defaults.xsrfCookieName = '_xsrf';
});


app.controller("TngGreed", ["$scope", "$http", "$route", function($scope, $http){

    $scope.trainings = [];
    $scope.myData = [{name: "Moroni", age: 50},
                 {name: "Tiancum", age: 43},
                 {name: "Jacob", age: 27},
                 {name: "Nephi", age: 29},
                 {name: "Enos", age: 34}];

    $scope.gridOptions = { data: 'myData' };



    $scope.loadTrainings = function(){
        $http.get('http://localhost:8000/training').
            success(function(data){
                $scope.trainings = angular.fromJson(data);
                //$scope.gridOptions = { data: $scope.trainings};
            });
    };

    //$scope.loadTrainings();


}]);
