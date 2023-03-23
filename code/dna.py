def read_data(file_name):
    import os
    current_path = os.path.dirname(__file__)
    new_path = os.path.join(current_path, '..', 'data')
    os.chdir(new_path)

    sequence1 = open(file_name).read().rstrip()
    return sequence1

def base_count(sequence):
    l_count = [sequence.count('A'), sequence.count('C'), sequence.count('G'), sequence.count('T')]
    return l_count

def write_data(answer):
    with open('rosalind_dna_ans.txt', 'w') as f:
        final_answer = str()
        for i in answer:
            final_answer += str(i) + " "
        final_answer = final_answer.rstrip()
        f.write(final_answer)

if __name__ == '__main__':
    write_data(base_count(read_data('rosalind_dna.txt')))