import numpy as np
def multiply(*args):
	print(args)
	return np.prod(args) * 4 *2

if __name__=='__main__':
	multiply(2,3)
