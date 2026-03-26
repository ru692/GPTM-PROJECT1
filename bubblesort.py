import time
import matplotlib.pyplot as plt
def bubblesort(array):
    n=len(array)
    for i in range(n-1):
        swapped=False
        for j in range(n-1-i):
            if array[j]>array[j+1]:
                array[j],array[j+1]=array[j+1],array[j]
            swapped=True
        if swapped==False:
            Break
    return array
array=[]
n=int(input("how many elements you want in your array:"))
for i in range(n):
    array.append(int(input("enter %d element:"%j)))
print(f"before swapping:{array}")
array=bubblesort(array)
x=list(range(1,10000))
plt.plot(x,[y*y for y in x])
print("bubblesort time complexity is")
plt.xlabel("input")
plt.ylabel("time")
plt.show()
