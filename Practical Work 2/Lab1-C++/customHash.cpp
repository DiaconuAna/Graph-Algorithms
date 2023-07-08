#include "customHash.h"

size_t CustomHashFunction::operator()(const Edge& edge) const {
    return (edge.svf * 7 + edge.evf * 11) % modulo;
}