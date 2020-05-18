import matplotlib.pyplot as plt
import cv2, sys
from motion_blur.libs.nn.motion_net import MotionNet
from motion_blur.libs.forward_models.functions import *
from motion_blur.libs.nn.train import train


if __name__ == "__main__":
    # PARAMETERS
    NAngles = 100
    L = 15
    nb_epoch = 2000

    # Argument parser
    net = MotionNet()

    # Train
    train(net)