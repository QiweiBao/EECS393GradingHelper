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
		if "." is in repo_path:
			res.append(item)
			return res
		fileAndDir = []
		if os.path.exists(repo_path):
			fileAndDir = os.listdir(repo_path)

		for item in fileAndDir:
			item = repo_path + item + "/"
			if "." not in item:
				sub_fileAndDir = self.readFileNames(res, item)
			else:
				res.append(item)
				# fileAndDir.append(item)
		return res

	# delete the last / from filenames
	def formatFileNames(self, filenames):
		return [filename[:-1] for filename in finenames]

	# Select file names of test cases
	def selectTestCases(self, filenames):
		res = []
		for filename in filenames:
			if (("test" is in filename) or ("Test" is in filename) or ("TEST" is in filename)):
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
	def countLines(self, filePath, pathname, dataType):
		'''for filename in filenames:
			os.system("cloc --list-file=" + filePath + "| tee -a /Users/qiweibao/Data/EECS393GradingHelper/" + dataType + "_tmp.txt")
		'''
		os.system("cloc --list-file=" + filePath + "| tee -a " + pathname + dataType + "_count.txt")

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

	# Delete root directory
	def writeFileList(self, Data, pathwrite):
		# self.clearFileList(pathwrite)
		output = open(pathwrite, 'ab+')
		for i in Data:
			output.write(".." + str(i)[34:])
			output.write("\n")
		output.close()




