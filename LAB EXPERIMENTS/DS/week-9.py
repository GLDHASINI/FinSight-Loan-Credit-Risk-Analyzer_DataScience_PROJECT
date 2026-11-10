from scipy.stats import bernoulli
p = 0.7
bernoulli_samples = bernoulli.rvs(p, size=10)
print("Probability of Passing:", p)
print("Student Outcomes (1=Pass, 0=Fail):")
print(bernoulli_samples)
print("\nProbability of Pass:")
print(bernoulli.pmf(1, p))
print("Probability of Fail:")
print(bernoulli.pmf(0, p))
