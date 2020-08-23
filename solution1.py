def smallest_anti_pal(s):
    if s == s[::-1]:
        return -1
    else:
       string = sorted(s, key=str.upper)
       listToStr = ''.join(map(str, string)) 
       return listToStr
  
if __name__ == "__main__":
    test = int(raw_input())
    while test > 0 :
        strr = raw_input()
        print(smallest_anti_pal(strr))
        test -= 1