# STREAMLIT_DEMO


## Getting Started

Some scripts testing out the streamlit app

- First_app.py                        shows a bunch of streamlit objects thrown onto the website 
- take_a_picture.py                   draws boundries around a still photo taken on the webcam (or what ever is the default camera)
- open_cv_face_detection _video.py    is simular take_a_picture.py but shows it in a live  video
haarcascades folder                 has different opencv face detection parameters 
aruco_demo.py                       a quick demo find aruco items 

The openCV was taken from this article : https://towardsdatascience.com/computer-vision-for-beginners-part-3-79de62dbeef7 and her git page : https://github.com/jjone36/vision_4_beginners

<br>
<br>

### Installing streamlit on 64bit Raspberry PI OS using conda - 

confirmed working on:
Raspberry Pi 4 Model B 4 Gb RAM


<br>
<br>
Followed the instructions on the post here : https://discuss.streamlit.io/t/raspberry-pi-streamlit/2900/43

Streamlit wont installed on 32bit Raspbian due to supported libraries.  We will use the ARM64 (the usual as of writing this is 32bit raspbian) which is still in beta but does work.  The 64bit version is also recomended for open CV due to speed.  Streamlit also recomends using conda to install its package ( it wont work otherwise), it also makes opencv easier too.  This was installed on a Raspberry Pi 4 Model B 4 Gb RAM.  
<br><br>

Instructions below:

- $ wget https://github.com/Archiconda/build-tools/releases/download/0.2.3/Archiconda3-0.2.3-Linux-aarch64.sh 4
- $ chmod +x Archiconda3-0.2.3-Linux-aarch64.sh
- $ ./Archiconda3-0.2.3-Linux-aarch64.sh (takes quite a while)
- $ conda install -c conda-forge streamlit (as @randyzwitch as suggested above)
- Streamlit installs – but does not work yet (I got AttributeError: module ‘google.protobuf.descriptor’ has no attribute '_internal_create_key when I tried to run the streamlit hello app)
- $ conda update conda -y
- $ pip install --upgrade protobuf (this solved: AttributeError: module ‘google.protobuf.descriptor’ …)
- $ pip install --upgrade pip (just for good measure – most likely not required)42 Gb RAM,
- A fresh SD card with 2020-08-20-raspios-buster-arm64-lite.img (I haven’t done any update of raspios because that would just be a waste of time if the Streamlit install should fail)
- $ wget https://github.com/Archiconda/build-tools/releases/download/0.2.3/Archiconda3-0.2.3-Linux-aarch64.sh 4
- $ chmod +x Archiconda3-0.2.3-Linux-aarch64.sh
- $ ./Archiconda3-0.2.3-Linux-aarch64.sh (takes quite a while)
- $ conda install -c conda-forge streamlit (as @randyzwitch as suggested above)
- Streamlit installs – but does not work yet (I got AttributeError: module ‘google.protobuf.descriptor’ has no attribute '_internal_create_key when I tried to run the streamlit hello app)
- $ conda update conda -y
- $ pip install --upgrade protobuf (this solved: AttributeError: module ‘google.protobuf.descriptor’ …)
- $ pip install --upgrade pip (just for good measure – most likely not required)

<br>
<br>

### arUco 
<br>
Arcuo worked using the installation " streamlit on 64bit Raspberry PI OS using conda" above on Raspberry PI.  I imagine it will work on multiple linux versions, just need to make sure archicture version match up, that seams to be a sticking point on this and opencv.
<br>
<br>
It didnt like the following statements.  The images can be loaded into memory.   

cv2.imshow('Display', frame)
if cv2.waitKey(1) & 0xFF == ord('q'):
break

<br>
<br>

### If using the XPT2046 Touch Screen

<br>
<br>

- sudo nano /boot/config.txt
add the following 


```
dtparam=i2c_arm=on
dtparam=spi=on
dtoverlay=ads7846,penirq=25,speed=10000,penirq_pull=2,xohms=150
```


Next Create directory /etc/X11/xorg.conf.d and file 99-calibration.conf in that directory

```
sudo mkddir /etc/X11/xorg.conf.d 
sudo nano /etc/X11/xorg.conf.d/99-calibration.conf
```

Add the following into the file

```
Section "InputClass"
        Identifier "calibration"
        MatchProduct "ADS7846 Touchscreen"
        Option "Calibration" "3853 170 288 3796"
        Option "SwapAxes" "1"
EndSection
```


## Todo 


### docker installation 

- i couldnt get the following to work on the raspberry pi 

- i might be able to get it to work using the new "streamlit on 64bit Raspberry PI OS using conda" method above.  Just need to use correct base architecture 

Followed instructions here : 
https://phoenixnap.com/kb/docker-on-raspberry-pi

Commands to run : 
```
sudo apt-get update && sudo apt-get upgrade
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker Pi
```

this post : https://discuss.streamlit.io/t/how-to-use-streamlit-in-docker/1067/7  explains how to get streamlit installed on docker 

