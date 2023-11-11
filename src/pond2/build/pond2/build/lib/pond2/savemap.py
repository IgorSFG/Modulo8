import rclpy
from rclpy.node import Node
import sys
import termios
import tty
import os
import threading

class CustomTeleopNode(Node):
    def __init__(self):
        super().__init__('custom_teleop_node')
        self.get_logger().info("custom_teleop_node_started!")
        
        # Set up a separate thread to listen to keyboard input
        self.input_thread = threading.Thread(target=self.keyboard_listener)
        self.input_thread.daemon = True
        self.input_thread.start()
    
    def keyboard_listener(self):
        # Set the terminal to raw mode to read key presses without pressing enter
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            while True:
                key = sys.stdin.read(1)  # Read one key press at a time
                if key.lower() == 'm':  # Save the map when 'M' is pressed
                    self.save_map()
                elif key == '\x03':  # Handle Ctrl-C for termination
                    break
        
        # Add other key handling here for additional teleop functionality
        except Exception as e:
            self.get_logger().error('Could not read key: %r' % e)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

    def save_map(self):
        self.get_logger().info("Saving the map...")
        map_saver_command = "ros2 run nav2_map_server map_saver_cli -f ~/Code/Modulo8/src/pond2/maps/my-map"
        os.system(map_saver_command)
        self.get_logger().info("Map saved successfully.")
    
    def destroy_node(self):
        # Clean up before shutting down
        self.get_logger().info("Shutting down custom teleop node...")
        super().destroy_node()

def main(args=None):
    rclpy.init(args=args)
    custom_teleop_node = CustomTeleopNode()
    try:
        rclpy.spin(custom_teleop_node)
    except KeyboardInterrupt:
        pass  # Allow a clean exit on Ctrl+C
    finally:
        custom_teleop_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()