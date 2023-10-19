#include <iostream>
#include <vector>
#include <pybind11/pybind11.h>

class MySum {
public:
    MySum(float initial_value) {
        this->sum = initial_value;
    }

    float Get() {
        return sum;
    }

    void Update(float value) {
        sum += value;
    }

private:
    float sum;
};

namespace py = pybind11;

PYBIND11_MODULE(my_sum, m) {
    py::class_<MySum>(m, "MySum")
        .def(py::init<float>())
        .def("Get", &MySum::Get)
        .def("Update", &MySum::Update);
}