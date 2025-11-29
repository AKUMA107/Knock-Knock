from godot import exposed, export
from godot import *
from globalvar import globalvar

@exposed
class Control(Control):

	# member variables here, example:
	a = export(int)
	b = export(str, default='foo')

	def _ready(self):
		"""
		Called every time the node is added to the scene.
		Initialization here.
		"""
		pass
		
	def _on_TextureButton_pressed(self):
		globalvar.replay = True
		
	def _on_TextureButton2_pressed(self):
		pass
		
