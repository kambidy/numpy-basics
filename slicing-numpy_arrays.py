import numpy as np

#slicing numpy arrays

np1 = np.array([1,2,3,4,5,6,7,8,9])

#returning 2,3,4,5

print(np1[1:5])

#return 4 through 9

print(np1[3:])

#return negative slices

print(np1[-3:-1])

#printing through steps

print(np1[1:5])#2-5
print(np1[1:5:2])#2-5 in 2 steps


#go through every thing in 2 steps

print(np1[::2])

#slicing 2-D arrays

np2 = np.array([[1,2,3,4,5],[6,7,8,9,10]])
#pulling item

print(np2[1,2])

#slicing
print(np2[0:2,1:3])
