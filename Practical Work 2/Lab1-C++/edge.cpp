#include "edge.h"
using namespace std;

Edge::Edge(int svf, int evf) {
    this->svf = svf;
    this->evf = evf;
}

bool Edge::operator == (const Edge& newEdge) const{
    return (this->svf == newEdge.svf && this->evf == newEdge.evf);
}