def my_range(start,stop,step=1):
    while start<stop:
        yield start
        start+=step
def my_map(func,*my_list):
    for i in my_list:
        yield func(i)
def myzip_2x(*seqs):
    its = [iter(seq) for seq in seqs]
    res = []
    while True:
        try:
            res.append(tuple([next(it) for it in its]))   
        except StopIteration:
            break
    return res

def myzip_3x(*seqs):
    its = [iter(seq) for seq in seqs]
    while True:
        try:
            yield tuple([next(it) for it in its])         
        except StopIteration:
            return

    
