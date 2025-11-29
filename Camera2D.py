from godot import exposed, export
from godot import *
from globalvar import globalvar

@exposed
class o2d(Camera2D):

	# member variables here, example:
	a = export(int)
	b = export(str, default='foo')

	
