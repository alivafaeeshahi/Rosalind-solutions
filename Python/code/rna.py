def read_data(file_name):
    import os
    current_path = os.path.dirname(__file__)
    new_path = os.path.join(current_path, '..', 'data')
    os.chdir(new_path)

    sequence = open(file_name).read().rstrip()
    return sequence

def transcription(sequence):
    transcribed_sequence = sequence.replace('T', 'U')
    return transcribed_sequence

def write_data(answer):
    with open('rosalind_rna_ans.txt', 'w') as f:
        f.write(answer)

if __name__ == '__main__':
    write_data(transcription(read_data('rosalind_rna.txt')))