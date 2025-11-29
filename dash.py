from godot import exposed, export
from godot import Sprite, Color, Tween, Timer, Input

@exposed
class CustomSprite(Sprite):
	limit4 = False

	def _ready(self):
		self.ghosting()
		self.set_z_index(-100)
		self.limit4 = False

	def ghosting(self):
		tween = Tween.new()
		self.add_child(tween)

		tween.interpolate_property(self, 'modulate', Color(1, 1, 1, 1), Color(1, 1, 1, 0), 0.75)
		tween.start()

		self.light_timer = Timer.new()
		self.add_child(self.light_timer)
		self.light_timer.set_wait_time(0.3)  # Set the timer duration here
		self.light_timer.connect("timeout", self, "_on_light_timer_timeout")

	def _on_light_timer_timeout(self):
		self.limit4 = False

	def _on_fade_timeout(self):
		self.queue_free()
	def _process(self, delta):
		if Input.is_action_just_pressed("ui_spacebar") and not self.limit4:
			self.set_z_index(-1)
			self.light_timer.start()
			self.limit4 = True

