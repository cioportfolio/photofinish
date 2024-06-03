
import time
import math
import colorsys
import pygame
import sys
import numpy as np
import os

# If you find you need better contrast this array can be used to adjust the raw colour values for a typical LED gamma e.g. new_val=gamma8[raw_val]
gamma8 = [
    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  1,  1,  1,
    1,  1,  1,  1,  1,  1,  1,  1,  1,  2,  2,  2,  2,  2,  2,  2,
    2,  3,  3,  3,  3,  3,  3,  3,  4,  4,  4,  4,  4,  5,  5,  5,
    5,  6,  6,  6,  6,  7,  7,  7,  7,  8,  8,  8,  9,  9,  9, 10,
   10, 10, 11, 11, 11, 12, 12, 13, 13, 13, 14, 14, 15, 15, 16, 16,
   17, 17, 18, 18, 19, 19, 20, 20, 21, 21, 22, 22, 23, 24, 24, 25,
   25, 26, 27, 27, 28, 29, 29, 30, 31, 32, 32, 33, 34, 35, 35, 36,
   37, 38, 39, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 50,
   51, 52, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 66, 67, 68,
   69, 70, 72, 73, 74, 75, 77, 78, 79, 81, 82, 83, 85, 86, 87, 89,
   90, 92, 93, 95, 96, 98, 99,101,102,104,105,107,109,110,112,114,
  115,117,119,120,122,124,126,127,129,131,133,135,137,138,140,142,
  144,146,148,150,152,154,156,158,160,162,164,167,169,171,173,175,
  177,180,182,184,186,189,191,193,196,198,200,203,205,208,210,213,
  215,218,220,223,225,228,231,233,236,239,241,244,247,249,252,255
]

pygame.init()

pScale = 5 # size of pixels drawn to illustrate the generated immage
pRad = int(pScale/2)
matrixHeight = 32 # number of LEDs that will be used in the strip
# font = 'Harabara Mais Demo.otf' # path and name of font file to be used
# myfont = pygame.font.Font(font, matrixHeight-4)
# myfont.italic=True
# myfont.bold=True
black = (0,0,0)
white = (255,255,255)

def buildMessage(name, imagefile, background):
    buildMessages(name, [(imagefile, background)])

def buildMessages(name, msglist):
    os.environ['SDL_VIDEO_WINDOW_POS'] = "0,0"
    screen = pygame.display.set_mode((matrixHeight * pScale, matrixHeight * pScale))
    res = np.zeros((0,matrixHeight,3), dtype=np.uint8)
    totw = 0
    for (imagefile, background) in msglist:
        imgsurface = pygame.image.load(imagefile).convert_alpha()
        imageHeight = imgsurface.get_height()
        imageWidth = imgsurface.get_width()
        scale = matrixHeight/imageHeight
        newWidth = int(scale*imageWidth)
        newsurface = pygame.transform.smoothscale(imgsurface, (newWidth, matrixHeight))
        totw+=newWidth
        leds = pygame.Surface((newWidth, matrixHeight),pygame.SRCALPHA, screen)
        leds.blit(newsurface, (0,0))
        res = np.concatenate((res,pygame.surfarray.pixels3d(leds)), axis=0)
    screen = pygame.display.set_mode((totw * pScale, matrixHeight * pScale))
    screen.fill(black)
    defFile  = open(name+".py", "w")
    defFile.write("message_data=[]\n")
    for x in range(totw):
            defFile.write("message_data.append([")
            for y in range(matrixHeight):
                    pygame.draw.circle(screen, (res[x,y,0],res[x,y,1],res[x,y,2]),[int(x * pScale + pRad), int(y * pScale + pRad)], pRad)
                    if y > 0:
                        defFile.write(", ")
                    hcol = (res[x,y,0] << 16) | (res[x,y,1] << 8) | (res[x,y,2])
                    defFile.write(hex(hcol))
            defFile.write("])\n")
    defFile.close()
    pygame.display.flip()
        
buildMessages("message",[("R2T_1.png",(255,255,255)),("R2T_2.png", (255,255,255))]) # change the images and background RGB as required
