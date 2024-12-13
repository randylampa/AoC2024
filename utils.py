#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# randylampa/AoC2024
#

import sys
import re


def get_demo_sufix(demo: int) -> str:
	"""Returns filename suffix for demo

	'demoN-' or ''
	"""
	if demo > 0:
		return 'demo{}-'.format(str(demo))
	return ''


def get_input_file(demo: int, day: int, year: int) -> str:
	"""Returns filename for INput data
	"""
	return 'data-{}{}-{}'.format(
		get_demo_sufix(demo),
		str(year),
		str(day).rjust(2, '0'),
	)


def get_output_file(demo: int, day: int, year: int) -> str:
	"""Returns filename for OUTput data
	"""
	return 'outdata-{}{}-{}'.format(
		get_demo_sufix(demo),
		str(year),
		str(day).rjust(2, '0'),
	)


def read_file_into_lines(name: str, mode: str = 'r') -> list:
	"""Reads all lines into list
	"""
	f = open(name, 'r')
	lines = f.readlines()
	f.close()
	return lines


def read_file_into_list(name: str, mapfnc=lambda x: x.strip()) -> list:
	"""Reads all lines into list and map mapfnc on each.
	"""
	return [*map(mapfnc, read_file_into_lines(name))]


def read_file_into_list_bin(name: str, mapfnc=None) -> list:
	"""Reads all lines into list and map mapfnc on each.
	"""
	lines = read_file_into_lines(name, 'rb')
	if mapfnc is not None:
		return [*map(mapfnc, lines)]
	else:
		return lines


def read_file_into_list_of_ints(name: str) -> list:
	"""Reads all lines into list and map int(x.strip()) on each.
	"""
	return read_file_into_list(
		name,
		lambda x: int(x.strip()),
	)


def read_file_into_lists_of_ints(name: str, sep: str = ',') -> list:
	"""Read all lines into list of lists (sep=,)
	"""
	return read_file_into_list(
		name,
		lambda x: [*map(int, x.strip().split(sep))],
	)


def read_file_into_dict(
	name: str,
	kvpattrn: str = '(?P<k>.*):\\s*(?P<v>.*)',
	vmap=int,
) -> dict:
	"""Reads all lines into dict and maps vmap on each value
	"""
	outdict = {}
	for line in read_file_into_lines(name):
		mm = re.search(kvpattrn, line)
		k = mm.groupdict()['k']
		v = mm.groupdict()['v']
		outdict[k] = vmap(v)
	return outdict


def dump_list_of(xlist: list):
	for x in xlist:
		print(x)


def print_answer(part: int, demo: bool, answer) -> None:
	print("Answer_{} = {}{}".format(part, answer, ' (demo)' if demo else ''))


def test_answers(expect: dict, runner) -> bool:
	"""Test expected answers for different inputs
	expect {demoN: answer, ..}
	runner solve_part_N
	"""
	allmet = True
	for itm in expect.items():
		ret = runner(itm[0])
		if ret == itm[1]:
			print('EXPECTATION MET')
			allmet &= True
		else:
			print('EXPECTATION UNMET!')
			allmet &= False
	return allmet


def main(args):
	return 0


if __name__ == '__main__':
	sys.exit(main(sys.argv))
