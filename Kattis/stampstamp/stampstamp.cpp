// https://open.kattis.com/problems/stampstamp
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
        Debugger(const std::string& _separator = " ") :
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
        std::string separator;
    };
#else
    #define debug(args...) // Just strip off all debug tokens
#endif
// }}}
struct pt {
    int x, y;
};

int orientation(pt a, pt b, pt c) {
    int v = a.x*(b.y-c.y)+b.x*(c.y-a.y)+c.x*(a.y-b.y);
    if (v < 0) return -1; // clockwise
    if (v > 0) return +1; // counter-clockwise
    return 0;
}

bool cw(pt a, pt b, pt c, bool include_collinear) {
    int o = orientation(a, b, c);
    return o < 0 || (include_collinear && o == 0);
}
bool collinear(pt a, pt b, pt c) { return orientation(a, b, c) == 0; }

void convex_hull(vector<pt>& a, bool include_collinear = false) {
    pt p0 = *min_element(a.begin(), a.end(), [](pt a, pt b) {
        return make_pair(a.y, a.x) < make_pair(b.y, b.x);
    });
    sort(a.begin(), a.end(), [&p0](const pt& a, const pt& b) {
        int o = orientation(p0, a, b);
        if (o == 0)
            return (p0.x-a.x)*(p0.x-a.x) + (p0.y-a.y)*(p0.y-a.y)
                < (p0.x-b.x)*(p0.x-b.x) + (p0.y-b.y)*(p0.y-b.y);
        return o < 0;
    });
    if (include_collinear) {
        int i = (int)a.size()-1;
        while (i >= 0 && collinear(p0, a[i], a.back())) i--;
        reverse(a.begin()+i+1, a.end());
    }

    vector<pt> st;
    for (int i = 0; i < (int)a.size(); i++) {
        while (st.size() > 1 && !cw(st[st.size()-2], st.back(), a[i], include_collinear))
            st.pop_back();
        st.push_back(a[i]);
    }

    a = st;
}


int main() {
  int n; // rows
  int m; // columns

  bool grid[505][505];
  vector<pt> points;
  cin >> n >> m;

  char s;
  for (int j=0; j<n; ++j) {
    for (int i=0; i<m; i++) {
      cin >> s;
      grid[i][n-1-j] = (s == '#');
      if (grid[i][n-1-j]) {
        pt p;
        p.x = i;
        p.y = n-1-j;
        points.push_back( p );
      }
    }
  }
  int number_of_points_total = points.size();
  debug(number_of_points_total, "points read");
  if (points.size() == 0) {
    cout << 0 << endl;
    return 0;
  }
  if (points.size() <= 2) {
    cout << 1 << endl;
    return 0;
  }

  // replace points with just the convex hull
  convex_hull(points, false);
  // cerr << points.size() << " points in the convex hull" << endl;

  points.push_back(points.at(0)); // cyclic
  int ax, ay;
  int cx, cy; // coprime ones
  int dx, dy;
  int score;
  int best_score = 999999;
  int y_lower_bound, y_upper_bound;
  int g;

  vector<pair<int, int>> seen_once;
  vector<pair<int, int>> seen_twice;
  map<pair<int,int>,int> gcd_of_dirs;
  pair<int, int> cpair;

  for (int i=0; i<points.size()-1; ++i) {
    pt p = points.at(i);
    pt q = points.at(i+1);
    if (q.x < p.x || (q.x == p.x && (q.y < p.y))) {
      swap(p,q);
    }
    g = abs(__gcd(q.x - p.x, q.y - p.y));
    cx = (q.x - p.x) / g;
    cy = (q.y - p.y) / g;
    assert (cx >= 0);
    cpair = make_pair(cx, cy);
    if(std::find(seen_once.begin(), seen_once.end(), cpair) != seen_once.end()) {
      seen_twice.push_back(cpair);
      gcd_of_dirs[cpair] = min(gcd_of_dirs[cpair], g);
    } else {
      seen_once.push_back(cpair);
      gcd_of_dirs[cpair] = g;
    }
  }

  for (int i=0; i<seen_twice.size(); ++i) {
    cx = seen_twice.at(i).first;
    cy = seen_twice.at(i).second;
    for (int k=1; k <= gcd_of_dirs[seen_twice.at(i)]; k++) {
      dx = k*cx;
      dy = k*cy;
      score = 0;
      bool alive = true;

      for (int sx=0; sx<m; sx++) {
        if (dx == 0) {
          y_lower_bound = 0;
          y_upper_bound = dy;
        }
        else if (sx < dx) {
          y_lower_bound = 0;
          y_upper_bound = n;
        }
        else {
          if (dy < 0) {
            y_lower_bound = n + dy;
            y_upper_bound = n;
          }
          if (dy == 0) {
            y_lower_bound = 0;
            y_upper_bound = 0;
          }
          if (dy > 0) {
            y_lower_bound = 0;
            y_upper_bound = dy;
          }
        }
        assert(y_lower_bound <= y_upper_bound);

        for (int sy=y_lower_bound; sy<y_upper_bound; sy++) {
          ax = sx;
          ay = sy;
          int run_length = 0;
          int this_line_score = 0;

          // scan the line
          while (true) {
            if ((ax >= 0) && (ay >= 0) && (ax < m) && (ay < n) && grid[ax][ay]) {
              run_length++;
            } else {
              if (run_length == 1) {
                alive = false;
                break;
              } else {
                this_line_score += (run_length+1) / 2;
                run_length = 0;
              }
            }
            if ((ax > m) || (ay > n) || (ax < 0) || (ay < 0)) {
              break;
            }
            ax += dx;
            ay += dy;
          }
          if (!alive) {
            // cerr << "FAILED run from " << sx << " " << sy << endl;
            break; // this (dx, dy) is stale
          } else {
            // cerr << "... scored " << this_line_score << " run from " << sx << " " << sy << endl;
            score += this_line_score;
            if (score > best_score) { alive=false; break; } // lol
          }
        }
        if (!alive) {
          score = 999999;
          break;
        }
      }
      // cerr << dx << " " << dy << " got result " << score << endl;
      // cerr << "---------------------" << endl;

      if (alive) {
        best_score = min(score, best_score);
      }
    }
  }
  if (best_score != 999999) {
    cout << best_score << endl;
  } else {
    cout << number_of_points_total << endl;
  }
}
