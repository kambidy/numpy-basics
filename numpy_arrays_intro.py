import numpy as np

np1 = np.array([0,1,2,3,4,5,6,7,8,9])

print(np1)
#printing the shape of the array

print(np1.shape)

#creating a range of numpy arrays

np2 = np.arange(10)
print(np2)

#making steps in the range

np3 = np.arange(0,10,2)#making a step of 2(apparently makine an array of even numbers)
print(np3)

#making an array of zeros

np4 = np.zeros(10)

print(np4)

#multidimensional array of zeros

np5 = np.zeros((2,10))
print(np5)

#multidimensional array of full
print("---------------------")
np6 = np.full((10,2),6)
print(np6)

#converting python list to np array
py_list = [1,2,3,4,5]
np7 = np.array(py_list)
print(np7)
print(np7[0])

#np (for loops)

np8 = np.arange(10)

for i in range(len(np8)):
    print(np8[i])












