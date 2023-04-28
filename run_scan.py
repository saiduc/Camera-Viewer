from experiment_control.scan_generator import *
from instrument_control.camera import *
from instrument_control.stage import *
import time

camera = Camera("Solid HHG Detector").initiate()
camera.set_exposure(10000000)
camera.set_gain(27)

# wedge_stage = Stage("Wedge").initiate()
# lens_stage = Stage("Lens").initiate()
# c_stage = Stage("Compression").initiate()
# hwp_stage = Stage("HWP").initiate()
rot_stage = Stage("ROT").initiate()
# FW_stage = Stage("Filter Wheel").initiate()
#iris_stage = Stage("Iris").initiate()

# lens_stage.set_position(12.5)
# c_stage.set_position(5.3)
# hwp_stage.set_position(114)
# time.sleep(5)

# print(lens_stage.get_position())
# print(c_stage.get_position())
# print(hwp_stage.get_position())

scan = ScanGenerator()
scan.set_detector(camera)
scan.set_save_directory("C:\\Users\\reddragon\\Documents", "Scan_f-9_w25_minpower_MgO100_MCP1")
#c_stage.set_position(5.1462)
# scan.add_axis(c_stage, np.repeat(np.linspace(4.5,5.6,11),6))
# scan.add_axis(hwp_stage, np.repeat([5.0,6.0,6.5,7.0,7.5,8.0,8.5,9.0,9.5,10.0,10.5,11.0,11.5,12.0,13.0,15.0],3))
scan.add_axis(rot_stage, np.repeat([45, 60, 75, 90,105, 120, 135],3))
#scan.add_axis(FW_stage, np.repeat(np.array([0,120,240]),6*20))
# scan.add_axis(wedge_stage, np.repeat(np.array([7, 13, 20, 25]),5))

#scan.run_repeats(20*6)
scan.run_scan()
scan.output_config()
#iris_stage.set_position(76)

