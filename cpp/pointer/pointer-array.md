- 前置：[[pointer]], [[array]]
- 堆区指针数组示例
  ```cpp
  int main() {
    int **p = new int*[3];
    for (int **q = p; q-p<3; q++){
    *q = new int[4];
    for (int *r = *q; r-*q<4; r++) *r = (r-*q) * 10 + q-p; 
    }

    for (int **q = p; q-p<3; q++){
      for (int *r = *q; r-*q<4; r++) cout<<*r<<endl;
    }
    return 0;
  }
  ```

- [[2-4-cpp]]中问了这题