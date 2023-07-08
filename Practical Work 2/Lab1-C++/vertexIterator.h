#pragma once
#include <vector>
#include "graph.h"

class VertexIterator {
    int currentPos;
public:
    VertexIterator(Graph* currentGraph);
    bool isValid();
    VertexIterator operator++(int);
    int operator *();
};