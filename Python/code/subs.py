#Brute force approach

def read_data(file_name):
    import os
    current_path = os.path.dirname(__file__)
    new_path = os.path.join(current_path, '..', 'data')
    os.chdir(new_path)

    l_data = open(file_name).read().rstrip().split('\n')
    sequence = l_data[0]
    motif = l_data[1]
    return sequence, motif

def find_motif(sequence, motif):
    l_index = []
    for i in range(len(sequence) - len(motif) + 1):
        current_sequence =sequence[i:i+len(motif)]
        if current_sequence == motif:
            l_index.append(i + 1)
    return l_index

def write_data(answer):
    with open('rosalind_subs_ans.txt', 'w') as f:
        ans = ''
        for i in answer:
            ans += str(i) + " "
        ans = ans[:-1]
        f.write(ans)

if __name__ == '__main__':
    seq, motif = read_data('rosalind_subs.txt')
    write_data(find_motif(seq, motif))