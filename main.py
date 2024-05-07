a= numpy.random.randint(2,size=(5, 5))
# Set the border elements to 0
a[0, :] = 0  # First row
a[-1, :] = 0  # Last row
a[:, 0] = 0  # First column
a[:, -1] = 0  # Last column
print(a)
b = grid2_function(a)
print(b)