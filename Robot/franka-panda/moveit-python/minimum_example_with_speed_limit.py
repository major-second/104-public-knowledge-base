#!/usr/bin/env python

MAX_V = 0.05
MAX_A = 0.05

import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
from math import pi
from moveit_commander.conversions import pose_to_list


def all_close(goal, actual, tolerance):
  """
  Convenience method for testing if a list of values are within a tolerance of their counterparts in another list
  @param: goal       A list of floats, a Pose or a PoseStamped
  @param: actual     A list of floats, a Pose or a PoseStamped
  @param: tolerance  A float
  @returns: bool
  """
  all_equal = True
  if type(goal) is list:
    for index in range(len(goal)):
      if abs(actual[index] - goal[index]) > tolerance:
        return False

  elif type(goal) is geometry_msgs.msg.PoseStamped:
    return all_close(goal.pose, actual.pose, tolerance)

  elif type(goal) is geometry_msgs.msg.Pose:
    return all_close(pose_to_list(goal), pose_to_list(actual), tolerance)

  return True

if __name__ == '__main__':
  try:
    moveit_commander.roscpp_initialize(sys.argv)
    rospy.init_node('move_group_python_interface_tutorial', anonymous=True)
    robot = moveit_commander.RobotCommander()
    scene = moveit_commander.PlanningSceneInterface()
    group_name = "panda_arm"
    move_group = moveit_commander.MoveGroupCommander(group_name)
    move_group.set_max_velocity_scaling_factor(MAX_V)
    move_group.set_max_acceleration_scaling_factor(MAX_A)

    display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path',
                                                   moveit_msgs.msg.DisplayTrajectory,
                                                   queue_size=20)
    planning_frame = move_group.get_planning_frame()
    eef_link = move_group.get_end_effector_link()
    group_names = robot.get_group_names()
    raw_input("Move to the initial point.")

    joint_goal = move_group.get_current_joint_values()
    joint_goal[0] = 0
    joint_goal[1] = -pi/4
    joint_goal[2] = 0
    joint_goal[3] = -pi/2
    joint_goal[4] = 0
    joint_goal[5] = pi/3
    joint_goal[6] = 0
    move_group.go(joint_goal, wait=True)
    move_group.stop()
    current_joints = move_group.get_current_joint_values()
    print all_close(joint_goal, current_joints, 0.01)
    raw_input("Show the cartesian goal.")

    pose_goal = geometry_msgs.msg.Pose()
    pose_goal.orientation.w = 1.0
    pose_goal.position.x = 0.4
    pose_goal.position.y = 0.1
    pose_goal.position.z = 0.4
    print pose_goal
    raw_input("Show the planned trajectory in Moveit.")

    (plan, fraction) = move_group.compute_cartesian_path(
                                       [pose_goal],   # waypoints to follow
                                       0.01,        # eef_step
                                       0.0)         # jump_threshold
    print fraction
    display_trajectory = moveit_msgs.msg.DisplayTrajectory()
    display_trajectory.trajectory_start = robot.get_current_state()
    display_trajectory.trajectory.append(plan)
    display_trajectory_publisher.publish(display_trajectory)
    raw_input("Slowly move to the point according to the trajectory.")

    move_group.set_pose_target(pose_goal)
    move_group.go(wait=True)
    move_group.stop()
    move_group.clear_pose_targets()
    current_pose = move_group.get_current_pose().pose
    print all_close(pose_goal, current_pose, 0.01)
    raw_input("Complete.")
  except rospy.ROSInterruptException:
    exit()
  except KeyboardInterrupt:
    exit()