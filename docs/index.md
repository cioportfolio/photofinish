# ![The Secret Message Challenge](photfin.jpg)

At the [TechJam](https://techjam.softwarecornwall.org/) there is a secret message being scrolled through a single strip of LEDS. You can see the lights changing but you can't make out what the message is saying. You can use computer vision to help. You can use this video to practice on but it doesn't have the same secret message!

![test message](IMG_6230.mp4)

## Get some computer vision tools

For this challenge we can use some computer vision tools called "OpenCV". This can work with lots of programing languages, including Python.

The are many online tutorials for working with OpenCV. First we need to install the OpenCV software. You can search for your own instructions or you can try the examples below. The instructions usually include some steps to do a quick check that things are working. Skipping these steps is not a good idea. They don't take very long to do and, if there is a problem, it will save you from wasting loads of time and frustration later on:

### Install OpenCV on a Raspberry Pi

[Raspberry Pi Guide](https://raspberrypi-guide.github.io/programming/install-opencv)

### Install OpenCV on a Windows PC

[Geeks for geeks Guide](https://www.geeksforgeeks.org/how-to-install-opencv-for-python-in-windows/)

## Practice with OpenCV

OpenCV can do all sorts of things with images and videos. To solve this challenge you will need to use several different bits of OpenCV together. First you need to get some practice and see how things work. You can try out lots of examples in the tutorials and they may give you more ideas for you own projects and challenges. You can search for you own examples or try some of the ones in [Geeks for Geeks](https://www.geeksforgeeks.org/opencv-python-tutorial/?ref=lbp).

Things to practice:

- cutting out and showing part of an image
- showing a video
- capturing a video from a camera

## Optional extra: Practice working with arrays

OpenCV helps us with computer vision but the computer isn't "seeing" in the same way that people do. The computer camera senses the light in a scene and records it a loads of colour data and stores that in a block of data called an array. OpenCV does all its clever tricks by moving data around arrays and doing maths on the arrays. You will probably need to use arrays to solve this challenge. It would be good to do some practice with arrays or come back here if you get stuck.

There are loads of tutorials and examples about arrays online. Many of them will mention a tool called "numpy". Search for you own guides or try this [guide on Mattermost](https://mattermost.com/blog/beginners-guide-to-numpy/)

Things to practice:
- make an empty array of a particular shape and size
- investigate the shape and size of arrays
- fill arrays with different types of data
- work with slices and sections of arrays
- combine small arrays into a bigger array

## Start using OpenCV to solve the challenge

1. Capture a video of the LED strip with a camera
2. Process the video so that you can work on it one frame at a time
3. Take each frame and cut out a tall thin section, only a few pixels wide, which contains the LED strip but not much of the surroundings.
4. Make a new image (it might be very wide) by placing the tall thin sections side-by-side
5. Show the new image you have made
6. If necessary repeat the steps and make adjustments until you can read the message. Some of the adjustments you might need to try:

    - re-record the video making sure the LED strip is as vertical as possible
    - change the shape of the tall thin section so that you capture the changing LEDs and not the static surroundings
    - change the width of the tall thin section so your final image is readable
    - change the order of the sections (right to left or left to right) so the words appear the right way round.

## Think about what you have made

If you can read the secret message, Well Done! You have completed the first part of the challenge but you have also made something really useful - a photofinish device. These devices are used in major sporting events. Take a look at [this video](https://www.youtube.com/watch?v=QGNgINohags) for an introduction. You have started to make an app that the presenter describes in his video. Now here are some things to try:

- Set up a pretend race with some friends and use your programme to create a photofinish image of your race. Who won?
- Do some comparison between each tall thin strip. Can you get the computer to tell you when someone crosses the line? This is a kind of motion detection.
- Add a timer. Can you calculate the race time of the winner?
- OpenCV can add text to an image. Can you add times to the photofinish image so you can see how far apart the racers are?
- Add some interaction. Show a marker line on the photofinish and let people move the line (with the mouse or keyboard) and show a more accurate time.
- It can be a little fiddly to place the camera just right at the finish line. Add a setup mode to your programme to help you place the camera at the right point before recording a race.
- Add some sound so that you can press a button and make a sound to start the race and use the photofinish to get an accurate time.
- You've already seen how you can insert a hidden message into the photofinish image. That was how you read the secret message. Can you make your own image and make a device to show it at the finish line so that it appears in the photofinish image?
