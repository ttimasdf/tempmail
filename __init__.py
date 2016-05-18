from sqlobject import AND

import models

def get_or_create_domain(name):
	return name

def get_or_create_user(name, domain):
	try:
		user = models.User.select(AND(models.User.q.name==name, models.User.q.domain==domain))[0]
	except IndexError:
		user = models.User(name=name, domain=domain)
	return user
