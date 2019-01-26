def min1(*args):
    res=args[0]
    for arg in args[1:]:
        if arg < res:
            res = arg
    return res
    
def min2(head,*body):
    for para in body:
        if para < head:
            head = para
    return head

def min3(*args):
    tmp = list(args)
    tmp.sort()
    return tmp[0]

print(min1([2,2],[1,1],[3,3]))
print(min2([2,2],[1,1],[3,3]))
print(min3([2,2],[1,1],[3,3]))
