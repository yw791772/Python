# approach 1, adding decorator for the function that needed
def requires_admin(fn):
	def ret_fn(*args, **kwargs):
		permissions = get_permissions(current_user_id())
		if 'administrator' in permissions:
			return fn(*args, **kwargs)
		else:
			raise Exception("Not allowed")
	return ret_fn

def requires_logged_in(fn):
	def ret_fn(*args, **kwargs):
		permissions = get_permissions(current_user_id())
		if 'logged_in' in permissions:
			return fn(*args, **kwargs)
		else:
			raise Exception("Not allowed")
	return ret_fn

def requires_premium_member(fn):
	def ret_fn(*args, **kwargs):
		permissions = get_permissions(current_user_id)
		if 'premium_member' in permissions:
			return fn(*args, **kwargs)
		else:
			raise Exception("Not allowed")
	return ret_fn

@requires_admin
def current_user_id():
	# return user id or None

def get_permissions(user_id):
	# return a list of avaialble permission for a given user

def delete_user(user_id):
	# delete a user

@requires_logged_in
def new_game():
	# logged in user can start a new game

@requires_premium_member
def premium_checkpoint():
	# check the game progress, available for premium members

# a better approach, create a function that return a decorator:
def requires_permission(permission):
	def decorator(fn):
		def decorated(*args, **kwargs):
			permissions = get_permissions(current_user_id())
			if permission in permissions:
				return fn(*args, **kwargs)
			else:
				raise Exception("Not allowed")
		return decorated
	return decorator

def get_permissions(user_id):
	return ["logged_in"]

def current_user_id():
	return 1

@requires_permission('administrator')
def delete_user(user_id):
	# delete a user

@requires_permission('logged_in')
def new_game():
	# logged in user can start a new game

@requires_permission('premium_member')
def premium_checkpoint():
	# check the game progress, available for premium members