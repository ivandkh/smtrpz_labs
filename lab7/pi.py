import numpy as np

def pi(n_iter):
    result = 0 
    for i in range(n_iter // 10_000):
        result += np.sum(np.sum(np.random.uniform(0,1, size=(10_000,2)) ** 2,axis=1) < 1)
    return result