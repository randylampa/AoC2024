#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# randylampa/AoC2024
# Advent of Code 2024 - 2
# @link https://adventofcode.com/2024/day/2

import sys
import os
# ~ import re
cur_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.dirname(cur_dir))
import utils

YEAR = 2024
DAY = 2
ISSUE = '02'


def solve_part_1(demo: int = 0) -> str:
	"""SOLVE PART 1
	"""
	fn = utils.get_input_file(demo, DAY, YEAR)
	print({"Using input file": fn})
	fl = cur_dir + '/' + fn
	# ~ print(fl)
	"""Do something here for PART 1 >>>"""

	answer = None

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

	answer = None

	"""<<< Do something here for PART 2"""
	utils.print_answer(2, demo, answer)
	return answer


def main():

	solve_part_1(1)

	solve_part_2(1)

	pass


if __name__ == '__main__':
	sys.exit(main())
