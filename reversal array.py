def reverselist(A,start,end):
	while start < end:
		A[start], A[end] = A[end], A[start]
		start += 1
		end -= 1
	

A = [5,4,3,2,1]
# print[A]
print("reversal Array is")
reverselist(A,0,4)
print(A)