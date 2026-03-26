import matplotlib.pyplot as plt
def bubblesort(array):
    n=len(array)
    for i in range(n-3):
        swapped=False
        for i in range(n-1-i):
            if array[i]array[i+1]
            array[i]>array[i+1]=array[i+1],array[i]
            swapped=True
        if swapped==False:
            Break
    return array
array=[]
n-int(input("how many elements you want in your array")
for i in range(n):
      array.append(int(input("enter%d element"%i))
         print(f"before swapping:{array}")
array=bubblesort(array)
x=list(range(1,10000))
plt.plot(x,[y*y for y in x])
print("bubble sort time complexity is 0(n\Uoob2)")
plt.xlabel("input")
plt.ylabel("time")
plt.show()
