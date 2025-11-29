from godot import exposed, export
from godot import Timer,Input


@exposed
class ghosttimer(Timer):

	# member variables here, example:
	a = export(int)
	b = export(str, default='foo')

	def _ready(self):
		"""
		Called every time the node is added to the scene.
		Initialization here.
		"""
		pass
		
		
	def _process(self, delta):
		if Input.is_action_pressed("ui_spacebar"):
			self.start(0.15)
			
		
		
