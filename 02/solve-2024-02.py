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
from utils import dump_list_of

YEAR = 2024
DAY = 2
ISSUE = '02'


def get_file(demo: int = 0) -> tuple:
	"""Returns (filePath, fileName)
	"""
	fn = utils.get_input_file(demo, DAY, YEAR)
	print({"Using input file": fn})
	fl = cur_dir + '/' + fn
	# ~ print(fl)
	return (fl, fn)


def parse_input(fl: str) -> list:
	return utils.read_file_into_lists_of_ints(fl, ' ')


def count_distances(inlist: list) -> list:
	"""Count numerical distances between items of list.
	Returning list is one item shorter than provided one.
	"""
	dists = []
	for i in range(len(inlist) - 1):
		dists.append(inlist[i + 1] - inlist[i])
	return dists


def solve_part_1(demo: int = 0) -> str:
	"""SOLVE PART 1
	"""
	fl, fn = get_file(demo)
	"""Do something here for PART 1 >>>"""

	reports = parse_input(fl)
	# ~ dump_list_of(reports)

	nSafe = 0
	for report in reports:
		dists = count_distances(report)
		# ~ print('dists:', dists)

		dd = (min(dists), max(dists))
		# ~ print({'dd': dd, 'madd': max(dd), 'midd': min(dd)})
		isIncr = min(dd) > 0		# exclusively increasing
		isDecr = max(dd) < 0		# exclusively decreasing
		# ~ print({'isIncr': isIncr, 'isDecr': isDecr})
		add = (abs(dd[0]), abs(dd[1]))
		# ~ print({'add': add, 'maadd': max(add), 'miadd': min(add)})

		if (isIncr or isDecr) and min(add) >= 1 and max(add) <= 3:
			# ~ print('SAFE', report)
			nSafe += 1
		else:
			# ~ print('UNSAFE', report)
			pass
		# ~ print()

	answer = nSafe

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

	solve_part_1(0)

	# ~ solve_part_2(1)

	pass


if __name__ == '__main__':
	sys.exit(main())
