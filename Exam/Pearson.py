import math
import scipy.stats


def pearson(x, y):
    n = len(x)
    a = sum(s * t for (s, t) in zip(x, y)) * n
    b = sum(x) * sum(y)
    c = math.sqrt(sum(s * s for s in x) * n - math.pow(sum(x), 2))
    d = math.sqrt(sum(s * s for s in y) * n - math.pow(sum(y), 2))
    return (a - b) / (c * d)


print(scipy.stats.norm.ppf(0.95))
print(scipy.stats.t.ppf(0.95, 1))
print(scipy.stats.chi2.ppf(0.95, 1))
print(scipy.stats.f.ppf(0.95, 1, 1))

print(
    pearson(
        [116.5, 120.8, 124.4, 125.5, 131.7, 136.2, 138.7, 140.2, 146.8, 149.6, 153, 158.2, 163.2, 170.5, 178.2, 185.9],
        [255.7, 263.3, 275.4, 278.3, 296.7, 309.3, 315.8, 318.8, 330, 340.2, 350.7, 367.3, 381.3, 406.5, 430.8, 451.5]))
