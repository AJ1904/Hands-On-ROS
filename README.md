# ROS2 Assignment: Installation, Exploration, and Implementation

https://github.com/user-attachments/assets/cbd9a155-fd2c-406d-9d1f-5a2c6ea9c259


## Overview and Purpose

This assignment involved installing ROS2, exploring its behavior, and developing a simple program within the ROS system. The goal was to gain foundational experience with ROS2 and set up a working development environment for future projects in the course.

## Logistics

This assignment was completed **individually**.

## Reference Material

The ROS documentation was extensively consulted to complete this assignment. This assignment emphasized practicing the ability to find, read, and apply relevant documentation effectively.

## Tasks

### Task 1: Install

ROS2 was installed on a Linux-based system, specifically using the **Humble** distribution. This ensured compatibility and reliability. Windows and macOS were avoided due to limited ROS support.

No specific deliverables were required for this task.

---

### Task 2: Draw

The `turtlesim` simulator and `turtle_teleop_key` node were launched in the ROS2 system. Using arrow keys, a picture was drawn with the turtle’s path. A screenshot of the creation was included in the report. This step verified proper ROS2 installation and configuration for graphical programs and multi-node operation.

---

### Task 3: Explore

The `ros2` command-line tool was used to explore the system while `turtlesim` was running. The following were achieved:
- Listed all **topics** in the system.
- Selected a topic and identified its data type, number of publishers, and subscribers.
- Examined the fields of the topic's data type.
- Counted the total number of **interfaces** (messages, services, actions).
- Counted the number of **packages** starting with the letter `s`.

The commands and their outputs were documented in the report.

---

### Task 4: Implement

A program was written to:
1. Publish messages to `/turtle1/cmd_vel`, moving the turtle in a circular pattern.
2. Subscribe to `/turtle1/color_sensor` and print incoming messages to the console.

The program was added to a ROS workspace and package, built, and executed using the command:
```bash
ros2 run <package_name> <program_name>
```

The package build commands, program execution, outputs, and a screenshot of the circle-drawing turtle were included in the submission. The program's source code was provided in the final submission.

---

### Task 5: Install

The `sim` package was downloaded and extracted into the `src` directory of the ROS workspace. The workspace was built, and the package was verified using:
```bash
ros2 pkg prefix sim
```

The command output was included in the report.

---

### Task 6: Visualize

The `sim1` executable from the `sim` package was launched using `ros2 run`. The `rviz2` tool was configured to display:
- A **RobotModel** display showing the robot’s shape.
- A **MarkerArray** display to visualize the robot's path.

The simulated robot was made to move, and its path was displayed as a red trail. A screenshot of the `rviz2` window showing the robot and its path was included in the report. Additionally, the configuration was saved as an `.rviz` file for future use, which was included in the final submission.

---

