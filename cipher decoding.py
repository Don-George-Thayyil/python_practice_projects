#this decoder is used for decoding the American civil war ciphers


cipher = input("Enter the words: ")
key = input("Enter key values: ")
column = input("column number: ")
COL = int(column)
row = input("row number: ")
ROW = int(row)
start = 0
stop = ROW
cipher_list = list(cipher.split())
key_list = [int(i) for i in key.split()]
length = len(cipher_list)
array = [None]*COL
text = ""

for k in key_list:
    if k < 0:
        col = cipher_list[start:stop]
    elif k > 0:
        col = list(reversed(cipher_list[start:stop]))
    array[abs(k)-1] = col
    start += ROW
    stop += ROW

    
   




print(array)









