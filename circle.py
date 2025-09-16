import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time

class MinimalPublisher(Node):
    def __init__(self):
        super().__init__('minimal_publisher')
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)

    def draw_circle(self):
        move = Twist()
        #loop to approximate circle with 13 sides
        for _ in range(13):
            # move in line with velocity 0.8
            move.linear.x = 0.8
            move.angular.z = 0.0
            time.sleep(2.0)
            self.publisher_.publish(move)
            # Rotate with angular velocity 0.5
            move.linear.x = 0.0
            move.angular.z = 0.5
            time.sleep(2.0)
            self.publisher_.publish(move)

def main(args=None):
    rclpy.init(args=args) #initialize
    node = MinimalPublisher() # create publisher node
    node.draw_circle() # call draw_circle
    node.destroy_node() # destroy node
    rclpy.shutdown() # shutdown

if __name__ == '__main__':
    main()
