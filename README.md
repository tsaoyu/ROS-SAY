# ROS-SAY
`ros_say` is a simple ROS package to help your robot speaking out. It uses your system native tts engine that works offline and provides log API in Python.

## Basic Usage

```
rosrun ros_say ros_say_listener
```


## Python API

```python
import ros_say
ros_say.loginfo("Armed")
# also support logdebug, logwarn, logerr, and logfatal

```


## C++

There is no C++ API but you can publish any `std_msgs/String` to the topic `/rossay` and `ros_say` will speak out.


