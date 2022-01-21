#define sqr(x) (x) * (x)
#include <bits/stdc++.h>

using namespace std;

constexpr int INFINITE(0x3f3f3f3f);
constexpr int MAXN(1e5 + 1);

bool planets[MAXN];
int leastJumps[MAXN];
int numberOfPlanets(0);

int32_t main() {
	std::ios_base::sync_with_stdio(false);
	std::cin.tie(NULL);

	cin >> numberOfPlanets;

	for (size_t i(1); i <= numberOfPlanets; ++i)
		cin >> planets[i];


	leastJumps[0] = 0;
	leastJumps[1] = 0;
	leastJumps[2] = planets[2] ? INFINITE : 1;

	for (size_t i(2); i <= numberOfPlanets; ++i) {
		if (not planets[i]) {
			leastJumps[i] = min(leastJumps[i - 1], leastJumps[i - 2]) + 1;
			/* dynamic programming */
			continue;
		}

		leastJumps[i] = INFINITE;
	}

	cout << leastJumps[numberOfPlanets];
}
