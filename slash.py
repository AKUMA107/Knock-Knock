from godot import exposed, Area2D, Input
from testing import testing

@exposed
class Slash(Area2D):
	animation_finished = exposed()

	def _ready(self):
		print("slash check")
		self.animation_player = self.get_node("AnimationPlayer")
		print(testing.a)
		#self.animation_player.connect("animation_finished", self, "_on_animation_finished")

	def _process(self, delta):
		input_state = Input

		# Check if the "P" key is pressed and if the player is moving
		if input_state.is_action_just_pressed("ui_accept"):
			# Get the player's movement direction
			horizontal_input = input_state.is_action_pressed("ui_right") - input_state.is_action_pressed("ui_left")
			vertical_input = input_state.is_action_pressed("ui_down") - input_state.is_action_pressed("ui_up")

			# Check if the player is moving in any direction
			if horizontal_input != 0 or vertical_input != 0:
				# Determine the appropriate slash animation based on player's direction
				animation_name = "slashRight"

				if horizontal_input > 0:
					animation_name = "slashRight"
				elif horizontal_input < 0:
					animation_name = "slashLeft"
				elif vertical_input > 0:
					animation_name = "slashDown"
				elif vertical_input < 0:
					animation_name = "slashUp"

				self.animation_player.play(animation_name)
				
	def slash(self):
		pass
		
	def _on_slash_body_entered(self,body):
		if body.has_method("enemy"):
			pass
		
	
