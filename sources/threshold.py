
def threshold(a,th):
    m=len(a)
    n=len(a[0])
    for i in range(m):
        for j in range(n):
            if(a[i][j]<th):
                a[i][j]=0
                
            else:
                a[i][j]=255
                
    return np.array(a)
