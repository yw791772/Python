def time_fn(ori_fn):
	print("decorating")
	def new_fn(*args, **kwargs):
		print("starting timer")
		import datetime
		start = datetime.datetime.now()
		x = ori_fn(*args, **kwargs)
		end = datetime.datetime.now()
		print("Elapsed Time = {0}".format(end - start))
		return x
	return new_fn

def time_all_class_methods(Cls):
	class NewCls(obj):
		def __init__(self, *args, **kwargs):
			self.o_instance = Cls(*args, **kwargs)
		def __getattribute__(self, s):
			try:
				x = super(NewCls, self).__getattribute__(s)
			except AttributeError:
				pass
			else:
				return x
			x = self.o_instance.__getattribute__(s)
			if type(x) == type(self.__init__):
				return time_fn(x)
			else:
				return x
return NewCls

