import ikpy
import numpy as np
from ikpy import plot_utils

def get_angles():
	
	my_chain = ikpy.chain.Chain.from_urdf_file("robot_2link.URDF")
	target_vector = [ 0.6,0.4, 0.3]
	target_frame = np.eye(4)
	target_frame[:3, 3] = target_vector
	print("The angles of each joints are : ", my_chain.inverse_kinematics(target_frame))
	real_frame = my_chain.forward_kinematics(my_chain.inverse_kinematics(target_frame))
	print("Computed position vector : %s, original position vector : %s" % (real_frame[:3, 3], target_frame[:3, 3]))
	 
	import matplotlib.pyplot as plt
	ax = plot_utils.init_3d_figure()
	my_chain.plot( [ 0,0,0,0,0],ax, target=target_vector)
	my_chain.plot(my_chain.inverse_kinematics(target_frame), ax, target=target_vector)
	angles=my_chain.inverse_kinematics(target_frame)
    
	#plt.xlim(-1,1)
	#plt.ylim(-1,1)
	#plt.show()
	return angles
print(get_angles())
