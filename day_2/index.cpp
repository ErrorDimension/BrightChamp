#define sqr(x) (x) * (x)
#include <iostream>

constexpr int INFINITE(0x3f3f3f3f);

bool compare(int& a, int& b)
{
	if ((!(a & 1)) && (!(b & 1)) && a >= b)
		return true;
	if ((a & 1) && (b & 1) && a <= b)
		return true;
	if ((a & 1) && (!(b & 1)))
		return false;
	return false;
}

void sort(int* m_array, int&& m_size, bool (*m_compare)(int&, int&)) {
	for (size_t i(0); i < m_size - 1; ++i)
		for (size_t j(i + 1); j < m_size; ++j)
			if (m_compare(m_array[i], m_array[j]))
				std::swap(m_array[i], m_array[j]);
}

int32_t main() {
	std::ios_base::sync_with_stdio(false);
	std::cin.tie(NULL);

	int array_[10]{ 1, 2, 3, 4, 5, 6, 7, 7, 9, 6 };

	sort(array_, 10, compare);

	for (size_t i(0); i < 10; ++i) {
		std::cout << array_[i] << ' ';
	}
}
