from godot import exposed, export
from godot import ResourceLoader, Control


@exposed
class game_over(Control):

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
		print("lol")
		self.get_tree().change_scene("res://ColorRect.tscn")
		
	def _on_TextureButton2_pressed(self):
		self.get_tree().quit()
