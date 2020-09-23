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

#TextToCArray.py
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
		print 'BinaryToCArray.py::Error: Failed to open %s.' %(Path)
	else:
		print 'BinaryToCArray.py::System Error:Read(Path/File).'
	exit()

def Write(Path, Text):
	if type(Path) == file:
		Path.write(Text)
		if Path == sys.stdout: Path.write('\n')
	elif type(Path) == str:
		with open(Path, 'w') as io:
			io.write(Text)
		print 'BinaryToCArray.py::Error: Failed to open %s.' %(Path)
	else:
		print 'BinaryToCArray.py::System Error:Write(Path/File).'
	exit()

def CreateStringFromInteger(Integer):
	if Integer > 99: return str(Integer)
	if Integer >  9: return ' ' + str(Integer)
	return ' ' + ' ' + str(Integer)

def CreateStringFromNumber(Number, Type):
	if Type == 'hex': return "{0:#0{1}x}".format(Number, 4)
	if Type == 'HEX': return '0x{0:0{1}X}'.format(Number, 2)
	if Type == 'dec': return CreateStringFromInteger(Number)
	print 'BinaryToCArray.py::Error: invalid type %s' % Type
	exit()

def CreateArray(Binary, Type):
	array = []
	for byte in Binary:
		number = ord(byte)
		string = CreateStringFromNumber(number, Type)
		array.append(string)
	return array

def CreateStringFromArray(List, Column):
	string = ''
	icol = 0
	count = str(len(List))
	begin = 'char binary [' + count + '] = {'
	end = '};'
	string += begin + '\n\t'
	for i, item in enumerate(List):
		string += item
		if i < len(List) - 1: string += ', '
		if Column > 0:
			icol += 1
			if icol == Column:
				icol = 0
				string += '\n'
				if i < len(List) - 1: string += '\t'
	string += '\n' + end
	return string

def RunConsole():
	arg = ap.ArgumentParser(description='Converts binary to C array.')
	arg.add_argument('-i', '--input', default='input.txt', help='File path to read binary from. Default\'input.txt\'', type=ap.FileType('r'))
	arg.add_argument('-o', '--output', default=sys.stdout, help='File path to write text to. Default:console', type=ap.FileType('w'))
	arg.add_argument('-c', '--column', default=10, help='The number of array items to be arranged horizontally. Default:10', type=int)
	arg.add_argument('-t', '--type', default='dec', choices=['hex', 'HEX', 'dec'], help='Item literal number form. Default:\'dec\'', type=str)
	cmd = arg.parse_args()
	binary = Read(cmd.input)
	array = CreateArray(binary, cmd.type)
	string = CreateStringFromArray(array, cmd.column)
	Write(cmd.output, string)

if __name__ == '__main__':
	RunConsole()
