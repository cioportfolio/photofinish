# The Secret Message Challenge #

There is a secret message being scrolled through a single strip of LEDS. You can see the lights changing but you can't make out what the message is saying. You can use computer vision to help.

## Get some computer vision tools ##
For this challenge we can use some computer vision tools called "OpenCV". This can work with lots of programing languages, including Python.

The are many online tutorials for working with OpenCV. First we need to install the OpenCV software. You can search for your own instructions or you can try these:

### Install OpenCV on a Raspberry Pi ###
[Raspberry Pi Guide](https://raspberrypi-guide.github.io/programming/install-opencv)

### Install OpenCV on a Windows PC ###
[Geeks for geeks Guide](https://www.geeksforgeeks.org/how-to-install-opencv-for-python-in-windows/)

## Practice with OpenCV ##

OpenCV can do all sorts of things with images and videos. You can try out lots of examples in the tutorials. You can search for you own examples or try some of the ones in [Geeks for Geeks](https://www.geeksforgeeks.org/opencv-python-tutorial/?ref=lbp).

Look for:

- cutting out and showing part of an image
- showing a video
- capturing a video from a camera

## Start using OpenCV to beat the challenge ##

1. Capture a video of the LED strip with a camera
2. Process the video so that you can work on it one frame at a time
3. Take each frame and cut out a tall thin section, only a few pixels wide, which contains the LED strip but not much of the surroundings.
4. Make a new image (it might be very wide) by placing the tall thin sections side-by-side
5. Show the new image you have made
6. If necessary repeat the steps and make adjustments until you can read the message. Some of the adjustments you might need to try:

    - re-record the video making sure the LED strip is a vertical as possible
    - change the shape of the tall thin section so that you capture the changing LEDs and not the static surroundings
    - change the width of the tall thin section so your final image is readable
    - change the order of the sections (right to left or left to right) so the words appear the right way round.

## Think about what you have made ##

If you can read the secret message, Well Done! You have completed the first part of the challenge but you have also made something really useful - a photofinish device. These devices are used in major sporting events. Take a look at [this video]()