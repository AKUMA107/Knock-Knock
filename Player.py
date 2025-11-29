from godot import exposed, export, PackedScene
from godot import KinematicBody2D, Vector2, Input, ResourceLoader, Timer
from globalvar import globalvar

@exposed
class Player(KinematicBody2D):
	a = export(int)
	b = export(str, default='foo')
	ghost_node = export(PackedScene)

	def _ready(self):
		self.move_speed = 40.0
		self.animation_player = self.get_node("AnimationPlayer")
		self.ghost_timer = self.get_node("ghosttimer")  # Initialize your ghost_timer here
		self.limit2 = False  # Initialize the class variable
		self.limit3 = False
		self.last_move_vector = Vector2()
		self.speed_timer = Timer.new()
		self.dash_timer = Timer.new()
		self.add_child(self.speed_timer)
		self.add_child(self.dash_timer)
		self.speed_timer.connect("timeout", self, "_on_speed_timer_timeout")
		self.dash_timer.connect("timeout", self, "_on_dash_timer_timeout")
		self.ghost_timer.connect("timeout",self,"_on_ghosttimer_timeout")
		self.dash_timer.set_one_shot(True)
		# Load the PackedScene into ghost_node
		self.ghost_node = ResourceLoader.load("res://dash.tscn")  # Adjust the path
		self.enemy_attack = False
		globalvar.alive = True
	def _physics_process(self, delta):
		input_state = Input
		self.enemy_attacking(self)
		move_vector = Vector2()
		
		if globalvar.hp <= 0:
			print("dead")
			globalvar.hp = 0
			globalvar.alive = False
			
			self.queue_free()
			
			
			
		
			

		if input_state.is_action_pressed("ui_right"):
			move_vector.x += 1
		if input_state.is_action_pressed("ui_left"):
			move_vector.x -= 1
		if input_state.is_action_pressed("ui_down"):
			move_vector.y += 1
		if input_state.is_action_pressed("ui_up"):
			move_vector.y -= 1
		if input_state.is_action_just_pressed("ui_spacebar") and self.limit3== False:
			self.move_speed = 200
			self.speed_timer.set_wait_time(0.15)  # Set the initial delay before starting the animation
			self.speed_timer.start()
			self.dash_timer.set_wait_time(0.3)
			self.dash_timer.start()
			self.limit3 = True
		if input_state.is_action_just_pressed("ui_tab"):
			
			if not self.limit2:
				
				ultimate_scene = ResourceLoader.load("res://Ultimate.tscn")
				ultimate_instance = ultimate_scene.instance()
				self.add_child(ultimate_instance)
				god_scene = ResourceLoader.load("res://godmode.tscn")
				god_instance = god_scene.instance()
				self.add_child(god_instance)
				self.limit2 = True

		if move_vector.length() > 0:
			move_vector = move_vector.normalized()
			move_vector *= self.move_speed
			self.move_and_slide(move_vector)

		self.update_animation(move_vector)
		self.last_move_vector = move_vector

	def _on_speed_timer_timeout(self):
		self.move_speed = 40 # Stop the dash timer here

	def _on_dash_timer_timeout(self):
		self.limit3 = False
		self.dash_timer.stop()
		self.dash_timer.start()

	def update_animation(self, move_vector):
		if move_vector.x > 0:
			self.animation_player.play("WalkRight")
		elif move_vector.x < 0:
			self.animation_player.play("WalkLeft")
		elif move_vector.y > 0:
			self.animation_player.play("WalkDown")
		elif move_vector.y < 0:
			self.animation_player.play("WalkUp")
		else:
			if self.last_move_vector.x > 0:
				self.animation_player.play("IdleRight")
			elif self.last_move_vector.x < 0:
				self.animation_player.play("IdleLeft")
			elif self.last_move_vector.y > 0:
				self.animation_player.play("IdleDown")
			elif self.last_move_vector.y < 0:
				self.animation_player.play("IdleUp")

	def add_ghost(self):
		if self.ghost_node:
			ghost = self.ghost_node.instance()
			ghost.position = self.position
			ghost.scale = self.get_node("Sprite").scale
			self.get_tree().get_root().add_child(ghost)

	def _on_ghosttimer_timeout(self):
		self.add_ghost()

	def _on_hitbox_body_entered(self,body):
		if body.has_method("enemy"):
			self.enemy_attack = True
		if body.has_method("emo") and globalvar.god_mode == False :
			globalvar.hp-=10
			print(globalvar.hp)
		
	def player(self):
		pass
		
	def _on_hitbox_body_exited(self,body):
		if body.has_method("enemy"):
			self.enemy_attack = False
			
	def enemy_attacking(self,body):
		if self.enemy_attack == True and globalvar.god_mode == False :
			globalvar.hp-=1
			print(globalvar.hp)
			
	
		
			
			
	
