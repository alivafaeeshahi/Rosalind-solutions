def read_data(file_name):
    import os
    current_path = os.path.dirname(__file__)
    new_path = os.path.join(current_path, '..', 'data')
    os.chdir(new_path)

    l_data = [int(i) for i in open(file_name).read().rstrip().split()]
    return l_data

def rabbit_fib(n, k):
    if n not in d_populations.keys():
        n1 = rabbit_fib(n-1, k)
        n2 = rabbit_fib(n-2, k)
        population = (k*n2) + n1
        d_populations.update({n:population})
        return population
    else:
        return d_populations[n]

def write_data(answer):
    with open('rosalind_fib_ans.txt', 'w') as f:
        f.write(str(answer))

if __name__ == '__main__':
    parameters = read_data('rosalind_fib.txt')
    d_populations = {1:1, 2:1}
    answer = rabbit_fib(parameters[0], parameters[1])
    write_data(answer)