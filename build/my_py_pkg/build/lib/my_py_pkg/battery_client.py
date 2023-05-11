#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

class BatteryClientNode(Node):
    def __init__(self):
        super().__init__("battery_client") 


def main(args=None):
    rclpy.init(args=args) 
    node = BatteryClientNode() 
    rclpy.spin(node)
    rclpy.shutdown()

if __name__== "__main__":
    main()