import numpy as np

arr = np.random.rand(3,3)
def my_function(arg1:int, arg2:str=...):
    print(type(arg2))
    print(arr[arg2,0]) # get the first item of the last dim
    print(arr)

my_function(1) # still works -> no strict type checking