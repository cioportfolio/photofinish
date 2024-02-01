
import time
import math
import colorsys
import pygame
import sys

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

pScale = 10 # size of pixels drawn to illustrate the generated immage
pRad = int(pScale/2)
matrixHeight = 32 # number of LEDs that will be used in the strip
font = 'FreeSansBold.ttf' # path and name of font file to be used
myfont = pygame.font.Font(font, matrixHeight-4)
black = (0,0,0)

def buildMessage(text, name, foreground, background):
        screen = pygame.display.set_mode((matrixHeight * pScale, matrixHeight * pScale))
        textsurface = myfont.render(text, True, foreground, background).convert_alpha()
        textWidth = textsurface.get_width()
        print(textWidth)
        screen = pygame.display.set_mode((textWidth * pScale, matrixHeight * pScale))
        leds = pygame.Surface((textWidth, matrixHeight),pygame.SRCALPHA, screen)
        leds.blit(textsurface, (0,int((matrixHeight-textsurface.get_height())/2)))
        res = pygame.surfarray.pixels3d(leds)
        screen.fill(black)
        defFile  = open(name+".py", "w")
        defFile.write("message_data=[]\n")
        for x in range(textWidth):
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
        
buildMessage("Hello     ", "message", (255,255,0),(0,0,0)) # change the message and RGB colours as required
