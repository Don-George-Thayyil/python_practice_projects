#print out a pyramid

def pyramid(a):
    rows = a
    k = 0
    i=rows
    while(rows-i < rows):
        for j in range(i):
            print("--", end=" ")
        
        d = 2*k+1
        
        for f in range(d):
            print(" *", end=" ")
            
        k = k+1
        i = i-1
        print("\n")


pyramid(8)
