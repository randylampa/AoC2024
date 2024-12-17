#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# randylampa/AoC2024
# Advent of Code 2024 - 15
# @link https://adventofcode.com/2024/day/15

import sys
import os
# ~ import re
cur_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.dirname(cur_dir))
import utils
from utils import dump_list_of

YEAR = 2024
DAY = 15
ISSUE = '15'


def get_file(demo: int = 0) -> tuple:
	"""Returns (filePath, fileName)
	"""
	fn = utils.get_input_file(demo, DAY, YEAR)
	print({"Using input file": fn})
	fl = cur_dir + '/' + fn
	# ~ print(fl)
	return (fl, fn)


def parse_input(fl: str):
	return None


def solve_part_1(demo: int = 0) -> str:
	"""SOLVE PART 1
	"""
	fl, fn = get_file(demo)
	"""Do something here for PART 1 >>>"""

	parse_input(fl)

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
		1: None,
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
	print(utils.test_answers(expect2, solve_part_2))


if __name__ == '__main__':
	sys.exit(main())
