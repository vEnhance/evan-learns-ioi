// https://atcoder.jp/contests/arc139/tasks/arc139_e

#include "cmath"
#include "iostream"
#include "atcoder/all"

using namespace std;
using namespace atcoder;

typedef modint998244353 mint;
typedef long long ll;

const ll MOD = 998244353;
const bool DEBUG = false;
const bool FORCE_NTT = true;

mint meow(ll r, ll n) {
  assert(r % 2 == 1);
  if (n <= 2e5 && !FORCE_NTT) {
    mint binom_coeff = 1;
    mint answer_divided_by_r = 0;
    for (int k=0; k<=n; ++k) {
      if (k!=0) {
        binom_coeff *= (n+1-k);
        binom_coeff /= k;
      }
      if (DEBUG) {
        cout << binom_coeff.val() << " ";
      }
      if (n%2 == 0) {
        if (k % r == n/2 % r) {
          answer_divided_by_r += binom_coeff;
        }
      }
      if (n%2 == 1) {
        if (k % r == (n+r)/2 % r) {
          answer_divided_by_r += binom_coeff;
        }
      }
    }
    if (DEBUG) {
      cout << endl;
    }
    return answer_divided_by_r * r;
  } else {
    assert(r <= 1e5);
    vector<mint> v(r, 0);  // please send help orz
    v[0] = 1;
    // v = 1 + zeta where zeta is a primitive r'th root of unity

    int num_bits = __lg(n) + 1;
    if (DEBUG) {
      cout << "number of bits = " << num_bits << endl;
    }
    for (int i=0; i < num_bits; i++) {
      if (DEBUG) {
        cout << "i = " << i << endl;
        cout << (n >> (num_bits-1-i)) << endl;
      }
      if ((n >> (num_bits - 1 - i)) % 2 == 1) {
        v = convolution(v, {1, 1});
        assert(v.size() == r+1);
        v.at(0) += v.at(r);
        v.pop_back();
        if (DEBUG) {
          for (int i=0; i<r; ++i) {
            cout << v.at(i).val() << "\t";
          }
          cout << endl;
        }
      }

      // square
      if (i != num_bits - 1) {
        v = convolution(v, v);
        assert(v.size() == 2*r-1);
        for (int i=r; i<2*r-1; i++) {
          v.at(i-r) += v.at(i);
        }
        for (int i=r; i<2*r-1; i++) {
          v.pop_back();
        }
        if (DEBUG) {
          for (int i=0; i<r; ++i) {
            cout << v.at(i).val() << "\t";
          }
          cout << endl;
        }
      }
    }
    // let's debug code guys
    assert(v.size() == r);
    int k = (n%2==0 ? n/2 : (n+r)/2) % r;
    if (DEBUG) {
      for (int i=0; i<r; ++i) {
        cout << v.at(i).val() << "\t";
      }
      cout << endl;
      cout << "r = " << r << endl;
      cout << "n = " << n << endl;
      cout << "k = " << k << endl;
    }
    // great, now we computed (1+zeta)^n YAYYY
    return v.at(k) * r;
  }
}

mint get_final_answer_to_print(ll H, ll W) {
  if ((H % 2 == 0) && (W % 2 == 0)) {
    return 2;
  }
  else if ((H % 2 == 1) && (W % 2 == 0)) {
    return meow(H, W);
  }
  else if ((H % 2 == 0) && (W % 2 == 1)) {
    return meow(W, H);
  }
  else if (H <= W) {
    return meow(H, W);
  }
  else {
    return meow(W, H);
  }
}

int main() {
  ll H;
  ll W;
  cin >> H >> W;
  cout << get_final_answer_to_print(H, W).val() << endl;
}
