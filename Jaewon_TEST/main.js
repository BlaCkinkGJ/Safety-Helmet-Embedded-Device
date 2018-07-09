var http = require('http');
var fs = require('fs');
var url = require('url');
 
var app = http.createServer(function(request,response){
    var _url = request.url;
    var queryData = url.parse(_url, true).query;
    var title = queryData.id;
    if(_url == '/'){
      title = 'Nations of NE Asia';
    }
    if(_url == '/favicon.ico'){
      return response.writeHead(404);
    }
    response.writeHead(200);
    fs.readFile(`data/${queryData.id}`, 'utf8', function (err, description){
        console.log(err);
      var template = `
      <!doctype html>
      <html>
      <head>
        <title>Nations - ${title}</title>
        <meta charset="utf-8">
      </head>
      <body>
        <h1><a href="/">Nations</a></h1>
        <ul>
          <li><a href="/?id=Korea">Korea</a></li>
          <li><a href="/?id=Japan">Japan</a></li>
          <li><a href="/?id=China">China</a></li>
        </ul>
        <h2>${title}</h2>
        <p>${description}</p>
      </body>
      </html>
      `;
      response.end(template);
    })
 
 
});
app.listen(3000);