var express = require('express');
var app = express();
require('./db');

var UserController = require('./user/UserController');
app.use('/users', UserController);

// Test Hello world
app.get("/", function (req, res) {
    res.send("The API is working fine");
})

module.exports = app;
