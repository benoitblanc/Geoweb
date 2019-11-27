# -*-coding:UTF-8 -*

"""
				Xm
				Easy XML document creation
				Uses minidom
				Franck Favetta - 2017


				example:
				
					document:
					
						<?xml version="1.0" ?>
						<one a="1" b="2">
							<two>text1</two>
							<three a="1" b="2">
								<four>text2</four>
								<five>text3</five>
							</three>
							<six a="1">text4</six>
						</one>
					
					code:
					
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
"""

from xml.dom import minidom

class Xm:

	#create a document
	def __init__(self):
		self.doc = minidom.Document()
		
	#creates a node with text and returns it
	#att_list: list of attributes
	def text(self, name, att_list, text):
		node = self.doc.createElement(name)
		for key in att_list:
			node.setAttribute(key, str(att_list[key]) if att_list[key] is not None else '')
		text_node = self.doc.createTextNode(str(text))
		node.appendChild(text_node)
		return node
		
	#creates a node grouping a set nodes and returns it
	#att_list: list of attributes
	#node_list: list of nodes
	def group(self, name, att_list, node_list):
		node = self.doc.createElement(name)
		for key in att_list:
			node.setAttribute(key, str(att_list[key]) if att_list[key] is not None else '')
		for n in node_list:
			node.appendChild(n)
		return node
		
	#adds a node to another (the parent node) and returns the parent
	def add(self, parent_node, node):
		parent_node.appendChild(node)
		return parent_node
	
	#adds a node to the document root
	def root(self, root_node):
		self.doc.appendChild(root_node)
		
	#serializes the document
	def tostring(self):
		return self.doc.toprettyxml()
		
	#serializes in a file
	def tofile(self, file_name):
		with open(file_name, 'w', encoding='utf-8') as xmlFile:
			xmlFile.write(self.tostring())

		

		
		
		
		








