// Laura Lundell
// Created 2019-10-09
// Modified 2019-10-15
// CS411 Analysis of Algorithms
// Assignment 3-A: Greatest Contiguous Sum

#ifndef contigsum_h
#define contigsum_h

#include <iterator>
using std::distance; //compute size

struct GCSValues
{
  int A_seqGCS;
  int B_firstValGCS;
  int C_lastValGCS;
  int D_entireSeqSum;
};

// template<typename RAIter>
// GCSValues divideConquer(RAIter first, RAIter last)
// {
//
//
//
// }

template<typename RAIter>
int contigSum(RAIter first, RAIter last)
{
  int seqSize = distance(first, last);
  return 0;
}

#endif /* contigsum_h */
