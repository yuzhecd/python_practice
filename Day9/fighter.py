#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-07-02 21:46:57
# @Author  : yuzhecd (yuzhecd@163.com)
# @Link    : --------
# @Version : $Id$

from abc import ABCMeta, abstractmethod
from random import randint, randrange

class Fighter(object, metaclass=ABCMeta):
	"""
	Fighter
	"""
	# use __slots__ limit the number of Fighter

	__slots__ = ('_name', '_hp')

	def __init__(self, name, hp):
		"""
		init method
		:param name: NAME
		:param hp: LIVE
		"""
		self._name = name
		self._hp = hp

	@property
	def name(self):
		return self._name
	
	@property
	def hp(self):
		return self._hp

	@hp.setter
	def hp(self, hp):
		self._hp = hp if hp >= 0 else 0

	@property
	def alive(self):
		return self._hp > 0

	@abstractmethod
	def attack(self, other):
		"""
		attack
		:param other: the object be attacked
		"""
		pass


class Ultraman(Fighter):
	"""
	Ultraman
	"""
	__slots__ = ('_name', '_hp', '_mp')

	def __init__(self, name, hp, mp):
		"""
		init method
		:param name:NAME
		:param hp:LIVE
		:param mp: MP
		"""

		super().__init__(name, hp)
		self._mp = mp

	def attack(self, other):
		other._hp -= randint(15, 25)

	def huge_attack(self, other):
		"""
		take off 50% or 3/4 of other's live
		:param other: the object be attacked
		:return : use successfully return True
		"""
		if self._mp >= 50:
			self._mp -= 50
			injury = other.hp * 3 // 4
			injury = injury if injury >= 50 else 50
			other.hp -= injury
			return True
		else:
			self.attack(other)
			return False

	def magic_attack(self, others):
		"""
		magic attack
		:param others: the objects be attacked
		:return: use sucessfully return True
		"""
		if self._mp >= 20:
			self._mp -= 20
			for temp in others:
				if temp.alive:
					temp.hp -= randint(10, 15)
			return True
		else:
			return False

	def resume(self):
		"""
		resume mp
		"""
		incr_point = randint(1, 10)
		self._mp += incr_point
		return incr_point

	def __str__(self):
		return '~~~%sUltraman~~~\n' % self._name + \
		    'hp: %d\n' % self._hp + \
		    'mp: %d\n' % self._mp

class Monster(Fighter):
	"""
	Monster
	"""

	__slots__ = ('_name', '_hp')

	def attack(self, other):
		other.hp -= randint(10, 20)

	def __str__(self):
		return '~~~%sMonster~~~\n' % self._name + \
		'hp: %d\n' % self._hp

def is_any_alive(monsters):
	"""
	judging if any monster alive
	"""
	for monster in monsters:
		if monster.alive > 0:
			return True
	return False

def select_alive_one(monsters):
	"""
	select an alive monster
	"""
	monsters_len = len(monsters)
	while True:
		index = randrange(monsters_len)
		monster = monsters[index]
		if monster.alive > 0:
			return monster


def display_info(ultraman, monsters):
	"""
	display the information of ultraman and monsters
	"""
	print(ultraman)
	for monster in monsters:
		print(monster, end='')
def main():
	superman = Ultraman('James', 1000, 120)
	monster_1 = Monster('Tom', 250)
	monster_2 = Monster('Jack', 500)
	monster_3 = Monster('Linsa', 750)
	monster_all = [monster_1, monster_2, monster_3]
	fight_round = 1
	while superman.alive and is_any_alive(monster_all):
		print('======the %d round======' % fight_round)
		monster_select = select_alive_one(monster_all)
		skill = randint(1, 10)
		if skill <= 6: # 60% using normal attack
			print('{} attacks {} using normal attack.'.format(superman.name, monster_select.name))
			superman.attack(monster_select)
			print('{} is resuming mp of {}'.format(superman.name, superman.resume()))
		elif skill <= 9: # 30% using magic attack
			if superman.magic_attack(monster_all):
				print('{} attacks {} using magic attack'.format(superman.name, monster_select.name))
			else:
				print('{} using magic attack failure'.format(superman.name))
		else: # 10% using huge attack
			if superman.huge_attack(monster_select):
				print('{} attacks {} using huge attack'.format(superman.name, monster_select.name))
			else:
				print('{} attcks {} using normal attack'.format(superman.name, monster_select.name))
				superman.attack(monster_select)
				print('{} is resuming mp of {}'.format(superman.name, superman.resume()))
		if monster_select.alive > 0: # if the select monster do not be killed, attack ultraman
			print('{} is attack {}'.format(monster_select.name, superman.name))
			monster_select.attack(superman)

		display_info(superman, monster_all) # display information every round
		fight_round += 1
	print('\n====fighting end!=======\n')
	if superman.alive > 0:
		print('{} win'.format(superman.name))
	else:
		print('{} win'.format(monster_select.name))

if __name__ == '__main__':
	main()