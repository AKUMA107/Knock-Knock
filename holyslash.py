from godot import exposed, Area2D, Input
from globalvar import globalvar

@exposed
class holyslash(Area2D):
	animation_finished = exposed()

	def _ready(self):
		print("holyslash check")
		self.animation_player = self.get_node("AnimationPlayer")
		self.set_z_index(-10)
		#self.animation_player.connect("animation_finished", self, "_on_animation_finished")

	def _process(self, delta):
		input_state = Input

		# Check if the "P" key is pressed and if the player is moving
		if input_state.is_action_just_pressed("ui_e") and globalvar.kc>= 5:
			globalvar.kc -=5
			self.set_z_index(-1)
			self.animation_player.play("AOE")
			
	def AOE(self):
		pass
