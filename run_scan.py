from experiment_control.scan_generator import *
from instrument_control.camera import *
from instrument_control.stage import *

camera = Camera("Solid HHG Detector").initiate()
camera.set_exposure(10000000)
camera.set_gain(27)

# wedge_stage = Stage("Wedge").initiate()
lens_stage = Stage("Lens").initiate()
c_stage = Stage("Compression").initiate()
#iris_stage = Stage("Iris").initiate()

scan = ScanGenerator()
scan.set_detector(camera)
scan.set_save_directory("Z:\\project\\laserprojectsmatthews\\live\\Kasia_RDS\\SolidHHG\\20221104", "Scan_MCP1800V_1p3cm_800nm_focusScan_h2o_withaerosols")
#c_stage.set_position(5.1462)
# scan.add_axis(c_stage, np.repeat(np.linspace(5.06,5.20,14),30))
# scan.add_axis(c_stage, np.linspace(5.03,5.20,2))
scan.add_axis(lens_stage, np.repeat(np.array([2.5,5.5]),20))
# scan.add_axis(wedge_stage, np.repeat(np.array([7, 13, 20, 25]),5))

scan.run_scan()

#iris_stage.set_position(76)

