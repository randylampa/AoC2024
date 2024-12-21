#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# randylampa/AoC2024
# Advent of Code 2024 - 14
# @link https://adventofcode.com/2024/day/14

import sys
import os
import re
import time
cur_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.dirname(cur_dir))
import utils
from utils import dump_list_of

YEAR = 2024
DAY = 14
ISSUE = '14'


def get_file(demo: int = 0) -> tuple:
	"""Returns (filePath, fileName)
	"""
	fn = utils.get_input_file(demo, DAY, YEAR)
	print({"Using input file": fn})
	fl = cur_dir + '/' + fn
	# ~ print(fl)
	return (fl, fn)


def parse_line(line: str) -> dict:
	robot = {}
	for m in re.finditer('(?P<var>\\w)=(?P<x>-?\\d+),(?P<y>-?\\d+)', line):
		gd = m.groupdict()
		# ~ print(gd)
		robot[gd['var']] = (int(gd['x']), int(gd['y']))
	return robot


def parse_input(fl: str):
	robots = utils.read_file_into_list(fl, parse_line)
	# ~ dump_list_of(robots)
	return robots


def move_robots(robots: list, xmax: int, ymax: int):
	for robot in robots:
		p = robot['p']
		v = robot['v']
		robot['p'] = ((p[0] + v[0]) % xmax, (p[1] + v[1]) % ymax)
	pass


def init_playfield(x: int, y: int):
	"""make new field of provided dimensions
	"""
	pf = []
	for yi in range(y):
		pf.append([0] * x)
	return pf


def clean_playfield(playfield: list):
	"""cleanup existing field
	"""
	xn = range(len(playfield[0]))
	for y in range(len(playfield)):
		for x in xn:
			playfield[y][x] = 0
	pass


def place_robots(robots: list, playfield: list):
	for robot in robots:
		pos = robot['p']
		playfield[pos[1]][pos[0]] += 1
	pass


def visualize(playfield: list, output: bool = True):
	field = ''
	for line in playfield:
		field += "\n" if field != '' else ''
		field += ' '.join(map(lambda x: str(x) if x > 0 else '.', line))

	if output:
		print('=' * 60) if output else None
		print(field)
		print('=' * 60) if output else None


def solve_part_1(demo: int = 0) -> str:
	"""SOLVE PART 1
	"""
	fl, fn = get_file(demo)
	"""Do something here for PART 1 >>>"""

	animate = demo > 0
	sec = 100

	if demo == 0:
		xmax = 101
		ymax = 103
	else:
		xmax = 11
		ymax = 7

	robots = parse_input(fl)
	# ~ dump_list_of(robots)

	playfield = init_playfield(xmax, ymax)
	# ~ visualize(playfield)
	place_robots(robots, playfield)
	visualize(playfield) if animate else None
	# ~ clean_playfield(playfield)
	# ~ visualize(playfield)
	# ~ exit()

	for sec in range(sec):
		time.sleep(0.040) if animate else None
		move_robots(robots, xmax, ymax)
		clean_playfield(playfield)
		place_robots(robots, playfield)
		visualize(playfield) if animate else None

	# ~ xmid = xmax // 2 + 1
	# ~ ymid = ymax // 2 + 1

	answer = None

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
		1: 12,
		# ~ 2: None,
		# ~ 0: None,
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
