from iprb import read_data

def probability(n, k):
    from scipy.stats import binom
    prob = 1 - binom.cdf(n - 1, 2**k, 0.25)
    return prob

def write_data(answer):
    with open('rosalind_lia_ans.txt', 'w') as f:
        f.write(str(answer))

if __name__=='__main__':
    k, n = read_data('rosalind_lia.txt')
    write_data(probability(n, k))