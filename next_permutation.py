def next_permutation(numbers):
    li = []
    idx1 = 0
    idx2 = 0
    for ch in numbers:
        li.append(ch)
    for i in range(len(li)):
        if li[i] < li[i+1]:
            idx1 = 1
            # print(idx1)
            break
    for i in range(len(li)-1,-1,-1):
        print(i)
        if li[i] > li[idx1]:
            idx2 = i
            break
    li[idx1],li[idx2] = li[idx2],li[idx1]
    li[idx1:len(li)].reverse()
    str1 = ''.join(list1)
    return str1


if __name__ == '__main__':
    nums ='13542'
    next_permutation(nums)