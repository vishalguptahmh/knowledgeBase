print("Hello, World!")

num = 100
num2 = num

print("num pointer address :",id(num))
print("num2 pointer address :",id(num2))

arr= [1,2,3,4,5]

numm = []
def rightRotate(arr,k):
    lenth = len(arr)
    count = 0
    for i in range(lenth):
        if count > k : 
            numm.append(arr[i])
        count+=1

    count = 0
    for i in range(lenth):
        if count <= k : 
            numm.append(arr[i])
        count+=1


rightRotate(arr,2)
print(numm)