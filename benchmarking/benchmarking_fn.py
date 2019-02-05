# one basic example to understaning decorator is:
# 1. we want to debug a function execution time, what we do, we add time before and after the function call
# 2. if the same function is used in lot of places, we move the timer inside the function, first line and last line
# 3. we solve it for one function, but if we want to able to timer multiple functions(different)
#	 without adding timer for every single of them
# 4 hence decorator

# example to understand function return function
def function_return_function():
	def get_function():
		print('inside getfunction')
		def returned_function():
			print("inside returned_function")
			print(1)
		print("outside returned_function")
		return returned_function

	#returned_function()
	#x = get_function()
	#print(x)
	#x()
#function_return_function()

# combine 1 and 2:
def time_fn(ori_fn):
	def new_fn(*arg, **kwargs):
		import datetime
		before = datetime.datetime.now()
		x = ori_fn(*args, **kwargs)
		after = datetime.datetime.now()
		print("Elapsed Time = {0}".format(after - before))
		return x
	return new_fn()

@time_fn
def example_function():
	import time
	time.sleep(3)

