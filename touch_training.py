import rospy
import baxter_interface
import time

rospy.init_node('hello')

limb = baxter_interface.Limb('left')
angles = limb.joint_angles()

#angles['left_w0'] = 0.6649806707885743
#angles['left_w1'] = 1.1451166568481446
#angles['left_w2'] = -0.17372332402954102
#angles['left_e0'] = -0.5453301694702148
#angles['left_e1'] = 0.3574175231689453
#angles['left_s0'] = -0.8958447791015626
#angles['left_s1'] = -0.27189809434204104
#limb.move_to_joint_positions( angles )
point_1 = {'left_w0': 0.6649806707885743, 'left_w1': 1.1451166568481446, 'left_w2': -0.17372332402954102, 'left_e0': -0.5453301694702148, 'left_e1': 0.3574175231689453, 'left_s0': -0.8958447791015626, 'left_s1': -0.27189809434204104}
limb.move_to_joint_positions( point_1 )


#angles['left_w0'] = 0.7830971913208008
#angles['left_w1'] = 1.1079176227844239
#angles['left_w2'] = -0.49164084195556645
#angles['left_e0'] = -0.8782040000610352
#angles['left_e1'] = 0.7378447581298828
#angles['left_s0'] = -0.6856894114013672
#angles['left_s1'] = -0.47131559653930666
#limb.move_to_joint_positions( angles )
point_2 = {'left_w0': 0.7830971913208008, 'left_w1': 1.1079176227844239, 'left_w2': -0.49164084195556645, 'left_e0': -0.8782040000610352, 'left_e1': 0.7378447581298828, 'left_s0': -0.6856894114013672, 'left_s1': -0.47131559653930666}
limb.move_to_joint_positions( point_2 )


#angles['left_w0'] = 0.6435049397827148
#angles['left_w1'] = 0.9736943039978028
#angles['left_w2'] = -0.4874223947937012
#angles['left_e0'] = -1.1190389834838868
#angles['left_e1'] = 1.9374177328857423
#angles['left_s0'] = -0.1438106986999512
#angles['left_s1'] = -0.9606554673156739
#limb.move_to_joint_positions( angles )
point_3 = {'left_w0': 0.6435049397827148, 'left_w1': 0.9736943039978028, 'left_w2': -0.4874223947937012, 'left_e0': -1.1190389834838868, 'left_e1': 1.9374177328857423, 'left_s0': -0.1438106986999512, 'left_s1': -0.9606554673156739}
limb.move_to_joint_positions( point_3 )

for _move in range(10):
    limb.move_to_joint_positions( point_2 )
    time.sleep( 5 )
    limb.move_to_joint_positions( point_1 )
    time.sleep( 5 )
    limb.move_to_joint_positions( point_2 )
    time.sleep( 5 )
    limb.move_to_joint_positions( point_3 )
    time.sleep( 5 )


