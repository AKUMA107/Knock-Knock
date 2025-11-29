from godot import exposed, export
from godot import Node2D


@exposed
class globalvar(Node2D):

	# member variables here, example:
	god_mode = False
	hp = 100
	kc = 0
	alive = True
	replay = False
	e = 0

	def _ready(self):
		
		pass
		
	def god_mode_bool(self):
		self.god_mode = False
