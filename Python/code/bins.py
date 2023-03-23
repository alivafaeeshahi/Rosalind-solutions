import sys
sys.setrecursionlimit(100000)
def read_data(file_name):
    import os
    current_path = os.path.dirname(__file__)
    new_path = os.path.join(current_path, '..', 'data')
    os.chdir(new_path)
    l_data = open(file_name).read().rstrip().split('\n')
    source = [int(i) for i in l_data[2].split()]
    l_search = [int(i) for i in l_data[3].split()]

    return source, l_search

def bin_search(x, source, start, end):
    source = sorted(source)
    
    if end >= start:
        middle = (start + (end-1)) // 2

        if source[middle] == x:
            return middle
        elif source[middle] > x:
            return bin_search(x, source, start, middle-1)
        else:
            return bin_search(x, source, middle+1, end)
    else:
        return -1

def write_data(answer):
    with open('rosalind_bins_ans.txt', 'w') as f:
        ans = ''
        for i in answer:
            ans += str(i) + " "
        ans = ans[:-1]
        f.write(ans)

if __name__ == '__main__':
    l, l_s = read_data('rosalind_bins.txt')
    
    l_ans = []
    for i in l_s:
        l_ans.append(bin_search(i, l, 0, len(l)-1))
    print(l_ans)
    write_data(l_ans)
