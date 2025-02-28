import rclpy
from g_stream.param_dump_manager import param_loader
from rclpy.context import Context

def test_param_loader():
    rclpy.init()
    node = rclpy.create_node("test_node")
    param_loader(node, "/workspace/src/g_stream/config/test.yaml")

    param_names = node.([], depth=1).names
    for param in node.get_parameters([]):
        node.get_logger().warning("dddddddddddddddddddddddddddddddddddd")
        print(param.name)

    print("00000000000000000000000000000000000000000000000000000099999999999999999999")
    node.destroy_node()
    rclpy.shutdown()

    assert False
