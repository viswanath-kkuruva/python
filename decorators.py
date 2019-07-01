import time

# basic timer decorator

def timer(fun):
	def wrapper(n):
		start = time.time()
		fun_result = fun(n)
		end = time.time()
		print('Execution Time : {} sec.'.format(end-start))
		return fun_result
	return wrapper

@timer
def counter(n):
	for i in range(n, 0, -1):
		print(i)
		time.sleep(0.1T)

counter(5)