# Import the necessary modules from the Godot module
from godot import Camera2D, exposed
from globalvar import globalvar

# Expose the class to Godot
@exposed
class deadcam(Camera2D):
		def _process(self, delta):
		# Check if globalvar.alive is False
			if  globalvar.alive == False:
			# Set the current property of this camera to True
				self.make_current()
		
