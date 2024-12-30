# import necessary modules
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Color
import time

# new class that inherits Node class
class TurtleController(Node):
	# constructor method
	def __init__(self):
		# initialize node with unique name
		super().__init__('turtle_controller_1')
		
		# create a publisher which publish Twist type messages to the topic '/turtle1/cmd_vel' with a queue size of 10
		self.publisher = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
		
		# create a subscription to listen to Color type messages for the topic 'turtle1/color_sensor' with a queue size of 10
		self.subscription = self.create_subscription(Color, '/turtle1/color_sensor', self.color_sensor_callback, 10)
		
		# create a timer to call publish_msg_cmd_vel method every second
		self.timer = self.create_timer(1.0, self.publish_msg_cmd_vel)
		
		# instantiate Twist type message to define angular and linear velocities of turtle
		self.twist_msg = Twist()
        

	def publish_msg_cmd_vel(self):
		# set linear velocity
		self.twist_msg.linear.x = 0.5 
		
		# set angular velocity
		self.twist_msg.angular.z = 0.4
		
		# publish Twist message to specify angular and linear velocities of turtle
		self.publisher.publish(self.twist_msg)
		
		# print message to console to verfiy frequency
		self.get_logger().info('Publishing twist message')

	def color_sensor_callback(self, msg):
		# print message to console
		self.get_logger().info(f'Color Sensor Data: R={msg.r}, G={msg.g}, B={msg.b}')


# starting point of script
def main(args=None):
	# initialize rclpy library
	rclpy.init(args=args)
	
	# create object for TurtleController class
	turtle_controller = TurtleController()
	
	# start the event loop to handle incoming messages and timer
	rclpy.spin(turtle_controller)
	
	# cleanup after program is finished
	turtle_controller.destroy_node()
	
	# release resources and shutdown
	rclpy.shutdown()


if __name__ == '__main__':
    main()
