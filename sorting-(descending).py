#sort them in a descending fasion

def descender(block):
    
    array = []
   
    finished_arr =[]
    array = block

    for i in range(0,len(array)):
        for j in range(0,len(array)):
            if array[j]<=array[i]:
                temp = array[j]
                array[j] = array[i]
                array[i] = temp
    
    for k in range(0,len(array)):
        if array[k] not in finished_arr:
            h = array[k]
            finished_arr.append(h)
            
    return finished_arr




        
