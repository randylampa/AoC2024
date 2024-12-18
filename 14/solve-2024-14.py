#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# randylampa/AoC2024
# Advent of Code 2024 - 14
# @link https://adventofcode.com/2024/day/14

import sys
import os
import re
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
	for m in re.finditer('(?P<var>\w)=(?P<x>-?\d+),(?P<y>-?\d+)', line):
		gd = m.groupdict()
		# ~ print(gd)
		robot[gd['var']] = (int(gd['x']), int(gd['y']))
	return robot


def parse_input(fl: str):
	robots = utils.read_file_into_list(fl, parse_line)
	# ~ dump_list_of(robots)
	return robots


playfield = None


def init_playfield(playfield: list, x: int = None, y: int = None):
	"""if x,y not provided, only cleanup existing field,
	else make new of provided dimensions
	"""
	pf = []
	if x is not None and y is not None:
		for yi in range(y):
			pf.append(['.'] * x)
	if x is None and y is None:
		pass
	return pf


def visualize(playfield: list, output: bool = True):
	field = ''
	for line in playfield:
		field += "\n" if field != '' else ''
		field += ' '.join(line)

	if output:
		print('='*60) if output else None
		print(field)
		print('='*60) if output else None


def solve_part_1(demo: int = 0) -> str:
	"""SOLVE PART 1
	"""
	fl, fn = get_file(demo)
	"""Do something here for PART 1 >>>"""

	robots = parse_input(fl)
	# ~ dump_list_of(robots)

	playfield = []
	playfield = init_playfield(playfield, 11, 7)
	visualize(playfield)

	for sec in range(100):


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

	solve_part_1(1)
	expect1 = {
		1: 12,
		# ~ 2: None,
		# ~ 0: None,
	}
	# ~ print(utils.test_answers(expect1, solve_part_1))

	# ~ solve_part_2(1)
	expect2 = {
		1: None,
		# ~ 2: None,
		# ~ 0: None,
	}
	# ~ print(utils.test_answers(expect2, solve_part_2))


if __name__ == '__main__':
	sys.exit(main())
