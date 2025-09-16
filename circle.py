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
        for _ in range(13):
            move.linear.x = 0.8  # Move forward
            move.angular.z = 0.0
            time.sleep(2.0)
            self.publisher_.publish(move)
            move.linear.x = 0.0
            move.angular.z = 0.5  # Rotate
            time.sleep(2.0)
            self.publisher_.publish(move)

def main(args=None):
    rclpy.init(args=args)
    node = MinimalPublisher()
    node.timer_callback()
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
