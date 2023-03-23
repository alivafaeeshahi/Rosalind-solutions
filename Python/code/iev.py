def read_data(file_name):
    import os
    current_path = os.path.dirname(__file__)
    new_path = os.path.join(current_path, '..', 'data')
    os.chdir(new_path)

    l_data = [int(i) for i in open(file_name).read().rstrip().split()]
    return l_data

def expected_offspring(l_data):
    expected = (2*(l_data[0] + l_data[1] + l_data[2])) + ((3/2) * l_data[3]) + (l_data[4])
    return expected

def write_data(answer):
    with open('rosalind_iev_ans.txt', 'w') as f:
        f.write(str(answer))

if __name__ == '__main__':
    write_data(expected_offspring(read_data('rosalind_iev.txt')))

