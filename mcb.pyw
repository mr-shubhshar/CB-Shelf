
"""
	mcb.pyw - Saves content from/on clipboard(CB) to a shelf file "mcbdata".
	USAGE:	python mcb.pyw save <keyword>: saves data from CB to keyword.
			python mcb.pyw <keyword>: loads keyword's data to CB.
			python mcb.pyw list: loads all keywords' list to CB.
			python mcb.pyw delete all: deletes full database from shelf.
			python mcb.pyw delete <keyword>: deletes keyword's data from shelf database.
"""

#!usr/bin/python

from sys import *
import pyperclip, shelve

mcbshelf = shelve.open('mcbdata')

scr = argv[0]

if (len(argv) == 3) and (argv[1].lower() == 'save'):
	mcbshelf[argv[2]] = pyperclip.paste()
	print 'saved to database'
elif (len(argv) == 3) and (argv[1].lower() == 'delete'):
	if argv[2] == 'all':
		mcbshelf.clear()
		print 'all data has been cleared!'
	elif argv[2] in mcbshelf:
		del mcbshelf[argv[2]]
		print 'requested key has been deleted!'
	else:
		exit('No such key is there in the database/check your arguments')
elif (len(argv) == 2) and (argv[1] == 'list'):
	pyperclip.copy(str(list(mcbshelf.keys())))
	print 'all keywords have been copied to clipboard'
elif argv[1] in mcbshelf:
	pyperclip.copy(str(mcbshelf[argv[1]]))
	print 'Data for query has been copied!'
else:
	exit('No such keyword has been saved yet! OR check your command again')
