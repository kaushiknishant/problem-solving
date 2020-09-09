def tower_of_brahma(n,A,C,B):
    if n == 1:
        print("Move disk {0} from rod {1} to rod {2}".format(n,A,C))
        return
    tower_of_brahma(n-1,A,B,C)
    print("Move disk {0} from rod {1} to rod {2}".format(n,A,C))
    tower_of_brahma(n-1,B,C,A)
    
if __name__ == '__main__' :
    tower_of_brahma(3,'A','C','B')