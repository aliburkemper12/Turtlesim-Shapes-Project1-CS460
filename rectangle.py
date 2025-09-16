import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time

class MinimalPublisher(Node):
    def __init__(self):
        super().__init__('minimal_publisher')
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)

    def draw_rectangle(self):
        move = Twist()
        # loop twice
        # each loop creates a long and short side of rectangle
        for _ in range(2):
            # first create short side (smaller linear velocity)
            move.linear.x = 1.0
            move.angular.z = 0.0
            self.publisher_.publish(move)
            time.sleep(3.0)
            # rotate ~ 90 degrees
            move.linear.x = 0.0
            move.angular.z = 1.6
            self.publisher_.publish(move)
            time.sleep(3.0)
            # now create long side (larger linear velocity)
            move.linear.x = 2.0
            move.angular.z = 0.0
            self.publisher_.publish(move)
            time.sleep(3.0)
            # rotate ~ 90 degrees
            move.linear.x = 0.0
            move.angular.z = 1.6
            self.publisher_.publish(move)
            time.sleep(3.0)

def main(args=None):
    rclpy.init(args=args) #initialize
    node = MinimalPublisher() # create publisher node
    node.draw_rectangle() # call draw_rectangle
    node.destroy_node() # destroy node
    rclpy.shutdown() # shutdown

if __name__ == '__main__':
    main()
