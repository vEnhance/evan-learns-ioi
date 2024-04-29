/* {{{ https://gist.github.com/kodekracker/e09f9d23573f117a5db0
 * vim:fdm=marker
 *
 * Note: This template uses some c++11 functions , so you have to compile it with c++11 flag.
 *       Example:-   $ g++ -std=c++11 c++Template.cpp
 *
 * Author : Akshay Pratap Singh
 * Handle: code_crack_01
 *
 */
#pragma GCC optimize ("O3")

/********   All Required Header Files ********/
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>
#include <queue>
#include <deque>
#include <bitset>
#include <iterator>
#include <list>
#include <stack>
#include <map>
#include <set>
#include <functional>
#include <numeric>
#include <utility>
#include <limits>
#include <time.h>
#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>

using namespace std;

/*******  All Required define Pre-Processors and typedef Constants *******/
#define SCD(t) scanf("%d",&t)
#define SCLD(t) scanf("%ld",&t)
#define SCLLD(t) scanf("%lld",&t)
#define SCC(t) scanf("%c",&t)
#define SCS(t) scanf("%s",t)
#define SCF(t) scanf("%f",&t)
#define SCLF(t) scanf("%lf",&t)
#define MEM(a, b) memset(a, (b), sizeof(a))
#define FOR(i, j, k, in) for (int i=j ; i<k ; i+=in)
#define RFOR(i, j, k, in) for (int i=j ; i>=k ; i-=in)
#define REP(i, j) FOR(i, 0, j, 1)
#define RREP(i, j) RFOR(i, j, 0, 1)
#define all(cont) cont.begin(), cont.end()
#define rall(cont) cont.end(), cont.begin()
#define FOREACH(it, l) for (auto it = l.begin(); it != l.end(); it++)
#define IN(A, B, C) assert( B <= A && A <= C)
#define MP make_pair
#define PB push_back
#define INF (int)1e9
#define EPS 1e-9
#define PI 3.1415926535897932384626433832795
#define MOD 1000000007
#define read(type) readInt<type>()
const double pi=acos(-1.0);
typedef pair<int, int> PII;
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<PII> VII;
typedef vector<VI> VVI;
typedef map<int,int> MPII;
typedef set<int> SETI;
typedef multiset<int> MSETI;
typedef long long int int64;
typedef unsigned long long int  uint64;
typedef vector<int64> VI64;
typedef vector<uint64> VUI64;
template<typename T, typename U> inline void amin(T &x, U y) { if(y < x) x = y; }
template<typename T, typename U> inline void amax(T &x, U y) { if(x < y) x = y; }
#ifdef DEBUG
    #define debug(args...)     (Debugger()) , args
    class Debugger
    {
        public:
        Debugger(const string& _separator = " ") :
        first(true), separator(_separator){}
        template<typename ObjectType> Debugger& operator , (const ObjectType& v)
        {
            if(!first)
                cerr << separator;
            cerr << v;
            first = false;
            return *this;
        }
        ~Debugger() {  cerr << endl;}
        private:
        bool first;
        string separator;
    };
#else
    #define debug(args...) // Just strip off all debug tokens
#endif
// }}}

/********** Main()  function **********/
int64 grid[512][512];
int Fx[100];
int Fy[100];
int64 next_grid[512][512];

int main()
{
  int k;
  cin >> k;
  int n = 1 << k; // = 2^k
  for (int i=0; i<n; ++i) {
    for (int j=0; j<n; ++j) {
      grid[i][j] = 0;
      next_grid[i][j] = 0;
    }
  }

  for (int i=0; i<n; ++i) {
    for (int j=0; j<n; ++j) {
      cin >> grid[i][j];
    }
  }
  int t;
  cin >> t;

  for (int i=0; i<t; ++i) {
    cin >> Fx[i];
    cin >> Fy[i];
  }
  for (int e=0; e<k; ++e) {
    int c = (1<<e); // = 2^e
    for (int m=0; m<t; ++m) {
      // Multiply by F(X,Y) genfunc
      for (int i=0; i<n; ++i) {
        for (int j=0; j<n; ++j) {
          next_grid[(n*n+i+c*Fx[m])%n][(n*n+j+c*Fy[m])%n] ^= grid[i][j];
        }
      }
    }
    // Copy the result back into the main grid and reset
    for (int i=0; i<n; ++i) {
      for (int j=0; j<n; ++j) {
        grid[i][j] = next_grid[i][j];
        next_grid[i][j] = 0;
      }
    }
  }

  int count = 0;
  for (int i=0; i<n; ++i) {
    for (int j=0; j<n; ++j) {
      debug(i, j, grid[i][j]);
      if (grid[i][j] != 0) {
        count++;
      }
    }
  }

  cout << count << endl;
  return 0;
}
