#pragma GCC optimize ("O3")

#include <assert.h>
#include <algorithm>
#include <numeric>
#include <vector>
#include <iostream>

using namespace std;

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
  cerr << number_of_points_total << " points read" << endl;
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
  cerr << points.size() << " points in the convex hull" << endl;



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
    if(std::find(seen_once.begin(), seen_twice.end(), cpair) != seen_once.end()) {
      seen_twice.push_back(cpair);
    } else {
      seen_once.push_back(cpair);
        /* v does not contain x */
    }
  }


  for (int i=0; i<seen_twice.size()-1; ++i) {
    cx = seen_twice.at(i).first;
    cy = seen_twice.at(i).second;
    for (int k=1; (k*cx <= m) && (k*abs(cy) <= n); k++) {
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
            cerr << "FAILED run from " << sx << " " << sy << endl;
            break; // this (dx, dy) is stale
          } else {
            cerr << "... scored " << this_line_score << " run from " << sx << " " << sy << endl;
            score += this_line_score;
          }
        }
        if (!alive) {
          score = 999999;
          break;
        }
      }
      cerr << dx << " " << dy << " got result " << score << endl;
      cerr << "---------------------" << endl;

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
