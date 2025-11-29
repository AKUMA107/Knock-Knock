from godot import exposed, export
from godot import TextureProgress
from globalvar import globalvar


@exposed
class hp(TextureProgress):

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
		self.value = globalvar.hp
