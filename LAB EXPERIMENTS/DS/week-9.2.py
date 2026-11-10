import numpy as np
from scipy import stats
from statsmodels.stats.weightstats import ztest
print("----- Z-Test -----")
sample_marks = np.array([78, 82, 85, 88, 90, 76, 95, 89, 84, 91])
population_mean = 80
z_stat, p_value = ztest(sample_marks, value=population_mean)
print("Sample Marks:")
print(sample_marks)
print("\nPopulation Mean:", population_mean)
print("\nZ-Statistic:", z_stat)
print("P-Value:", p_value)
alpha = 0.05
if p_value < alpha:
    print("\nResult: Reject Null Hypothesis")
else:
    print("\nResult: Fail to Reject Null Hypothesis")
