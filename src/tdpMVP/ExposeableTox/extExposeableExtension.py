'''Info Header Start
Name : extExposeableExtension
Author : Wieland PlusPlusOne@AMB-ZEPH15
Saveorigin : Project.toe
Saveversion : 2023.12480
Info Header End'''

if __package__ is None:
	import some_relative_data
else:
	from . import some_relative_data

class extExposeableExtension:
	"""
	extExposeableExtension description
	"""
	def __init__(self, ownerComp):
		# The component to which this extension is attached
		self.ownerComp = ownerComp
		print( some_relative_data.important_value )

	