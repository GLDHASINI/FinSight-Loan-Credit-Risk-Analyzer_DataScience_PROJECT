from scipy.stats import binom
n = 10
p = 0.7
k = 8
binomial_probability = binom.pmf(k, n, p)
print("Number of Students:", n)
print("Probability of Passing:", p)
print(f"\nProbability that exactly {k} students pass:")
print(binomial_probability)
random_binomial = binom.rvs(n, p, size=5)
print("\nRandom Binomial Outcomes:")
print(random_binomial)
