from godot import exposed, export
from godot import Node2D, Input, Timer
from globalvar import globalvar

@exposed
class Ultimate(Node2D):
	a = export(int)
	b = export(str, default='foo')

	def _ready(self):
		print("ulti check")
		self.set_z_index(-10)
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
		if Input.is_action_just_pressed("ui_ulti"):
			self.set_z_index(1)
			globalvar.hp += 20
			print(globalvar.hp)
			print("recieved")
			self.animation_player.play("Load")
			self.start_timer.set_wait_time(1.01)  # Set the initial delay before starting the animation
			self.start_timer.start()

	def _on_start_timer_timeout(self):
		self.animation_player.play("moyamoya")
		self.duration_timer.set_wait_time(3.2)  # Set the duration of the animation
		self.duration_timer.start()

	def _on_duration_timer_timeout(self):
		globalvar.hp = 100
		print(globalvar.hp)
		self.queue_free()  # Free the node after the animation duration completes
