var connect = require('connect');
var serveStatic = require('serve-static');
connect().use(serveStatic(__dirname)).listen(8545, function(){
    console.log('Web server running on 8545...');
});
