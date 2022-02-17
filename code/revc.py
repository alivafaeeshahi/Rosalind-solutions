def read_data(file_name):
    import os
    current_path = os.path.dirname(__file__)
    new_path = os.path.join(current_path, '..', 'data')
    os.chdir(new_path)

    sequence = open(file_name).read().rstrip()
    return sequence

def reverse_complement(sequence):
    d_complemetary = {'A':'T', 'C':'G', 'G':'C', 'T':'A'}
    rev_sequence = sequence[::-1]
    revc_sequence = ''
    for nucleotide in rev_sequence:
        revc_sequence += d_complemetary[nucleotide] 
    return revc_sequence

def write_data(answer):
    with open('rosalind_revc_ans.txt', 'w') as f:
        f.write(answer)

if __name__ == '__main__':
    write_data(reverse_complement(read_data('rosalind_revc.txt')))
