import numpy as np

mylist = [1,2,3]
print("mylist type:", type(mylist))

myarray = np.array([1, 2, 3, 4])
print("myarray:", myarray)
print("myarray type:", type(myarray))

print("np.arange(0,10,2):", np.arange(0,10,2))

print("np.zeros(shape=(10,5)):\n", np.zeros(shape=(10,5)))

print("type(0):",type(0))

print("type(0.):",type(0.))

print("np.ones(shape=(2,4)):\n", np.ones(shape=(2,4)))
print("np.ones((2,4)):\n", np.ones((2,4)))

np.random.seed(101)
arr = np.random.randint(0,100,10)
print("arr:", arr)

arr2 = np.random.randint(0,100,10)
print("arr2:", arr2)

print("arr.max():", arr.max())
print("arr.argmax(): ", arr.argmax())

print("arr.min():", arr.min())
print("arr.argmin(): ", arr.argmin())

print("arr.mean():", arr.mean())

print("arr.shape:", arr.shape)

print("arr.reshape(2,5):\n", arr.reshape(2,5))

mat = np.arange(0,100).reshape(10,10)
print("mat:\n", mat)
print("mat.shape:", mat.shape)

row = 0
col = 1
print("mat[row,col]:", mat[row,col])
print("mat[4,6]:", mat[4,6])
print("mat[:,1]:", mat[:,1])
print("mat[:,1].shape:", mat[:,1].shape)
print("mat[:,1].reshape(1,10):", mat[:,1].reshape(1,10))
print("mat[2,:]:", mat[2,:])
print("mat[0:3,0:3]:\n", mat[0:3,0:3])

mynewmat = mat.copy()
print("mynewmat:\n", mynewmat)
mynewmat[0:6,:] = 999
print("mynewmat:\n", mynewmat)
