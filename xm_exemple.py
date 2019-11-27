# -*-coding:UTF-8 -*

"""
	exemple utilisant Xm
"""
from Xm import *

xm = Xm()
main = xm.group('one', {'a': 1, 'b': 2}, [ 
		xm.text('two', {}, 'text1'), 
		xm.group('three', {'a': 1, 'b': 2}, [
				xm.text('four', {}, 'text2'), 
				xm.text('five', {}, 'text3')
			])
	])
xm.add(main, xm.text('six', {'a': 1}, 'text4'))
xm.root(main)
xm.tofile('fileName.xml')
		

		
		
		
		








