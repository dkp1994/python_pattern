'''
A 
B B 
C C C 
D D D D 
E E E E E 
'''
num = int(input("Enter number of rows : "))
for i in range(num):
    print((chr(65+i)+' ')*(i+1))