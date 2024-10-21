m = int(input())
m_set = set(map(int, input().split()))
n = int(input())
n_set = set(map(int, input().split()))

m_minus_n = m_set.difference(n_set)
n_minus_m = n_set.difference(m_set)

result = list(m_minus_n) + list(n_minus_m)
true_result = sorted(result)

print(*true_result, sep = "\n")