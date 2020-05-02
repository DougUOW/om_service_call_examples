#! /usr/bin/env python

# This code exapnds on the code single_movement.py to include 3 movements,
# it will move from home, to zero and back. There is a 5 second delay to stop 
# code skipping ahead to the next section until movement has been completed

import rospy
import sys
from open_manipulator_msgs.srv import SetJointPosition, SetJointPositionRequest

rospy.init_node('service_set_joint_position_client')
rospy.wait_for_service('/goal_joint_space_path')
goal_joint_space_path_service_client = rospy.ServiceProxy('/goal_joint_space_path', SetJointPosition)
goal_joint_space_path_request_object = SetJointPositionRequest()

# 1st Movement
goal_joint_space_path_request_object.planning_group = 'arm'
goal_joint_space_path_request_object.joint_position.joint_name = ['joint1', 'joint2', 'joint3', 'joint4']
goal_joint_space_path_request_object.joint_position.position = [0.0, -1, 0.3, 0.7]
goal_joint_space_path_request_object.joint_position.max_accelerations_scaling_factor = 1.0
goal_joint_space_path_request_object.joint_position.max_velocity_scaling_factor = 1.0
goal_joint_space_path_request_object.path_time = 2.0

rospy.loginfo("Doing Service Call 1...")
result = goal_joint_space_path_service_client(goal_joint_space_path_request_object)
print result
rospy.sleep(5)

# 2nd Movement
goal_joint_space_path_request_object.planning_group = 'arm'
goal_joint_space_path_request_object.joint_position.joint_name = ['joint1', 'joint2', 'joint3', 'joint4']
goal_joint_space_path_request_object.joint_position.position = [0.0, 0.0, 0.0, 0.0]
goal_joint_space_path_request_object.joint_position.max_accelerations_scaling_factor = 1.0
goal_joint_space_path_request_object.joint_position.max_velocity_scaling_factor = 1.0
goal_joint_space_path_request_object.path_time = 2.0

rospy.loginfo("Doing Service Call 2...")
result = goal_joint_space_path_service_client(goal_joint_space_path_request_object)
print result
rospy.sleep(5)

# 3rd Movement
goal_joint_space_path_request_object.planning_group = 'arm'
goal_joint_space_path_request_object.joint_position.joint_name = ['joint1', 'joint2', 'joint3', 'joint4']
goal_joint_space_path_request_object.joint_position.position = [0.0, -1, 0.3, 0.7]
goal_joint_space_path_request_object.joint_position.max_accelerations_scaling_factor = 1.0
goal_joint_space_path_request_object.joint_position.max_velocity_scaling_factor = 1.0
goal_joint_space_path_request_object.path_time = 2.0

rospy.loginfo("Doing Service Call 3...")
result = goal_joint_space_path_service_client(goal_joint_space_path_request_object)
print result
rospy.sleep(5)
