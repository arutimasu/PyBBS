const http = require("http");
var prompt = require("prompt");
const fs = require('fs');
const EOL = require('os').EOL;
var bulletins = fs.readFileSync('bulletins', 'utf8').split(EOL);
var contacts = fs.readFileSync('contacts', 'utf8').split(EOL);
str=""
for(let i=0;i < bulletins.length;i++){
       
        str+="<p>From: "+bulletins[i].split('\t')[1]+"<br>"+bulletins[i].split('\t')[0]+"<hr>";
         
       
} 
const server =  http.createServer(function(request, response){
    const ps = require("prompt-sync");

    const prompt = ps();
    const name = prompt("Введите свое имя:");
    console.log("Ваше имя: ", contacts[contacts.indexOf(name)].split('\t')[1])
    alert("Ваше имя: ", contacts[contacts.indexOf(name)].split('\t')[1])
    response.end(str.toString());
});
server.listen(3000, function(){ console.log("Сервер запущен по адресу http://localhost:3000")});
