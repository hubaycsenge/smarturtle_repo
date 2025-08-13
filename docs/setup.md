# SmarTurtle setup guide 

## Items needed 
	1. TurtleBot3 with components + SD card
	2. Jetson Nano + SD card
	3. Ethernet access for Jetson Nano
	4. Ethernet cable to connect the Raspberry PI with the Jetson Nano
## I. TurtleBot3 setup 

1. Follow through the original TurtleBot3 quick start guide](https://emanual.robotis.com/docs/en/platform/turtlebot3/quick-start/)
2. Set a static IP address for eth0 port in TurtleBot3 SBC

		```console
		$ sudo nano /etc/netplan/50-cloud-init.yaml
		```

		The file should be edited to this:
		<span style="color:red">#TODO</span>
		```console
		$ sudo netplan apply
		```

## II. Jetson Nano setup

1. Follow through the original [Jetson Nano Developer Kit setup guide](https://developer.nvidia.com/embedded/learn/get-started-jetson-nano-devkit)
2. Insert ethernet
3. Install [ROS2 Dashing Diademata](https://docs.ros.org/en/dashing/Installation.html)
4. Get the TurtleBot3 dependencies
		```console
		$ sudo apt install python3-argcomplete python3-colcon-common-extensions libboost-system-dev build-essential
		$ sudo apt install ros-dashing-hls-lfcd-lds-driver
		$ sudo apt install ros-dashing-turtlebot3-msgs
		$ sudo apt install ros-dashing-dynamixel-sdk
		$ sudo apt install ros-dashing-xacro
		$ sudo apt install libudev-dev
		```
5. Install LeRobot framework 
     ```console
		$ micromamba create env --name robotenv python=3.12 torchvision=0.21.0
		$ micromamba acivate robotenv
		$ micromamba install av=15.0.0 -c conda-forge #else pip install's av install throws error of not being within venv
		$ pip install lerobot
		```
6. Edit .bashrc 
		```console
		$ echo 'micromamba activate robotenv' >> ~/.bashrc 
		$ echo 'export PYTHONPATH =/home/$USER/micromamba/envs/robotenv/lib/python3.12/site-packages #so that ROS2 recognises the LeRobot package' >> ~/.bashrc
		$ echo 'export ROS_DOMAIN_ID=30 #TURTLEBOT3' >> ~/.bashrc
		$ echo 'source /opt/dashing/setup.sh' >> ~/.bashrc
		```
7. Setup static IP address for eth0 port

		Disconnect the ethernet cable from the built-in port of the Nano
		```console
		$ sudo nano /etc/netplan/01-netconfig.yaml
		```

		The file should be edited to this:
		<span style="color:red">#TODO</span>
		```console
		$ sudo netplan apply
		```
		Connect the Jetson Nano and the Raspberry PI via an ethernet cable 
		<span style="color:red"> IMPORTANT:</span> You want to connect the Jetson Nano with the TurtleBot3's PI device via Eth0 which are supposed to be the <span style="color:red"> built-in</span> ports of the devices. If an ethernet to USB adapter is connected during system boot it may get the static IP, preventing communication with the Turtebot. It is therefore advised to insert the USB adapter with the internet access after booting the two devices. From this step on, internet access of the Jetson  Nano is solved via an USB to ethernet adapter and/or a USB wifi dongle