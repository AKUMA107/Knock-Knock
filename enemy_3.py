from godot import exposed, export
from godot import KinematicBody2D, Vector2, Input, ResourceLoader, Timer
import random
from globalvar import globalvar

@exposed
class enemy_3(KinematicBody2D):
	a = export(int)
	b = export(str, default='foo')

	def _ready(self):
		self.move_speed = 60
		self.animation_player = self.get_node("AnimationPlayer")
		self.player_chase = False
		self.player = None
		self.hp = 20
		
		
	def _on_detectionarea_body_entered(self, body):
		self.player = body
		self.player_chase = True
		
	def _physics_process(self, delta):
		if self.player_chase:
			move_vector = self.player.position - self.position
			move_direction = move_vector.normalized()
			velocity = move_direction * self.move_speed
			velocity = self.move_and_slide(velocity)
			self.update_animation(move_direction)
		if self.hp <= 0:
			print("another falls to your blade")
			self.hp = 0
			self.queue_free()
			globalvar.kc+=1
			globalvar.e+=1
		
	def update_animation(self, move_vector):
		if abs(move_vector.x) > abs(move_vector.y):
			if move_vector.x > 0:
				self.animation_player.play("WalkRight")
			elif move_vector.x < 0:
				self.animation_player.play("WalkLeft")
		else:
			if move_vector.y > 0:
				self.animation_player.play("WalkDown")
			elif move_vector.y < 0:
				self.animation_player.play("WalkUp")
				
	def enemy(self):
		pass
		
	def _on_Area2D_area_entered(self,body):		
		if body.has_method("slash"):
			self.hp-=10
			print(self.hp)
			
		if body.has_method("AOE"):
			self.hp-=30
			print(self.hp)
