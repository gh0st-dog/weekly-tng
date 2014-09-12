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

    $scope.gridOptions = {
        data: 'trainings',
        columnDefs: [
            {field:'name', displayName:'Название'},
            {field:'goal', displayName:'Цель'},
            {field: 'tng_type', displayName: 'Тип'}
        ],
        showFooter: true,
        resizable: true,
        enablePinning: true
    };



    $scope.loadTrainings = function(){
        $http.jsonp('http://localhost:8080/training/?callback=JSON_CALLBACK').
            success(function(data){
                $scope.trainings = data;
            })
            .error(function(){
                console.error('got error');
            });
    };

    $scope.loadTrainings();


}]);
