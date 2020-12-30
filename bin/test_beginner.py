"""Test beginner file
"""
from beginner import beginner

__author__ = "help@castellanidavide.it"
__version__ = "1.0 2020-12-30"

def test():
	"""Tests the beginner function in the beginner class
	Write here all test you want to do.
	REMEMBER to test your programm you can't use __init__ function
	"""
	assert beginner() != "", "test failed"
	#assert beginner.<function>(<values>) == <the result(s) you would like to have>, "<the fail message>"
	
if __name__ == "__main__":
	test()
