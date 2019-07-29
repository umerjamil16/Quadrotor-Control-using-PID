# Quadrotor Control using PID
In this project, I implemented a PID controller within a ROS node to control a quadcopter in a Unity 3D environment

First, download the Unity simulator for your host computer OS [here](https://github.com/udacity/RoboND-Controls-Lab/releases). Before launching the simulator, change the ros_settings.txt file of the simulator to following:
```sf
{
	"vm-ip" : ROS_HOST_IP,
	"vm-port" : PORT,
	"vm-override" : true,
	"host-ip": "192.168.0.21",
	"host-override" : true
}
```
Afterwards, launch the simulator file. To fly the quad around the simulator without using your controller, simply click the “Input On” button in the lower left-hand corner. To get a list of the key commands that will allow you to fly around with local input turned on.

_Note 01_: You must first run `roscore`. If you don't run `roscore`, the
simulator will still run, but you will not be able to communicate
with it via ROS.
_Note 02_: When local input is enabled, force commands from ROS will be ignored. Make sure that it’s not enabled while you are testing your flight controllers.

### Hover Controller node ###
The simplest controller in the `quad_controller` package is the hover
controller node. It is nothing more than a simple PID controller that sets
applies a vertical thrust vector to the quad rotor body.

#### Running the hover controller node ####

```sh
$ rosrun quad_controller hover_controller_node
```
**Hover controller parameter tuning:**
The easiest way to tune the hover controller's PID parmaeters
or set the target position is to use ROS' dynamic reconfigure.

To run dynamic reconfigure:
```sh
$ rqt_reconfigure
```

If `hover_controller_node` is running you should now be able
to interactively explore the hover controller.

**Plotting Altitude**
One simple way to plot the altitude is to use `rqt_plot`. 

```sh
$ rqt_plot /quad_rotor/pose/pose/position/z
```
To try out the Ziegler–Nichols tuning method , use either `hover_zn_tuner_node`, or `hover_twiddle_tuner_node`.

To run `hover_zn_tuner_node`:
```
$ rosrun quad_controller hover_zn_tuner_node
```

To run `twiddle_tuner_node`:
```
$ rosrun quad_controller hover_twiddle_tuner_node
```
_Note_: ZN and Twiddle Tuner nodes only work with the Hover Controller, they will not function correctly with the Attitude Controller.

### Attitude Controller node
The attitude controller is responsible for controlling the roll, pitch, and yaw angle of the quad rotor. To launch it, run
```
$ roslaunch quad_controller attitude_controller.launch
```

Tune roll and pitch PID parmaeters until things look good.

### Position Controller 

The positional controller is
responsible for commanding the attitude and thrust vectors in order to acheive a
goal orientation in three dimensional space., To launch, run

```
$roslaunch quad_controller position_controller.launch
```

Tune parameters until the controller is well-behaved.
