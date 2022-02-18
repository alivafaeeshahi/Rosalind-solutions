def read_data(file_name):
    import os
    current_path = os.path.dirname(__file__)
    new_path = os.path.join(current_path, '..', 'data')
    os.chdir(new_path)

    data = open(file_name).read().rstrip().split('\n')
    sequence_1 = data[0]
    sequence_2 = data[1]
    return sequence_1, sequence_2

def hamm_distance(sequence1, sequence2):
    d = 0
    for i in range(len(sequence1)):
        if sequence1[i] != sequence2[i]:
            d += 1
    
    return d

def write_data(answer):
    with open('rosalind_hamm_ans.txt', 'w') as f:
        f.write(str(answer))

if __name__ == '__main__':
    seq1, seq2 = read_data('rosalind_hamm.txt')
    write_data(hamm_distance(seq1, seq2))




