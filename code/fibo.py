def read_data(file_name):
    import os
    current_path = os.path.dirname(__file__)
    new_path = os.path.join(current_path, '..', 'data')
    os.chdir(new_path)
    
    data = int(open(file_name).read().rstrip())
    return data

def fib(n):
    if n == 0:
        return 0
    l_fib = [None] * (n+1)
    l_fib[0], l_fib[1] = 0, 1
    for i in range(2, n+1):
        l_fib[i] = l_fib[i-1] + l_fib[i-2]
    return l_fib[-1]

def write_asnwer(answer):
    with open('rosalind_fibo_ans.txt', 'w') as f:
        f.write(str(answer))

if __name__ == '__main__':
    n = read_data('rosalind_fibo.txt')
    write_asnwer(fib(n))