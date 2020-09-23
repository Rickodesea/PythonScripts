"""
Copyright (c) <'2020'> <'Alrick Grandison'>

This software is provided 'as-is', without any express or implied
warranty. In no event will the authors be held liable for any damages
arising from the use of this software.

Permission is granted to anyone to use this software for any purpose,
including commercial applications, and to alter it and redistribute it
freely, subject to the following restrictions:

1. The origin of this software must not be misrepresented; you must not
   claim that you wrote the original software. If you use this software
   in a product, an acknowledgment in the product documentation would be
   appreciated but is not required.
2. Altered source versions must be plainly marked as such, and must not be
   misrepresented as being the original software.
3. This notice may not be removed or altered from any source distribution.
"""

#TextToCString.py
#This script converts any text into a 'C string literal'.  This string can be assigned to any 'C code variable'.

import os
from os import path as osp
import argparse as ap
import sys

def Read(Path):
	if type(Path) == file:
		return Path.read()
	elif type(Path) == str:
		with open(Path, 'r') as io:
			return io.read()
		print 'TextToCString.py::Error: Failed to open %s.' %(Path)
	else:
		print 'TextToCString.py::System Error:Read(Path/File).'
	exit()

def Write(Text, Path):
	if type(Path) == file:
		Path.write(Text)
		if Path == sys.stdout: Path.write('\n')
	elif type(Path) == str:
		with open(Path, 'w') as io:
			io.write(Text)
		print 'TextToCString.py::Error: Failed to open %s.' %(Path)
	else:
		print 'TextToCString.py::System Error:Write(Path/File).'
	exit()

def CreateStringFromStringList(StringList, Separator=''):
	string = ''
	for i, item in enumerate(StringList):
		string += item
		if Separator and i < len(StringList) - 1:
			string += Separator
	return string

def ApplyFormat(Text, Bool):
	if Bool:
		return Text.replace('%', '%%')
	return Text

def ApplyQuote(Text, Bool):
	if Bool:
		return Text.replace('"', '\\"')
	return Text

def ApplyEscape(Text, Bool):
	if Bool:
		return Text.replace('\\', '\\\\')
	return Text

def ApplySingle(Text, Bool):
	lines = Text.splitlines()
	newList = []
	if Bool:
		for line in lines:
			newList.append(line + '\\n')
		newList.insert(0, '"')
		newList.append('"')
	else:
		for line in lines:
			newList.append('"' + line + '\\n' + '"')
	return CreateStringFromStringList(newList, '\n')

def str2bool(v):
    if isinstance(v, bool):
       return v
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise ap.ArgumentTypeError('Boolean value expected.')

def RunConsole():
	arg = ap.ArgumentParser(description='Converts text to C string literal.')
	arg.add_argument('-i', '--input', default='input.txt', help='File path to read text from. Default:\'input.txt\'', type=ap.FileType('r'))
	arg.add_argument('-o', '--output', default=sys.stdout, help='File path to write text to. Default:console', type=ap.FileType('w'))
	arg.add_argument('-s', '--single', action='store_true', help='Store text in a single literal. Default:False.')
	arg.add_argument('-f', '--format', default=False, choices=[True, False], help='Protect embedded format \'%%\'. Default:False', type=str2bool)
	arg.add_argument('-q', '--quote', default=True, choices=[True, False], help='Protect embedded quote \'\"\'. Default:True', type=str2bool)
	arg.add_argument('-e', '--escape', default=False, choices=[True, False], help='Protect embedded escape \'\\\'. Default:False', type=str2bool)
	cmd = arg.parse_args()
	text = Read(cmd.input)
	text = ApplyFormat(text, cmd.format)
	text = ApplyEscape(text, cmd.escape) #Must be called before Quote to avoid corruption.
	text = ApplyQuote(text, cmd.quote)
	text = ApplySingle(text, cmd.single) #This adds the wrapper quotes, so must always be called last.
	Write(text, cmd.output)

if __name__ == '__main__':
	RunConsole()