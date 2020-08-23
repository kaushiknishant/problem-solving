def k_special(l,r,k):
    count = 0
    flag = 0
    for index in xrange(l,r+1):
        ls = map(int,str(index))
        print(ls)
        for num in ls:
            if num % k !=0:
                print('h')
                flag = 1
            else:
                
    return count

if __name__ == '__main__':
    n = int(raw_input())
    for i in xrange(n):
        lt = list(map(int,raw_input().split()))
        l = lt[0]
        r = lt[1]
        k = lt[2]
        print(k_special(l,r,k))
       