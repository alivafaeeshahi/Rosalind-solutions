def read_data(file_name):
    import os
    current_path = os.path.dirname(__file__)
    new_path = os.path.join(current_path, '..', 'data')
    os.chdir(new_path)

    data = open(file_name).read().rstrip().split('>')[1:]
    d_sequences = {}
    for sequence in data:
        l_sequence = sequence.split('\n')
        seq_name = l_sequence[0]
        new_sequence = ''.join(l_sequence[1:])
        d_sequences.update({seq_name:new_sequence})
    
    return d_sequences

def GC_content(sequence):
    return ((sequence.count('C') + sequence.count('G')) / len(sequence)) * 100

def write_asnwer(answer):
    with open('rosalind_gc_ans.txt', 'w') as f:
        f.write(answer)

if __name__ == '__main__':
    d_seqs = read_data('rosalind_gc.txt')
    l_scores = []
    for k,v in d_seqs.items():
        l_scores.append((GC_content(v), k))
    l_scores = sorted(l_scores, reverse=True)
    highest_GC = l_scores[0]
    answer = highest_GC[1] + '\n' + str(highest_GC[0])
    write_asnwer(answer)