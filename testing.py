from godot import exposed, export
from godot import *


@exposed
class testing(Node):

	# member variables here, example:
	a = 1
	b = export(str, default='foo')

	def _ready(self):
		self.a = 1
