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
typedef long int int32;
typedef unsigned long int uint32;
typedef long long int int64;
typedef unsigned long long int  uint64;
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

const int64 MODULUS = 1338557220;

int main()
{
  cout << 108 << endl;
  VI v{4, 5, 7, 9, 11, 13, 17, 19, 23};
  vector<uint64> lagrange{
    334639305,
    1070845776,
    764889840,
    594914320,
    365061060,
    1235591280,
    629909280,
    1056755700,
    640179540,
  };

  int s = 0;
  for (int i=0; i<v.size(); i++) {
    for (int j=0; j<v.at(i) - 1; j++) {
      s++;
      cout << s+1 << " ";
    }
    s++;
    cout << s-v.at(i)+1 << " ";
  }
  cout << endl;

  vector<uint64> residues;

  int k;
  s = 0;
  for (int i=0; i<v.size(); i++) {
    for (int j=0; j<v.at(i) - 1; j++) {
      s++;
      cin >> k; // discard this value
    }
    s++;
    cin >> k;
    int start_value = s-v.at(i)+1;
    int residue = (k-start_value+1) % v.at(i);
    debug(residue);
    residues.push_back(residue);
  }

  uint64 answer = 0;
  for (int i=0; i<v.size(); i++) {
    answer += residues.at(i) * lagrange.at(i);
  }
  debug(answer);
  answer %= MODULUS;
  cout << answer % MODULUS << endl;

  return 0;
}
