import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time

class MinimalPublisher(Node):
    def __init__(self):
        super().__init__('minimal_publisher')
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)

    def timer_callback(self):
        rate = 1
        move = Twist()
        for _ in range(2):
            move.linear.x = 1.0  # Move forward
            move.angular.z = 0.0
            self.publisher_.publish(move)
            time.sleep(3.0)
            move.linear.x = 0.0
            move.angular.z = 1.6  # Rotate
            self.publisher_.publish(move)
            time.sleep(3.0)
            move.linear.x = 2.0  # Move forward
            move.angular.z = 0.0
            self.publisher_.publish(move)
            time.sleep(3.0)
            move.linear.x = 0.0
            move.angular.z = 1.6  # Rotate
            self.publisher_.publish(move)
            time.sleep(3.0)

def main(args=None):
    rclpy.init(args=args)
    node = MinimalPublisher()
    node.timer_callback()
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
