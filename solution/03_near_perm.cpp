#include <iostream>
using namespace std;

#define int long long

const int MOD = 998244353;

signed main() {

  int n, k;
  cin >> n >> k;

  if (k == 0) {
    cout << 1 << '\n';
  } else if (k >= n - 1) {
    int ans = 1;

    for (int i = 2; i <= n; i++) {
      ans = ans * i % MOD;
    }

    cout << ans << '\n';
  } else if (k == 1) {
    vector<int> dp(n + 1);

    dp[0] = 1;
    dp[1] = 1;

    for (int i = 2; i <= n; i++) {
      dp[i] = (dp[i - 1] + dp[i - 2]) % MOD;
    }

    cout << dp[n] << '\n';
  }

  return 0;
}
