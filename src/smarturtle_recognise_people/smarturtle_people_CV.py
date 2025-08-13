from lerobot.cameras.opencv.configuration_opencv import OpenCVCameraConfig
from lerobot.cameras.opencv.camera_opencv import OpenCVCamera
from lerobot.cameras.configs import ColorMode, Cv2Rotation

from ultralytics import YOLO

import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class PersonPublisher(Node):
    def __init__(self, config):
        super().__init__("smarturtle_recognise_people")
        self.publisher_ = self.create_publisher(String, "topic", 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.model = YOLO("yolo11n.pt")
        self.i = 0
        # Instantiate and connect an `OpenCVCamera`, performing a warm-up read (default).
        self.camera = OpenCVCamera(config)
        self.camera.connect()

    def timer_callback(self):
        frame = self.camera.async_read(timeout_ms=200)
        msg = String()
        results = self.model(frame)
        msg.data = f"Bboxes: {results[0].boxes.xywh}, Classes:{results[0].boxes.cls}"
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)
        self.i += 1


def main(args=None):
    rclpy.init(args=args)

    # Construct an `OpenCVCameraConfig` with your desired FPS, resolution, color mode, and rotation.
    config = OpenCVCameraConfig(
        index_or_path=0,
        fps=30,
        width=640,
        height=480,
        color_mode=ColorMode.RGB,
        rotation=Cv2Rotation.NO_ROTATION,
    )

    publishernode = PersonPublisher(config)
    print("Hi from smarturtle_recognise_people.")
    rclpy.spin(publishernode)

    person_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
