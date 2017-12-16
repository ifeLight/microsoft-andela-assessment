var exec = require("child_process").exec;

exec("docker-compose up", function (err, stdout, stderr) {
    if (!err) {
        console.log(stdout);
    }
})

