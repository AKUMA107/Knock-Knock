from godot import exposed, export
from godot import ResourceLoader,YSort
from globalvar import globalvar


@exposed
class YSort_elements(YSort):

	# member variables here, example:
	a = export(int)
	b = export(str, default='foo')

	def _ready(self):
		pass
		player_scene = ResourceLoader.load("res://player_things.tscn")
		player_instance = player_scene.instance()
		self.add_child(player_instance)
		
	def _process(self,delta):
		'''if globalvar.hp <= 0:
			player_scene = ResourceLoader.load("res://player_things.tscn")
			player_instance = player_scene.instance()
			self.add_child(player_instance)
			globalvar.replay = False'''
		pass
