from typing import Optional

import numpy as np


class Die:
	def __init__(self, num_sides: int = 6):
		self.num_sides = num_sides

	def roll(self):
		return np.random.randint(1, self.num_sides + 1)

class Player:
	def __init__(self, num_dice: int = 5, num_sides: int = 6):
		self.num_dice = num_dice
		self.num_sides = num_sides
		self.dice = [Die(num_sides) for _ in range(num_dice)]
		self.dice_config = [die.roll() for die in self.dice]

	def roll_all_dice(self):
		self.dice_config = [die.roll() for die in self.dice]
		return self.dice_config

class LiarsDice:
	def __init__(self, num_players: int = 3, num_dice_per_player: int = 5, num_die_sides: int = 6):
		self.num_players = num_players
		self.num_die_sides = num_die_sides
		self.players = [Player(num_dice_per_player, num_die_sides) for _ in range(num_players)]
		self.current_player_idx = np.random.randint(1, num_players + 1)
		self.current_bid = None

	def make_bid(self, value: int, quantity: int):
		if self.current_bid and (value < 1 or value > self.num_die_sides or value <= self.current_bid[0] or quantity <= self.current_bid[1]):
			raise ValueError(f'Invalid bid {value, quantity}. Value and/or quantity must be greater than previous bid.')

		self.current_bid = (value, quantity)

	def challenge_bid(self) -> bool:
		if self.current_bid:
			count = sum(die == self.current_bid[0] for player in self.players for die in player.roll_all_dice())
			if count >= self.current_bid[1]:
				print('Challenge failed! The bid was correct.')
				return False
			else:
				print('Challenge succeeded! The bid was incorrect.')
				return True
		else:
			print('No bid to challenge')
			return False

	def step(self, action: int, bid: Optional[tuple[int, int]] = None) -> bool:
		'''
		action: 0 to make bid, 1 to challenge bid
		'''
		terminated = False
		if action == 0:
			if bid == None:
				raise ValueError('Make bid requested but bid not specified.')
			print(f'Player {self.current_player_idx}: make bid {bid}')
			self.make_bid(bid[0], bid[1])
		elif action == 1:
			print(f'Player {self.current_player_idx}: challenge previous bid')
			terminated = self.challenge_bid()
		self.current_player_idx = (self.current_player_idx + 1) % self.num_players
		return terminated

class Agent:
	def __init__(self):
		pass

	def action(self, current_bid) -> tuple[int, Optional[tuple[int, int]]]:
		return (1, None)
