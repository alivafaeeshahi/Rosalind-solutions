def read_data(file_name):
    import os
    current_path = os.path.dirname(__file__)
    new_path = os.path.join(current_path, '..', 'data')
    os.chdir(new_path)

    sequence = open(file_name).read().rstrip()
    return sequence

def write_data(answer):
    with open('rosalind_prot_ans.txt', 'w') as f:
        f.write(str(answer))

if __name__ == '__main__':
    from Bio.Seq import Seq
    data = Seq(read_data('rosalind_prot.txt'))
    protein = data.translate(to_stop=True)
    write_data(protein)

