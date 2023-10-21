import pygame
import sys
import random
import math
import os
from pygame import mixer
import sounddevice as sd
import numpy as np
from pydub import AudioSegment
from pydub.playback import play
from pydub.generators import Sine

pygame.init()
pygame.mixer.init()
#sound = pygame.mixer.Sound(r'C:\Users\hp\Downloads\so.wav')
#sound = pygame.mixer.Sound(r'C:\Users\hp\Downloads\coin_c_02-102844.mp3')
#sound = pygame.mixer.Sound(r'C:\Users\hp\Downloads\snd_fragment_retrievewav-14728.mp3')
sound = pygame.mixer.Sound(r'C:\Users\hp\Downloads\whoosh-6316.mp3')

# Set up some constants
WIDTH, HEIGHT = 1500, 700
RECT_WIDTH = 10






heights = []
count = 0
for i in range(150):
    heights.append(random.randint(50, 690))
swapped = [False]*len(heights)
def createArr():
    global heights
    global swapped
    for i in range(300):
        heights.append(random.randint(50, 690))
    swapped = [False] * len(heights)


win = pygame.display.set_mode((WIDTH, HEIGHT))
def playSound(value):
    # Normalize the value to fit inside the volume range
    normalized_value = value / 690 # Assuming max_value is the highest possible value
    channel = pygame.mixer.find_channel(True)

    # Set the sound volume to the normalized value
    sound.set_volume(normalized_value)

    # Play the sound
    channel.play(sound)

    # Wait for a moment
    pygame.time.wait(5)
# swap function with delay
def swap(lst, i, j):
    lst[i], lst[j] = lst[j], lst[i]
    swapped[i] = swapped[j] = True



    pygame.time.wait(50)
def maxHeapify(arr, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2

    # See if left child of root exists and is
    # greater than root

    if l < n and arr[i] < arr[l]:
        largest = l

    # See if right child of root exists and is
    # greater than root

    if r < n and arr[largest] < arr[r]:
        largest = r

    # Change root, if needed

    if largest != i:
        (arr[i], arr[largest]) = (arr[largest], arr[i])  # swap
        swapped[i] = swapped[largest] = True
        display()
        playSound(arr[i])
        playSound(arr[largest])


        #playSound(arr[i])
        #playSound(arr[largest])





        # Heapify the root.

        maxHeapify(arr, n, largest)

def change_volume(value, sound):
    new_volume = (value/100.0) * 60.0 - 60.0  # in dB, adjust as needed
    return sound + new_volume




def display():
    global swapped
    win.fill((0, 0, 0))
    for k, h in enumerate(heights):
        color = (0, 255, 0) if swapped[k] else (0, 0, 255)
        pygame.draw.rect(win, (0,0,0), (k * RECT_WIDTH, HEIGHT - h, RECT_WIDTH, h))
        pygame.draw.rect(win,color , (k * RECT_WIDTH+0.5, HEIGHT - h+0.5, RECT_WIDTH-0.5, h-0.5))
    pygame.display.update()
    swapped = [False] * len(heights)

def selectionSort(arr):
    global swapped
    for i in range(len(arr)):
        minindx = i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[minindx]:
                minindx = j
        swap(arr,i,minindx)
        playSound(arr[i])
        playSound(arr[minindx])


        display()

def merge(a,p,q,r):
    n1 = q-p+1
    n2 = r-q
    L = [0]*(n1+1)
    R = [0] * (n2 + 1)
    for i in range(0,n1):
        L[i] = a[p+i]
    #print(L)
    for i in range(0,n2):
        R[i] = a[q+i+1]
    #print(R)
    L[n1] = math.inf
    R[n2] = math.inf
    i = 0
    j = 0
    k = p
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            a[k] = L[i]
            swapped[k] = swapped[p+i] = True
            playSound(heights[k])
            playSound(heights[p+i])
            display()
            i += 1
        else:
            a[k] = R[j]
            playSound(heights[k])
            playSound(heights[q+j+1])
            swapped[k] = swapped[q + j + 1] = True
            display()
            j += 1
        k += 1

    while i < n1:
        a[k] = L[i]
        i += 1
        k += 1


    while j < n2:
        a[k] = R[j]
        j += 1
        k += 1

def mergeSort(a,p,r):
    if p < r:
        q = math.floor((p+r)/2)
        mergeSort(a,p,q)
        mergeSort(a,q+1,r)
        merge(a,p,q,r)

def insertionSort(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            playSound(arr[j])
            playSound(arr[j+1])
            swapped[j] = swapped[j+1] = True
            display()
            j-=1
        arr[j+1] = key
        display()

def partition(a,p,r):
    x = a[r]
    i = p-1
    for j in range(p,r):
        if a[j] <= x:
            i += 1
            (a[i], a[j]) = (a[j], a[i])
            swapped[i] = swapped[j] = True
            playSound(heights[i])
            playSound(heights[j])
            display()
    (a[i + 1], a[r]) = (a[r], a[i + 1])
    playSound(heights[i+1])
    playSound(heights[r])
    swapped[i+1] = swapped[r] = True
    display()
    return i+1

def quickSort(a,p,r):
    if p < r:
        q = partition(a,p,r)
        quickSort(a,p,q-1)
        quickSort(a,q+1,r)






def heapSort(arr):
    n = len(arr)


    for i in range(n // 2 - 1, -1, -1):
        maxHeapify(arr, n, i)



    for i in range(n - 1, 0, -1):
        (arr[i], arr[0]) = (arr[0], arr[i])
        maxHeapify(arr, i, 0)




# Main loop
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    win.fill((255, 255, 255))

    # Draw rectangles
    display()
    if(count == 0):
        quickSort(heights,0,149)
        createArr()
        #display()
        #selectionSort(heights)


    count+=1
    display()


    pygame.display.update()
