// Laura Lundell
// CS411 Analysis of Algorithms
// A2 Exhaustive Search - Bridge Optimization
// September 25, 2019

#ifndef build_h
#define build_h

#include "build.cpp"
#include <vector>
using std::vector;

using Bridge = vector<int>;

int build(int w, int e, const vector<Bridge> & bridges);

#endif /* build_h */
