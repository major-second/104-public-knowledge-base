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