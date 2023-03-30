import os

import rclpy
from rclpy.executors import SingleThreadedExecutor
from rclpy.node import Node
from voicevox_ros.voicevox import Voicevox
from voicevox_msgs.srv import Speak

class VoicevoxROS(Node):
    def __init__(self):
        super().__init__('voicevox_node')
        self.declare_parameter('speaker', 0)
        self.srv = self.create_service(Speak, 'speak', self.speak_callback)
        
    def speak_callback(self, request, response):
        speaker = self.get_parameter('speaker').value
        voicevox = Voicevox(speaker=speaker)
            
        try:
            voicevox.speak(request.text)
            response.result = True
        
            return response
            
        except Exception as e:
            self.get_logger().error('voicevox_ros has failed %r' & (e,))
            response.result = False
            
            return response
        
def main(args=None):
    rclpy.init(args=args)
    try:
        voicevox_ros = VoicevoxROS()
        executor = SingleThreadedExecutor()
        executor.add_node(voicevox_ros)
        
        try:
            executor.spin()
        finally:
            executor.shutdown()
            voicevox_ros.destroy_node()
    finally:
        rclpy.shutdown()
        
if __name__ == '__main__':
    main()
