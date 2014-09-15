/**
 * Created by buyvich on 01.09.14.
 */

angular
    .module("MainApp", ["ngGrid", "ngRoute"])
    .config(function($interpolateProvider, $httpProvider) {
        $httpProvider.defaults.useXDomain = true;
        $httpProvider.defaults.xsrfHeaderName = 'X-XSRFToken';
        $httpProvider.defaults.xsrfCookieName = '_xsrf';
    })
    .controller("TngGreed", ["$scope", "$http", "$route", TngGreed])
    .controller("TngGreed", ["$scope", "$http", "$route", CurrentWeek]);

function TngGreed($scope, $http){

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
}

function CurrentWeek($scope, $http){

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
}
