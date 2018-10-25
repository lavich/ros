import time
import os

from roslibpy import Ros

host = os.environ.get('ROS_BRIDGE_URI')
port = 9090
url = u'ws://%s:%d' % (host, port)


def run_rosapi_topics(*args, **kwargs):
    ros_client = Ros(*args, **kwargs)

    def callback(topic_list):
        print(topic_list)
        assert('/rosout' in topic_list['topics'])
        time.sleep(1)
        ros_client.terminate()

    def get_topics():
        ros_client.get_topics(callback)

    ros_client.on_ready(get_topics)
    ros_client.run_forever()


if __name__ == '__main__':
    import logging

    logging.basicConfig(level=logging.DEBUG, format='[%(thread)03d] %(asctime)-15s [%(levelname)s] %(message)s')
    LOGGER = logging.getLogger('test')

    run_rosapi_topics(host, port)