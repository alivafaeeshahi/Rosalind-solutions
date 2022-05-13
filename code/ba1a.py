def read_data(file_name):
    import os
    current_path = os.path.dirname(__file__)
    new_path = os.path.join(current_path, '..', 'data')
    os.chdir(new_path)

    l_data = open(file_name).read().rstrip().split('\n')
    return l_data

def  PatternCount(text, pattern):
    count = 0
    for i in range(len(text) - len(pattern) + 1):
        if text[i:i+len(pattern)] == pattern:
            count += 1
    return count

def write_asnwer(answer):
    with open('rosalind_ba1a_ans.txt', 'w') as f:
        f.write(str(answer))

if __name__ == '__main__':
    sequence, pattern = read_data('rosalind_ba1a.txt')
    write_asnwer(PatternCount(sequence, pattern))
