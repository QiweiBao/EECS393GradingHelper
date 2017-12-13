'''
--------------------------------------
	Created by Qiwei Bao on 12/10/2017
--------------------------------------
'''

import re
import os 
import logging

class GradingHelper():
	# Read names of all the files from a direcotry
	def readFileNames(self, res, repo_path):
		if repo_path.find(".") is not -1:
			res.append(item)
			return res
		fileAndDir =  os.listdir(repo_path)

		for item in fileAndDir:
			item = repo_path + item + "/"
			if item.find(".") is -1 and item.find("LICENSE") is -1:
				sub_fileAndDir = self.readFileNames(res, item)
			else:
				res.append(item)
				# fileAndDir.append(item)
		return res

	# delete the last / from filenames
	def formatFileNames(self, filenames):
		res = []
		for filename in filenames:
			filename = filename[:-1]
			res.append(filename)
		return res

	# Select file names of test cases
	def selectTestCases(self, filenames):
		res = []
		for filename in filenames:
			if ((filename.find("test") is not -1) or (filename.find("Test") is not -1) or (filename.find("TEST") is not -1)):
				res.append(filename)
		return res

	# Select file names of codes
	def selectCodes(self, filenames):
		res = []
		for filename in filenames:
			if ((filename.find("test") is -1) and (filename.find("Test") is -1) and (filename.find("TEST") is -1)):
				res.append(filename)
		return res

	# Count lines of codes using cloc
	def countLines(self, filePath, dataType):
		'''for filename in filenames:
			os.system("cloc --list-file=" + filePath + "| tee -a /Users/qiweibao/Data/EECS393GradingHelper/" + dataType + "_tmp.txt")
		'''
		os.system("cloc --list-file=" + filePath + "| tee -a /Users/qiweibao/Data/EECS393GradingHelper/" + dataType + "_tmp.txt")

	# Write data into a text.
	def writeDataList(self, Data, pathwrite):
		# self.clearFileList(pathwrite)
		output = open(pathwrite, 'ab+')
		for i in Data:
			output.write(str(i))
			output.write("\n")
		output.close()

	# clear file name list before write
	def clearFileList(self, pathwrite):
		if os.path.isfile(pathwrite):
			os.remove(pathwrite)

	# Count numbers of files
	def countFiles(self, filenames):
		count = 0
		for file in filenames:
			count += 1
		return count




