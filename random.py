import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time

class MinimalPublisher(Node):
    def __init__(self):
        super().__init__('minimal_publisher')
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)

    def draw_random(self):
        move = Twist()
        # loop a few times to create pattern
        # not too many to go off window
        for _ in range(5):
            # first move = curve
            # curve is linear and angular velocities at the same time
            move.linear.x = 1.0 
            move.angular.z = 4.0
            self.publisher_.publish(move)
            time.sleep(1.0)
            # second move = opposite curve
            move.linear.x = 1.0
            move.angular.z = -4.0
            self.publisher_.publish(move)
            time.sleep(1.0)

def main(args=None):
    rclpy.init(args=args) #initialize
    node = MinimalPublisher() # create publisher node
    node.draw_random() # call draw_random
    node.destroy_node() # destroy node
    rclpy.shutdown() # shutdown

if __name__ == '__main__':
    main()
