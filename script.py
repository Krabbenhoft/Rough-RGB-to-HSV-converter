import statistics
import math
import colorsys
import random
import tkinter as tk
from tkinter import *


def rgbToHex (colors):
    redPart = str(hex(colors[0]))
    redPart2 = redPart[2:]
    if len(redPart2) == 1:
        redPart3 = "0" + redPart2
    else:
        redPart3 = redPart2
    print(str(colors[0]) + " redpart: " + redPart + " redpart2 " + redPart2)

    bluePart = str(hex(colors[1]))
    bluePart2 = bluePart[2:]
    if len(bluePart2) == 1:
        bluePart3 = "0" + bluePart2
    else:
        bluePart3 = bluePart2
    print(str(colors[1]) + " bluepart: " + bluePart + " bluepart2 " + bluePart2)

    greenPart = str(hex(colors[2]))
    greenPart2 = greenPart[2:]
    if len(greenPart2) == 1:
        greenPart3 = "0" + greenPart2
    else:
        greenPart3 = greenPart2
    print(str(colors[2]) + " greenPart: " + greenPart + " greenPart2 " + greenPart2)

    return "#" + redPart3 + bluePart3 + greenPart3
def favoredAngle(larger, smaller):
    sum = larger + smaller
    favoredByPercentage = (larger/sum) * 100
    print("Favored by percentage: " + str(favoredByPercentage-60))
    favoredByAngleOffset = favoredByPercentage * 1.2
    if (favoredByPercentage-60) > 0:
        favoredByPercentage = favoredByPercentage * (math.log(favoredByPercentage-60) + 1)
    favoredByPercentage = min(favoredByPercentage, 120)
    return favoredByAngleOffset

def rgbToHsv(red, green, blue):
    # calculate value
    value = (max(red, green, blue) / 2.55)

    # calculate saturation
    biggestPair = max([red + green, red + blue, blue + green])
    colorSum = red + green + blue
    saturation = (biggestPair/colorSum) * 100

    # calculate hue
    # find largest two colors
    # if dealing with RED and GREEN
    if blue <= red and blue <= green:
        if red >= green:
            greenStartAngle = 120
            hue = greenStartAngle - favoredAngle(red, green)
        else:
            print(favoredAngle(green, red))
            hue = favoredAngle(green, red)
    # if dealing with RED and BLUE
    elif green < red and green < blue:
        if red >= blue:
            blueStartingAngle = 180;
            hue = blueStartingAngle + favoredAngle(red, blue)
        else:
            redStartingAngle = 360
            hue = redStartingAngle - favoredAngle(blue, red)
    # if dealing with BLUE and GREEN
    else:
        if blue >= green:
            greenStartingAngle = 120
            hue = greenStartingAngle + favoredAngle(blue, green)
        else:
            blueStartingAngle = 240
            hue = blueStartingAngle - favoredAngle(green, blue)

    return [round(hue), round(saturation), round(value)]



root = Tk()
root.title("Accuracy tester")
rowIndex = 1
while rowIndex < 6:
    colIndex = 1
    redSeed = math.floor(random.random() * 255)
    greenSeed = math.floor(random.random() * 255)
    blueSeed = math.floor(random.random() * 255)

    while colIndex < 4:
        colorFrame = tk.Frame(master=root, width = 500, height = 500, borderwidth=2)
        colorFrame.grid(row = rowIndex, column = colIndex)

        # middle
        if colIndex % 3 == 2:
            label = tk.Label(master=colorFrame, text="\n     →     \n")
            label.pack()

        #first
        elif colIndex % 3 == 1:
            label = tk.Label(master=colorFrame, bg=rgbToHex([redSeed, greenSeed, blueSeed]), text="\n           \n")
            label.pack()

        #converted
        else:
            label = tk.Label(master=colorFrame, text="\n           \n")
            rawHsv = rgbToHsv(redSeed, greenSeed, blueSeed)

            print ("#####" + str(rawHsv[0]), str(rawHsv[1]), str(rawHsv[2]))

            newRgb = colorsys.hsv_to_rgb(rawHsv[0]/350, rawHsv[1]/100, rawHsv[2]/100)

            print("\n\n\n VERY IMPORTANT")
            print(newRgb)
            print("\n\n\n")
            integerNewRgb = [round(newRgb[0]*255), round(newRgb[1]*255), round(newRgb[2]*255)]

            textNewRgb = rgbToHex(integerNewRgb)
            label.configure(bg=textNewRgb)
            label.pack()

        colIndex = colIndex + 1
    rowIndex = rowIndex + 1

root.mainloop()
