#!/usr/bin/env python3
#
# Author: Felix Chiang
# Date: 4/8/2019
# Description: Localization of DarkNet Training files paths
# 
#

import os

def main ():

	#Current Localized Working Directory
	cwd = os.getcwd()
	
	print("Localizing to {}".format(cwd))

	#491 File that require Localization
	data_filename = "491.data"
	#name_filename = "491.names"
	test_filename = "491_test.txt"
	train_filename = "491_train.txt"
	valid_filename = "491_valid.txt"

	#Test that all files exist before work
	if not os.path.isfile(data_filename):
		print("491.data file could not be found")
		quit()
	#if not os.path.isfile(name_filename):
	#	print("491.names file could not be found")
	#	quit()
	if not os.path.isfile(test_filename):
		print("491_test.txt file could not be found")
		quit()
	if not os.path.isfile(train_filename):
		print("491_train.txt file could not be found")
		quit()
	if not os.path.isfile(valid_filename):
		print("491_valid.txt file could not be found")
		quit()


	#Test if all files are accessible before work
	try:
		data_file = open(data_filename,'w')
	except:
		print("Error Opening File 491.data")
		quit()

	#try:
	#	name_file = open(name_filename,'r+')
	#except:
	#	print("Error Opening File 491.names")
	#	quit()

	try:
		test_file = open(test_filename,'r+')
	except:
		print("Error Opening File 491_train.txt")
		quit()

	try:
		train_file = open(train_filename,'r+')
	except:
		print("Error Opening File 491_train.txt")
		quit()

	try:
		valid_file = open(valid_filename,'r+')
	except:
		print("Error Opening File 491_valid.txt")
		quit()

	
	#Localize 491.data
	data_text = "classes = 4\n" 
	data_text += "train = {}/491_train.txt\n".format(cwd) 
	data_text += "valid = {}/491_valid.txt\n".format(cwd) 
	data_text += "names = {}/491.names\n".format(cwd) 
	data_text += "backup = backup"
	data_file.write(data_text)

	#Localize Test Data
	for line in test_file:
		head, tail = os.path.split(line)
		line = "{}/images/{}".format(cwd,tail)
	
	#Localize Train Data
	for line in train_file:
		head, tail = os.path.split(line)
		line = "{}/images/{}".format(cwd,tail)

	#Localize Valid Data
	for line in valid_file:
		head, tail = os.path.split(line)
		line = "{}/images/{}".format(cwd,tail)

	#Close all files
	data_file.close()
	test_file.close()
	train_file.close()
	valid_file.close()

	print("Localization Complete")

if __name__ == "__main__":
	main()
