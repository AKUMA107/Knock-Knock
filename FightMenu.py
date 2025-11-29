from godot import exposed, export, Sprite
from godot import Input

@exposed
class FightMenu(Sprite):
	# member variables here, example:
	a = export(int)
	b = export(str, default='foo')

	def _ready(self):
		print("FightMenu Check")
		self.visible = False

	def _process(self, delta):
		if Input.is_action_just_pressed("ui_ulti"):
			print("r")
			self.visible = False
		if Input.is_action_just_pressed("ui_e"):
			print("e")
			self.visible = False
		if Input.is_action_just_pressed("ui_g"):
			print("g")
			self.visible = False
		if Input.is_action_just_pressed("ui_tab"):
			print("tab")
			if self.visible == False:
				self.visible = True
			elif self.visible == True:
				self.visible = False
