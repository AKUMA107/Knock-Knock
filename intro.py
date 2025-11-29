from godot import exposed, export
from godot import *


@exposed
class intro(Control):

	# member variables here, example:
	a = export(int)
	b = export(str, default='foo')

	def _ready(self):
		"""
		Called every time the node is added to the scene.
		Initialization here.
		"""
		pass
		
	def _on_Timer_timeout(self):
		self.get_tree().change_scene("res://Hall.tscn")
