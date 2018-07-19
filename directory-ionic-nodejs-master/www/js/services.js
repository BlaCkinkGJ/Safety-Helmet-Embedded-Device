angular.module('directory.services', ['ngResource'])
    .factory('Employees', function ($resource) {
        return $resource('http://ionic-directory.herokuapp.com/employees/:employeeId/:data');
    });
