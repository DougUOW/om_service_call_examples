#! /usr/bin/env python

# This code can be used to control the gripper. Position can be changed with
# the range +/-0.01

import rospy
import sys
from open_manipulator_msgs.srv import SetJointPosition, SetJointPositionRequest

rospy.init_node('service_set_joint_position_client')
rospy.wait_for_service('/goal_tool_control')
goal_joint_space_path_service_client = rospy.ServiceProxy('/goal_tool_control', SetJointPosition)
goal_joint_space_path_request_object = SetJointPositionRequest()

goal_joint_space_path_request_object.planning_group = 'gripper'
goal_joint_space_path_request_object.joint_position.joint_name = ['gripper']
goal_joint_space_path_request_object.joint_position.position = [0.01]
goal_joint_space_path_request_object.joint_position.max_accelerations_scaling_factor = 1.0
goal_joint_space_path_request_object.joint_position.max_velocity_scaling_factor = 1.0
goal_joint_space_path_request_object.path_time = 2.0

rospy.loginfo("Moving Gripper...")

result = goal_joint_space_path_service_client(goal_joint_space_path_request_object)

print result
