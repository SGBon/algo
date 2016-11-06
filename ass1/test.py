def anyzero(x):
    n = len(x)
    if n == 1:
        return x[0] == 0
    elif n == 0 :
        return False
    else:
        y = n/3
        y2 = 2*n/3
        return(anyzero(x[:y]) or anyzero(x[y:y2]) or anyzero(x[y2:]))

if __name__ == "__main__":
    l1 = [0,4,1,3,5,0,2,1,0,3]
    l2 = [1,2,3,4,5,6,7,8,9,10]
    l3 = []
    print anyzero(l1)
    print anyzero(l2)
    print anyzero(l3)
