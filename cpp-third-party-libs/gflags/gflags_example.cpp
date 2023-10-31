#include<iostream>
#include<stdio.h>
#include <gflags/gflags.h>
DEFINE_bool(test_b, true, "test_b_help");
DEFINE_string(test_s, "default", "test_s_help");
using namespace std;
int main(){
    cout << FLAGS_test_b;
    cout << FLAGS_test_s;
    return 0;
}