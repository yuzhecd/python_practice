#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-07-11 17:15:56
# @Author  : yuzhecd (yuzhecd@163.com)
# @Link    : --------
# @Version : $Id$

import random

class Card(object):
	"""
	single card
	"""

	def __init__(self, suite, face):
		self._suite = suite
		self._face = face

	@property
	def face(self):
		return self._face
	
	@property
	def suite(self):
		return self._suite
	
	def __str__(self):
		if self._face == 1:
			face_str = 'A'
		elif self._face == 11:
			face_str = 'J'
		elif self._face == 12:
			face_str = 'Q'
		elif self._face == 13:
			face_str = 'K'
		else:
			face_str = str(self._face)
		return '%s%s' % (self._suite, face_str)

	def __repr__(self):
		return self.__str__()

class Poker(object):
	"""
	a pair of cards
	"""

	def __init__(self):
		self._cards = [Card(suite, face)
						for suite in 'abcd'
						for face in range(1, 14)]
		self._current = 0

	@property
	def cards(self):
		return self._cards
	
	def shuffle(self):
		"""
		random the cards
		"""
		self._current = 0
		random.shuffle(self._cards)

	@property
	def next(self):
		"""
		deal
		"""
		card = self._cards[self._current]
		self._current += 1
		return card

	@property
	def has_next(self):
		"""
		judging if have a card
		"""
		return self._current < len(self._cards)

class Player(object):
	"""
	Player
	"""

	def __init__(self, name):
		self._name = name
		self._cards_on_hand = []


	@property
	def name(self):
		return self._name
	
	@property
	def cards_on_hand(self):
		return self._cards_on_hand
	
	def get(self, card):
		"""
		get the card
		"""

		self._cards_on_hand.append(card)

	def arrange(self, card_key):
		"""
		arranging the card
		"""
		self._cards_on_hand.sort(key=card_key)

def get_key(card):
		return (card.suite, card.face)

def main():
	p = Poker()
	p.shuffle()
	players = [Player('James'), Player('Tom'), Player('Tommy'), Player('Jack')]
	for _ in range(13):
		for player in players:
			player.get(p.next)
	for player in players:
		print(player.name + ':', end=' ')
		#player.arrange(get_key(p))
		print(player.cards_on_hand)


if __name__ == '__main__':
	main()