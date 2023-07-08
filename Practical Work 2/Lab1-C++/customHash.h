#pragma once
#include "edge.h"
#include <iostream>

class CustomHashFunction {
    int modulo = 666013; // it is a prime
public:
    size_t operator()(const Edge& edge) const;
};