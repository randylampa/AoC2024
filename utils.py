#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# randylampa/AoC2024
#

import sys
import re


def get_input_file(demo: int, day: int, year: int) -> str:
	syear = str(year)
	sday = str(day).rjust(2, '0')
	sdemo = 'demo{}-'.format(str(demo) if demo > 0 else '')
	f = 'data-{}{}-{}'.format(sdemo if demo > 0 else '', syear, sday)
	return f


def get_output_file(demo: int, day: int, year: int) -> str:
	syear = str(year)
	sday = str(day).rjust(2, '0')
	sdemo = 'demo{}-'.format(str(demo) if demo > 0 else '')
	f = 'outdata-{}{}-{}'.format(sdemo if demo > 0 else '', syear, sday)
	return f


def read_file_into_lines(name: str = 'input', mode: str = 'r') -> list:
	"""
	Reads all lines into list
	"""
	f = open(name, 'r')
	lines = f.readlines()
	f.close()
	return lines


def read_file_into_list(name: str = 'input', mapfnc=lambda x: x.strip()) -> list:
	"""
	Reads all lines into list and map mapfnc on each.
	"""
	return [*map(mapfnc, read_file_into_lines(name))]


def read_file_into_list_bin(name: str = 'input', mapfnc=None) -> list:
	"""
	Reads all lines into list and map mapfnc on each.
	"""
	lines = read_file_into_lines(name, 'rb')
	if mapfnc is not None:
		return [*map(mapfnc, lines)]
	else:
		return lines


def read_file_into_list_of_ints(name: str = 'input') -> list:
	"""
	Reads all lines into list and map int(x.strip()) on each.
	"""
	return read_file_into_list(name, lambda x: int(x.strip()))


def read_file_into_lists_of_ints(name: str = 'input') -> list:
	"""
	Read all lines into list of lists (sep=,)
	"""
	return read_file_into_list(name, lambda x: [*map(int, x.strip().split(','))])


def read_file_into_dict(name: str = 'input', kvpattrn: str = '(?P<k>.*):\\s*(?P<v>.*)', vmap=int) -> dict:
	"""
	Reads all lines into dict and maps vmap on each value
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


def print_answer(part: int, demo, answer) -> None:
	print("Answer_{} = {}{}".format(part, answer, ' (demo)' if demo else ''))


def main(args):
	return 0


if __name__ == '__main__':
	sys.exit(main(sys.argv))
