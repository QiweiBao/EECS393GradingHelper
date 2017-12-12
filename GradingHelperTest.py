'''
--------------------------------------
    Created by Qiwei Bao on 12/12/2017
--------------------------------------
'''

from GradingHelper import GradingHelper

repo_path = "/Users/qiweibao/Code/Python/"
filenames = []
test = GradingHelper()
filenames = test.readFileNames(filenames, repo_path)
for filename in filenames:
	print filename

testcase = test.selectTestCases(filenames)
test.countLines(testcase)

codes = test.selectCodes(filenames)
test.countLines(codes)