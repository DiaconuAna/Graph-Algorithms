#pragma once
using namespace std;

class Edge {

public:
    int svf;
    int evf;

    //constructor
    Edge(int svf, int evf);

    //operator overloading to check if 2 edges are equal
    bool operator == (const Edge& newEdge) const;

};
