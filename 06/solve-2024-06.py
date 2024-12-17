#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# randylampa/AoC2024
# Advent of Code 2024 - 6
# @link https://adventofcode.com/2024/day/6

import sys
import os
# ~ import re
import time
cur_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.dirname(cur_dir))
import utils
from utils import dump_list_of

YEAR = 2024
DAY = 6
ISSUE = '06'


WALL = '#'
VISITED = 'X'
agents = '^>v<'
playfield = []
agent_pos = (0, 0)


def get_file(demo: int = 0) -> tuple:
	"""Returns (filePath, fileName)
	"""
	fn = utils.get_input_file(demo, DAY, YEAR)
	print({"Using input file": fn})
	fl = cur_dir + '/' + fn
	# ~ print(fl)
	return (fl, fn)


def parse_input(fl: str) -> tuple:
	"""returns (playfield, agent_pos, ag)
	"""
	playfield = utils.read_file_into_list(fl, lambda x: [*x.strip()])
	# ~ dump_list_of(playfield)
	x = None
	y = 0
	for line in playfield:
		for ag in agents:
			if ag not in line:
				continue
			x = line.index(ag)
			agent_pos = (x, y)
			break
		if x is not None:
			break
		y += 1
	agent_pos = (x, y)
	print({'agent_pos': agent_pos})
	return (playfield, agent_pos, ag)


def visualize(playfield: list, agent_pos: tuple, output: bool = True):
	field = ''
	for line in playfield:
		field += "\n" if field != '' else ''
		field += ' '.join(line)

	if output:
		print('='*60) if output else None
		print(field)
		print({'agent_pos': agent_pos})
		print('='*60) if output else None
	# ~ print({'agent_pos': agent_pos})


def count_visited(playfield: list) -> int:
	nVis = 0
	for line in playfield:
		nVis += line.count(VISITED)
	return nVis


def make_step(playfield: list, agent_pos: tuple) -> tuple:
	"""uses global playfield & agent_pos
	"""
	apx = agent_pos[0]
	apy = agent_pos[1]
	ag = playfield[apy][apx]
	napx = apx
	napy = apy
	if ag == '^':
		napy -= 1
	elif ag == 'v':
		napy += 1
	elif ag == '<':
		napx -= 1
	elif ag == '>':
		napx += 1
	else:
		raise ValueError('Unknown agent position!')

	if napy < 0 or napx < 0 or napy >= len(playfield) or napx >= len(playfield[0]):
		playfield[apy][apx] = VISITED
		raise IndexError('Stepped out of bounds')

	dest = playfield[napy][napx]
	if dest != WALL:
		playfield[apy][apx] = VISITED
		playfield[napy][napx] = ag
		agent_pos = (napx, napy)
	else:
		nagi = agents.find(ag) + 1
		ag = agents[nagi if nagi < len(agents) else 0]
		playfield[apy][apx] = ag

	return (playfield, agent_pos, ag)


def solve_part_1(demo: int = 0) -> str:
	"""SOLVE PART 1
	"""
	fl, fn = get_file(demo)
	"""Do something here for PART 1 >>>"""

	animate = demo > 0

	playfield, agent_pos, ag = parse_input(fl)
	visualize(playfield, agent_pos, animate)

	while True:
		time.sleep(0.075) if animate else None
		try:
			playfield, agent_pos, ag = make_step(playfield, agent_pos)
			visualize(playfield, agent_pos, animate)
		except (ValueError, IndexError) as err:
			visualize(playfield, agent_pos, animate)
			print("Oops!", err)
			break
		# ~ finally:
			# ~ visualize(playfield, agent_pos, animate)

	answer = count_visited(playfield)

	"""<<< Do something here for PART 1"""
	utils.print_answer(1, demo, answer)
	return answer


def solve_part_2(demo: int = 0) -> str:
	"""SOLVE PART 2
	"""
	fl, fn = get_file(demo)
	"""Do something here for PART 2 >>>"""

	parse_input(fl)

	answer = None

	"""<<< Do something here for PART 2"""
	utils.print_answer(2, demo, answer)
	return answer


def main():

	# ~ solve_part_1(1)
	expect1 = {
		1: 41,
		0: 5564, # 5595 is too high?! 'cos stepped to negative bounds
	}
	print(utils.test_answers(expect1, solve_part_1))

	# ~ solve_part_2(1)
	expect2 = {
		1: None,
		# ~ 2: None,
		# ~ 0: None,
	}
	# ~ print(utils.test_answers(expect2, solve_part_2))


if __name__ == '__main__':
	sys.exit(main())
