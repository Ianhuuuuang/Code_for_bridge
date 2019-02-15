# def myzip(*seqs):
#     seqs = [list(s) for s in seqs]    
#     while all(seqs):
#         yield tuple(s.pop(0) for s in seqs)

# print(list(myzip('abc','xyz123')))

# seqs = ['xyz','abc','uvw']
# res = [list(s) for s in seqs]
# out = tuple(s[0] for s in res)
# print(out)
S = '654321'
L = list(S)
D = enumerate(L)
DD = list(D)
print(DD)