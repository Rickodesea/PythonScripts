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

#CenterText.py
#This script converts any binary data into a 'C array'.  This array can be accessed normally in 'C code'.

import os
import argparse as ap
import sys

def Read(Path):
	if type(Path) == file:
		return Path.read()
	elif type(Path) == str:
		with open(Path, 'r') as io:
			return io.read()
		print 'CenterText.py::Error: Failed to open %s.' %(Path)
	else:
		print 'CenterText.py::System Error:Read(Path/File).'
	exit()

def Write(Path, Text):
	if type(Path) == file:
		Path.write(Text)
		if Path == sys.stdout: Path.write('\n')
	elif type(Path) == str:
		with open(Path, 'w') as io:
			io.write(Text)
		print 'CenterText.py::Error: Failed to open %s.' %(Path)
	else:
		print 'CenterText.py::System Error:Write(Path/File).'
	exit()

def CreateStringFromStringList(StringList, Separator=''):
	string = ''
	for i, item in enumerate(StringList):
		string += item
		if Separator and i < len(StringList) - 1:
			string += Separator
	return string

def GetMaxLengthFromStringList(StringList):
	maxlength = 0
	for string in StringList:
		length = len(string)
		if length > maxlength: maxlength = length
	return maxlength

def GetCenterOffsetForString(String, MaxLength):
	length = len(String)
	return int(round((MaxLength / 2.0 - length / 2.0), 0))

def CreateCenteredText(Text):
	centeredtextList = []
	lines = Text.splitlines()
	maxlength = GetMaxLengthFromStringList(lines)
	for line in lines:
		offset = GetCenterOffsetForString(line, maxlength)
		string = (' ' * offset) + line
		centeredtextList.append(string)
	return CreateStringFromStringList(centeredtextList, '\n')

def RunConsole():
	arg = ap.ArgumentParser(description='Centers a text.')
	arg.add_argument('-i', '--input', default='input.txt', help='File path to read text from. Default\'input.txt\'', type=ap.FileType('r'))
	arg.add_argument('-o', '--output', default=sys.stdout, help='File path to write text to. Default:console', type=ap.FileType('w'))
	cmd = arg.parse_args()
	text = Read(cmd.input)
	centeredtext = CreateCenteredText(text)
	Write(cmd.output, centeredtext)

if __name__ == '__main__':
	RunConsole()