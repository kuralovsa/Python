def gen_prime(x):
    multiples = []
    results = []
    for i in range(2, x+1):
        if i not in multiples:
            results.append(i)
            for j in range(i*i, x+1, i):
                multiples.append(j)

    return results
import timeit
start_time = timeit.default_timer()
gen_prime(3000)
print(timeit.default_timer() - start_time)
