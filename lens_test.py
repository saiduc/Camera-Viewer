from experiment_control.scan_generator import *
from instrument_control.camera import *
from instrument_control.stage import *
import time

lens_stage = Stage("Lens").initiate()

lens_stage.set_position(13)

