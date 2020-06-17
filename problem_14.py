def get_chain_len(n):
    result=n
    count=1
    while result != 1:
        if result % 2 == 0:
            result = result/2
        else:
            result = result*3 + 1
        count+=1
    return count

def get_longest_chain():
    lens = [get_chain_len(i) for i in range(1, 1000000)]    
    return lens.index(max(lens))

get_longest_chain()