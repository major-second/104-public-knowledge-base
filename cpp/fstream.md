- [参考](https://www.runoob.com/cplusplus/cpp-files-streams.html)
- 注意在什么地方启动的程序，使用相对路径时小心
- ```cpp
  #include <fstream>
  #include <iostream>
  using namespace std;
  
  int main ()
  {
      
  char data[100]; // 如果读入数等等，可能需要 double data; 等
  
  ofstream outfile;
  outfile.open("afile.dat"); 
  cout << "Writing to the file" << endl;
  cout << "Enter your name: "; 
  cin.getline(data, 100);
  outfile << data << endl;
  cout << "Enter your age: "; 
  cin >> data;
  cin.ignore();
  outfile << data << endl;
  outfile.close();
  ifstream infile; // 也可以 ifstream file("name");
  infile.open("afile.dat"); 
  cout << "Reading from the file" << endl; 
  infile >> data; 
  cout << data << endl;
  infile >> data; 
  cout << data << endl; 
  infile.close();
  return 0;
  }
  ```
# csv-input
- 前置
  - [[csv]]
  - [[cpp-io]]
```cpp
#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <filesystem>


int main(int argc, char *argv[]) {
    if (argc != 2) {
        std::cerr << "Usage: " << argv[0] << " <inputfile>\n";
        return 1;
    }
    std::filesystem::path inputPath(argv[1]);
    std::ifstream inputFile(inputPath);
    std::string line;

    while (std::getline(inputFile, line)) {
        std::istringstream ss(line);
        std::string token;
        std::vector<std::string> tokens;

        while (std::getline(ss, token, ',')) {
            tokens.push_back(token);
        }

        long timeStamp = std::stol(tokens[0]);
        std::string symbol = tokens[1];
        std::cout << timeStamp << ' ' << symbol << std::endl;
    }
    return 0;
}
```