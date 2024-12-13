#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# randylampa/AoC2024
# Advent of Code 2024 - 1
# @link https://adventofcode.com/2024/day/1

import sys
import os
# ~ import re
cur_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.dirname(cur_dir))
import utils

YEAR = 2024
DAY = 1
ISSUE = '01'


def parse_input(fl: str) -> tuple:
	"""Returns tuple of lists of ints
	([int,...], [int,...])
	"""
	listL = []
	listR = []
	lines = utils.read_file_into_lines(fl)
	for line in lines:
		nL, nR = line.strip().split('   ')
		listL.append(int(nL))
		listR.append(int(nR))
	return (listL, listR)


def solve_part_1(demo: int = 0) -> str:
	"""SOLVE PART 1
	"""
	fn = utils.get_input_file(demo, DAY, YEAR)
	print({"Using input file": fn})
	fl = cur_dir + '/' + fn
	# ~ print(fl)
	"""Do something here for PART 1 >>>"""

	listL, listR = parse_input(fl)
	# ~ print(listL)
	# ~ print(listR)
	listL.sort()
	listR.sort()
	# ~ print(listL)
	# ~ print(listR)

	dists = []
	for i in range(len(listL)):
		dists.append(abs(listL[i] - listR[i]))
	print(dists)

	answer = sum(dists)

	"""<<< Do something here for PART 1"""
	utils.print_answer(1, demo, answer)
	return answer


def solve_part_2(demo: int = 0) -> str:
	"""SOLVE PART 2
	"""
	fn = utils.get_input_file(demo, DAY, YEAR)
	print({"Using input file": fn})
	fl = cur_dir + '/' + fn
	# ~ print(fl)
	"""Do something here for PART 2 >>>"""

	listL, listR = parse_input(fl)
	print('listL =', listL)
	print('listR =', listR)

	scores = []
	for nL in listL:
		scores.append(nL * listR.count(nL))
	print(scores)

	answer = sum(scores)

	"""<<< Do something here for PART 2"""
	utils.print_answer(2, demo, answer)
	return answer


def main():

	# ~ solve_part_1(0)

	solve_part_2(0)

	pass


if __name__ == '__main__':
	sys.exit(main())
