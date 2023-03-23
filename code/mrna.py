from prot import read_data

def possible_mrna_count(sequence):
    d_codons = codons = {'F': ['UUU', 'UUC'],
              'L': ['UUA', 'UUG', 'CUU', 'CUC', 'CUA', 'CUG'],
              'S': ['UCU', 'UCC', 'UCA', 'UCG', 'AGU', 'AGC'],
              'Y': ['UAU', 'UAC'],
              'C': ['UGU', 'UGC'],
              'W': ['UGG'],
              'P': ['CCU', 'CCC', 'CCA', 'CCG'],
              'H': ['CAU', 'CAC'],
              'Q': ['CAA', 'CAG'],
              'R': ['CGU', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'],
              'V': ['GUU', 'GUC', 'GUA', 'GUG'],
              'A': ['GCU', 'GCC', 'GCA', 'GCG'],
              'D': ['GAU', 'GAC'],
              'E': ['GAA', 'GAG'],
              'G': ['GGU', 'GGC', 'GGA', 'GGG'],
              'I': ['AUU', 'AUC', 'AUA'],
              'M': ['AUG'],
              'T': ['ACU', 'ACC', 'ACA', 'ACG'],
              'N': ['AAU', 'AAC'],
              'K': ['AAA', 'AAG']}
    
    c = 1
    for nucleotide in sequence:
        c = c * len(d_codons[nucleotide])
    #counting stop codons:
    c = c * 3
    answer = c % 1000000
    return answer

def write_data(answer):
    with open('rosalind_mrna_ans.txt', 'w') as f:
        f.write(str(answer))

if __name__ == '__main__':
    write_data(possible_mrna_count(read_data('rosalind_mrna.txt')))