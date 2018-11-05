import sys


n = len(sys.argv)
num1 = sys.argv[1];
num2 = sys.argv[3];
num3 = sys.argv [5];
a = sys.argv[2]
b = sys.argv[4]
'''for x in range(0,n-1,2):
	num[x]=sys.argv[x]
	print(x)'''

if a == '+':
	num2= int(num1 )+int(num2);
elif a == '-':
	num2 = int(num1) - int(num2);
elif a == '*':
	num2 = int(num2) * int(num1)

elif  a == '/':
	num2 = int(num1)/(num2);


print(num2)

if b == '+':
	num3= int(num3 )+int(num2);
elif b == '-':
	num3 = int(num3) - int(num2);
elif b == '*':
	num3 = int(num3) * int(num1)

elif  b == '/':
	num3 = int(num2)/int (num3);
print(num3)

