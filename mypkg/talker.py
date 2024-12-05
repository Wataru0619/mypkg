import rclpy
from rclpy.node import Node
from person_msgs.srv import Query

class Talker(Node):
    def __init__(self):
        supper().__init__("talker")
        self.pub = self.create_publisher(Int16, "countup", 10)
        self.create_timer(0.5, self.cb)
        self.n = 0
    def cd(self):
        msg = Int16()
        msg.data = self.n
        self.pub.publish(msg)
        self.n += 1

def main():
    rclpy.init()
    node = Talker()
    rclpy.spin(node)

