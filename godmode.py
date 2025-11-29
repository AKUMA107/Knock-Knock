from godot import exposed, export
from godot import Node2D, Input , Timer
from globalvar import globalvar

@exposed
class godmode(Node2D):

	a = export(int)
	b = export(str, default='foo')
	limit = False

	def _ready(self):
		print("god check")
		self.set_z_index(-100)
		self.animation_player = self.get_node("AnimationPlayer")
		self.start_timer = Timer.new()
		self.add_child(self.start_timer)
		self.start_timer.connect("timeout", self, "_on_start_timer_timeout")
		self.start_timer.set_one_shot(True)
		

		self.duration_timer = Timer.new()
		self.add_child(self.duration_timer)
		self.duration_timer.connect("timeout", self, "_on_duration_timer_timeout")
		self.duration_timer.set_one_shot(True)
		
	def _process(self, delta):
		if not self.limit and Input.is_action_just_pressed("ui_g"):
			self.limit = True
			self.set_z_index(100)
			print("received")
			self.animation_player.play("GodMode")
			self.start_timer.set_wait_time(10.0)  # Set the initial delay before starting the animation
			self.start_timer.start()
			globalvar.god_mode = True

	def _on_start_timer_timeout(self):
		globalvar.god_mode = False
		self.queue_free()
		

	def _on_duration_timer_timeout(self):
		self.limit = False  # Reset the limit variable after the duration timer finishes

		
