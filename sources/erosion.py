def erosion(a):
    m=len(a)
    n=len(a[0])
    b=[[]*m]
    b=[]
    for i in range(m):
        c=[]
        for j in range(n):
            arr=[]
            if i-1>=0:
                arr.append(a[i-1][j])
                
            else:
                arr.append(0)
                
            if i+1<=m-1:
                arr.append(a[i+1][j])
                
            else:
                arr.append(0)
                
            if j+1<=n-1:
                arr.append(a[i][j+1])
                
            else:
                arr.append(0)
                
            if j-1>=0:
                arr.append(a[i][j-1])
                
            else:
                arr.append(0)
                
            if i-1>=0 and j-1>=0:
                arr.append(a[i-1][j-1])

            else:
                arr.append(0)
                
            if i-1>=0 and j+1<=n-1:
                arr.append(a[i-1][j+1])
                
            else:
                arr.append(0)
                
            if i+1<=m-1 and j-1>=0:
                arr.append(a[i+1][j-1])
                
            else:
                arr.append(0)
                
            if i+1<=m-1 and j+1<=n-1:
                arr.append(a[i+1][j+1])
                
            else:
                arr.append(0)
              
            c.append(min(arr))
                    
        b.append(c)
        
    b=np.array(b)
    b=b.astype(np.uint8)
    return b
