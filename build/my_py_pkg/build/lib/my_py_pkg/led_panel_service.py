#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

from my_robot_interfaces.srv import set_led

class LedPanelServerNode(Node):
    def __init__(self):
        super().__init__("set_led_server")
        self.server_ = self.create_service(set_led, "set_led_server", self.callback_set_led)
        self.get_logger().info("Set LED server has been started")

    def callback_set_led(self, request, response):

        if request.led1_status == True:
            response.led1_status_success = True
            response.led1_status_message  = "LED1 is on"
        else:
            response.led1_status_success = False
            response.led1_status_message  = "LED1 is off"

        if request.led2_status == True:
            response.led2_status_success = True
            response.led2_status_message  = "LED2 is on"

        else:
            response.led2_status_success = False
            response.led2_status_message  = "LED2 is off"

        if request.led3_status == True:
            response.led3_status_success = True
            response.led3_status_message  = "LED3 is on"
        else:
            response.led3_status_success = False
            response.led3_status_message  = "LED3 is off"
        
        self.get_logger().info(str(response.led1_status_message) + " , " + 
                               str(response.led2_status_message) + " , " + 
                               str(response.led3_status_message))
        return response

        

def main(args=None):
    rclpy.init(args=args) 
    node = LedPanelServerNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__== "__main__":
    main()