from godot import exposed, export
from godot import *


@exposed
class HUD(Node2D):

	# member variables here, example:
	a = export(int)
	b = export(str, default='foo')

	def _ready(self):
		"""
		Called every time the node is added to the scene.
		Initialization here.
		"""
		pass
		
	def update_health(self):
			self.healthbar = self.get_node("HealthBar")
			self.helthbar.value = globalvar.hp
