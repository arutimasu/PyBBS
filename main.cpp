#include <iostream>
#include "httplib.h"
#include <string.h> 
#include <vector>
using namespace httplib;

int main(void) {
    std::string line;
    std::string lines;
    std::string name;
    std::string username;
    std::ifstream in("bulletins"); // окрываем файл для чтения
    std::vector<std::string> usernames; 
    std::vector<std::string> names; 
    if (in.is_open())
    {
        while (std::getline(in, line))
        {
            std::cout << line << std::endl;
            lines+=line+"\n";
            username = std::string(strtok(&line[0], "\t"))[0];
            usernames.push_back(username);
            name = std::string(strtok(&line[0], "\t"))[1]; 
            names.push_back(name);
        }
    }
    in.close();     // закрываем файл
  Server svr;
  
  svr.Get("/hi", [](const Request & /*req*/, Response &res) {
    res.set_content("Hello World!", "text/plain");
  });

  svr.listen("0.0.0.0", 8080);
}
