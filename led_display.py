
def num():
    number = input("enter a number between 1-5: ")
    if number in "12345":
        return number
    else:
        print("sorry try again...")
        return num()

array = []  #biggest array
number = num()

for elem in range(len(number)):  # first for loop
    lis = [[" "," "," "]for row in range(5)] # create subarrays 
    array.append(lis)


#the patterns are coded here:-
for i in range(len(number)):    
    if int(number[i]) == 1:  
        array[i][0][2]= array[i][1][2]= array[i][2][2] = array[i][3][2] = array[i][4][2] = "#"
    elif int(number[i]) == 2:
        array[i][0] = array[i][2] = array[i][4] = ["#","#","#"]
        array[i][1][2] = array[i][3][0] = "#"
    elif int(number[i]) == 3:
        array[i][0] = array[i][2] = array[i][4] = ["#","#","#"]
        array[i][1][2] = array[i][3][2] = "#"
    elif int(number[i]) == 4:
        array[i][2] = ["#","#","#"]
        array[i][1][0] = array[i][4][2] = array[i][3][2] = array[i][0][0] = "#"
    elif int(number[i]) == 5:
        array[i][0] = array[i][2] = array[i][4] = ["#","#","#"]
        array[i][1][0] = array[i][3][2] = "#"

#printing occurs here
for row in range(5):      
    for subarray in array:  
        for element in range(3):  
            print(subarray[row][element],end = "")
        print("  ",end = "") #THE GAP
    print() #THE NEWLINE
        
        
    
#array is the biggest list which contains the pattern for the number we type in.
# in first for loop we create one list per one digit of the input.(lets call it subarray)
# inside each subarray we create 5 rows 
# now we append each subarray to the biggest list we created on the start of the prgm.
# the structure looks like this:-
# start of array [start of subarray[start of row[ "elemnt","elemnt","elemnt"] end of row x 5 times]end of subarray x number of times as the input ] end of array
# which looks like this :- (assuming we put in two digits)
# [ [ [][][][][] ]  , [ [][][][][] ] ] 
# the patterns are stored inside each subarrays which is stored inside the biggest array
# now we print them in such an order where,
# we print first row of each subarray with a gap in between( lets call it 'THE GAP')
# then we print a "\n"(lets call it 'THE NEWLINE') 
# then we print the 2nd row of every subarray and repeat.
