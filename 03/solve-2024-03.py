#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# randylampa/AoC2024
# Advent of Code 2024 - 3
# @link https://adventofcode.com/2024/day/3

import sys
import os
import re
cur_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.dirname(cur_dir))
import utils
from utils import dump_list_of

YEAR = 2024
DAY = 3
ISSUE = '03'


def get_file(demo: int = 0) -> tuple:
	"""Returns (filePath, fileName)
	"""
	fn = utils.get_input_file(demo, DAY, YEAR)
	print({"Using input file": fn})
	fl = cur_dir + '/' + fn
	# ~ print(fl)
	return (fl, fn)


def parse_input(fl: str) -> str:
	f = open(fl, 'r')
	content = f.read()
	f.close()
	return content


def solve_part_1(demo: int = 0) -> str:
	"""SOLVE PART 1
	"""
	fl, fn = get_file(demo)
	"""Do something here for PART 1 >>>"""

	content = parse_input(fl)

	instrs = re.findall('(mul)\\((\\d+),(\\d+)\\)', content)
	dump_list_of(instrs)

	nums = []
	for ins in instrs:
		nums.append(int(ins[1]) * int(ins[2]))
	print(nums)

	answer = sum(nums)

	"""<<< Do something here for PART 1"""
	utils.print_answer(1, demo, answer)
	return answer


def solve_part_2(demo: int = 0) -> str:
	"""SOLVE PART 2
	"""
	fl, fn = get_file(demo)
	"""Do something here for PART 2 >>>"""

	content = parse_input(fl)

	instrs = re.findall("(?:(do(?:n't)?)\\(\\))|(?:(mul)\\((\\d+),(\\d+)\\))", content)
	dump_list_of(instrs)

	nums = []
	do = True
	for ins in instrs:
		inm = ins[0] if ins[0] else ins[1]
		# ~ print(inm)
		if False:
			pass
		elif inm == "do":
			do = True
		elif inm == "don't":
			do = False
		elif do and inm == "mul":
			o1 = int(ins[2])
			o2 = int(ins[3])
			# ~ print(inm, o1, o2)
			nums.append(o1 * o2)
	print(nums)

	answer = sum(nums)

	"""<<< Do something here for PART 2"""
	utils.print_answer(2, demo, answer)
	return answer


def main():

	# ~ solve_part_1(0)
	print(utils.test_answers({
		# ~ 1: 161,
		# ~ 0: 173529487,
	}, solve_part_1))

	# ~ solve_part_2(0)  # 2 for demo!
	print(utils.test_answers({
		# ~ 2: 48,
		0: 99532691,
	}, solve_part_2))


if __name__ == '__main__':
	sys.exit(main())
