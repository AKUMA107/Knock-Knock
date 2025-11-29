from godot import exposed, export
from godot import Timer, Node2D ,Input
from globalvar import globalvar

@exposed
class Hall(Node2D):

	a = export(int)
	b = export(str, default='foo')

	def _ready(self):
		"""
		Called every time the node is added to the scene.
		Initialization here.
		"""
		  # Connect the timer's timeout signal to a method

	def _process(self, delta):
		if globalvar.e == 30:
			print("30")
			  # Start the timer
			if Input.is_action_just_pressed("ui_anything"):
				self.get_tree().change_scene("res://credits.tscn")

	
