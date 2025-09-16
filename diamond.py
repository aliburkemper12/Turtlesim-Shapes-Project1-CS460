import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time

class MinimalPublisher(Node):
    def __init__(self):
        super().__init__('minimal_publisher')
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)

    def draw_diamond(self):
        move = Twist()
        # initially rotate ~45 degrees to create diamond
        move.linear.x = 0.0
        move.angular.z = 0.8
        self.publisher_.publish(move)
        time.sleep(3.0)
        # create square: 4 equal sides, 90 degree turns
        # initial turn makes it a diamond
        for _ in range(4):
            # move forward
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
    node.draw_diamond() # call draw_diamond
    node.destroy_node() # destroy node
    rclpy.shutdown() # shutdown

if __name__ == '__main__':
    main()
