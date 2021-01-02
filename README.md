# STREAMLIT_DEMO


## Getting Started

Some scripts testing out the streamlit app

First_app.py                        shows a bunch of objects thrown onto the website 
take_a_picture.py                   draws boundries around a still photo teken on the webcam (or what ever is the default camera)
open_cv_face_detection _video.py    is simular take_a_picture.py but shows it in a video 
haarcascades folder                 has different opencv face detection parameters 


The openCV was taken from this article : https://towardsdatascience.com/computer-vision-for-beginners-part-3-79de62dbeef7 and her git page : https://github.com/jjone36/vision_4_beginners



### Installing Streamlit on a Raspberry PI 

Streamlit wont install using the pip as of 31/12/2020, it results in a error, it has to be installed through mini conda 


I followed the instructions here : https://gist.github.com/simoncos/a7ce35babeaf73f512be24135c0fbafb which are: 

wget http://repo.continuum.io/miniconda/Miniconda3-latest-Linux-armv7l.sh
sudo md5sum Miniconda3-latest-Linux-armv7l.sh # (optional) check md5
sudo /bin/bash Miniconda3-latest-Linux-armv7l.sh # -> change default directory to /home/pi/miniconda3
sudo nano /home/pi/.bashrc # -> add: export PATH="/home/pi/miniconda3/bin:$PATH"
sudo reboot -h now

Once conda is installed, i followed :  https://stackoverflow.com/questions/39371772/how-to-install-anaconda-on-raspberry-pi-3-model-b/56852714#56852714 and ran the commands below to install the latest python package

conda config --add channels rpi
conda install python=3.6


Then i created a seperated enviorment to install conda using the commands below (followed instructions here: https://discuss.streamlit.io/t/install-streamlit-with-anaconda/714/4)

conda create -y -n streamlit python=3.7
conda activate streamlit
pip install streamlit

Other useful resources are :

step by step guide to installing conda : https://www.anegron.site/2020/06/18/how-to-install-conda-and-docker-on-your-raspberry-pi/
installing streamlit in conda : https://anaconda.org/conda-forge/streamlit


### arUco 

not completed this one yet but might be worth install through conda mini.  I had trouble installing on windows, it might be corrected by following https://stackoverflow.com/questions/45972357/python-opencv-aruco-no-module-named-cv2-aruco:

"So I uninstalled opencv-python using

pip uninstall opencv-python
Run the program and same error. Then I uninstalled opencv-contrib-python

pip uninstall opencv-contrib-python
After that I reinstalled opencv-contrib-python using

pip install opencv-contrib-python
And run the program, no error now. So I upvoted both the above answers :)"



or installing conda mini: 

https://anaconda.org/conda-forge/opencv
/python-opencv-aruco-no-module-named-cv2-aruco


# docker installation 

Followed instructions here : 
https://phoenixnap.com/kb/docker-on-raspberry-pi

Commands to run : 

sudo apt-get update && sudo apt-get upgrade
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker Pi

this post : https://discuss.streamlit.io/t/how-to-use-streamlit-in-docker/1067/7  explains how to get streamlit installed on docker 


### If using the XPT2046 Touch Screen

sudo nano /boot/config.txt
add

"dtparam=i2c_arm=on
dtparam=spi=on
dtoverlay=ads7846,penirq=25,speed=10000,penirq_pull=2,xohms=150"

Next Create directory /etc/X11/xorg.conf.d and file 99-calibration.conf in that directory
Add the following into the file

"Section "InputClass"
        Identifier "calibration"
        MatchProduct "ADS7846 Touchscreen"
        Option "Calibration" "3853 170 288 3796"
        Option "SwapAxes" "1"
EndSection"

