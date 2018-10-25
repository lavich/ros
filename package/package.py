from __future__ import print_function
import os

import roslibpy

ros = roslibpy.Ros(host=os.environ.get('ROS_BRIDGE_URI'), port=9090)
ros.on_ready(lambda: print('Is ROS connected?', ros.is_connected))
print('start')
ros.run_forever()
print('end')
