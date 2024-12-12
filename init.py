#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# randylampa/AoC2024
#

import sys
import getopt
import os

YEAR = 2024


def main():
	try:
		options, arguments = getopt.getopt(sys.argv[1:], "y:d:p:", ["year =", "day =", "part ="])
	except:
		print("Error parsing args")
		return -1
	print(options, arguments)

	year = YEAR
	day = None
	part = 1

	for opt, arg in options:
		if opt in ('-y', '--year'):
			year = arg
		elif opt in ('-d', '--day'):
			day = int(arg)
		elif opt in ('-p', '--part'):
			part = int(arg)

	if len(arguments) > 0:
		day = int(arguments[0])

	if day is None:
		print('Day not set!')
		return -2

	issue = str(day).rjust(2, '0')

	url = "https://adventofcode.com/{}/day/{}".format(year, day)
	url_input = "{}/input".format(url)
	url_answer = "{}/answer".format(url)

	trtable = {
		'$YEAR': year,
		'$DAY': day,
		'$ISSUE': issue,
		'$URL': url,
		'$URL_INPUT': url_input,
		'$URL_ANSWER': url_answer,
	}

	def trans(instr: str) -> str:
		for k in trtable.keys():
			instr = instr.replace(k, str(trtable[k]))
		return instr

	srcDir = '_tpl'
	tgtDir = issue

	try:
		os.mkdir(tgtDir)
	except FileExistsError:
		print("Dir '{}' already exists".format(tgtDir))

	fhifo = open("{}/info-{}-{}.txt".format(tgtDir, year, issue), 'w')
	for i in trtable.items():
		l = "{}\t{}".format(i[0], i[1])
		# ~ print(l)
		fhifo.write(l + "\n")
	fhifo.close()

	'''
	get all files from dir `_tpl`. copy them into dir `$ISSUE`
	rename & modify according to `trtable`
	'''
	files = os.listdir(srcDir)
	for srcFl in files:
		tgtFl = trans(srcFl)
		# ~ print(srcFl, tgtFl)
		srcPath = srcDir + '/' + srcFl
		tgtPath = tgtDir + '/' + tgtFl
		fhin = open(srcPath)
		content = trans(fhin.read())
		fhin.close()
		fhout = open(tgtPath, 'w')
		fhout.write(content)
		fhout.close()
		if tgtFl.startswith("solve"):
			os.chmod(tgtPath, 0o755)

	print("Inspect result & commit:")
	print(" git add {}/".format(issue))
	print(' git commit -m "day {} - init"'.format(issue))
	print(' git push')

	return 0


if __name__ == '__main__':
	sys.exit(main())
