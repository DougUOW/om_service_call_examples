# om_service_call_examples
###### Example code for using ROS service calls with Open Manipulator-X

This package is designed to provide some example code to help getting started using the Open Manipulator-X with ROS and Gazebo. All coding is done in Python.

## System Setup
###### Hardware
Intel NUC, OpenCR development board and Open Manipulator-X with XM430-W350-t motors

###### Software
- Intel Nuc is running Ubuntu 16.04 LTS
- Have installed all ROS packages as stated in Open Manipulator-X eManual
- OpenCR is running usb_to_dxl
- Dynamixel motors setup as per Open Manipulator-X eManual

*Note*  
If using OpenCR, USB port address may need to be changed in open_manipulator_controller.launch from USB0 to ACM0.  

## Codes
###### single_movement.py
This code will call the **/goal_joint_space_path** service and use it to make the Open Manipulator-X perfrom 1 movement.
###### multiple_movements.py
This code functions the same as single_movement.py, except it will perform multiple movements (3 instead of 1)
###### gripper_movement.py
This code will call the **/goal_tool_control** service and use it to control the position of the gripper.

## YouTube Links
The following links will provide video of the Open Manipulator-X being used in both hardware and simulation using service calls and the open_manipulator_controller package.  

###### Open Manipulator-X. ROS. Service Calls. Implementation on physical hardware.  
https://www.youtube.com/watch?v=8JTLWg_CjYg  

###### Open Manipulator-X. ROS. Gazebo. Service Calls. Example implementation.  
https://www.youtube.com/watch?v=IuSqCRb4uYA&t=36s  

## Execution
###### Simulation with Gazebo
roslaunch open_manipulator_controller open_manipulator_controller.launch use_platform:=false  
roslaunch open_manipulastor_gazebo open_manipulator_gazebo.launch  
rosrun om_service_call_examples single_movement.py  
  
*Additional Commands*  
roslaunch open_manipulator_control_gui open_manipulator_control_gui.launch  
rosservice call /controller_manager/list_controllers [TAB]+[TAB]  

###### Running on Real Open Manipulator-X
roslaunch open_manipulator_controller open_manipulator_controller.launch  
rosrun om_service_call_examples single_movement.py  
