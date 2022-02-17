def read_data(file_name):
    import os
    current_path = os.path.dirname(__file__)
    new_path = os.path.join(current_path, '..', 'data')
    os.chdir(new_path)

    l_data = [int(i) for i in open(file_name).read().rstrip().split()]
    return l_data

def P_dominant(k, m ,n):
    t = m+n+k
    probability = ((k*(k-1)) + ((k*m) + (m*k)) + ((k*n) + (n*k)) + (3/4 * m*(m-1)) + (1/2 * ((m*n) + (n*m)))) / (t*(t-1))
    return probability

def write_data(answer):
    with open('rosalind_iprb_ans.txt', 'w') as f:
        f.write(str(answer))

if __name__ == '__main__':
    parameters = read_data('rosalind_iprb.txt')
    write_data(P_dominant(parameters[0], parameters[1], parameters[2]))