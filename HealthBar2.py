from godot import exposed, export
from godot import *
from globalvar import globalvar

@exposed
class HealthBar2(TextureProgress):

	# member variables here, example:
	a = export(int)
	b = export(str, default='foo')

	def _ready(self):
		"""
		Called every time the node is added to the scene.
		Initialization here.
		"""
		pass
		
	def _process(self,delta):
		self.value = globalvar.kc
		if globalvar.kc >= 5:
			self.value = 5
