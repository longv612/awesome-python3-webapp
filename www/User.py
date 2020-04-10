# -*- coding:utf-8 -*-

# /usr/bin/env python

__author__ = 'Five'


from www.orm  import Model, StringField, InterField, execute


class User(Model):
	__table__ = 'users'
	id = InterField(primary_key=True)
	name = StringField()
	
	
user = User(id=123, name='Five')
user.save()