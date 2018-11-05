list=[1,2,3,4,5,6,7,8,9,10]
even_sum=0
odd_sum=0
even_count=0
odd_count=0
for i in list:
	if(i%2==0):
		even_sum+=i
		even_count+=1
	elif(i%2!=0):
		odd_sum+=i
		odd_count+=1
print("sum of even is",even_sum)
print("sum of odd is",odd_sum)
print("average of even",even_sum/even_count)
print("average of odd",odd_sum/odd_count)