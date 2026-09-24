import math
import numpy as np
from MyConvolution import convolve

def makeGaussianKernel(sigma: float) -> np.ndarray: 
    size = int(8 * sigma + 1)
    if size%2==0:
        size+=1
    gaussian_kernel=np.zeros((size,size))
    center=size//2
    for i in range(size):
        for j in range(size):
            x,y=i-center,j-center
            gaussian_kernel[i][j]=(math.exp(-(x*x+y*y)/(2*sigma*sigma)))/(2*math.pi*sigma*sigma)
    gaussian_kernel /= np.sum(gaussian_kernel)
    return gaussian_kernel

def myHybridImages(lowImage: np.ndarray, lowSigma: float, highImage: np.ndarray, highSigma: float) -> np.ndarray: 

    low_kernel=makeGaussianKernel(lowSigma)
    high_kernel=makeGaussianKernel(highSigma)

    low_filtered=convolve(lowImage,low_kernel)

    blured_high=convolve(highImage,high_kernel)
    high_filtered=highImage-blured_high

    # float, because the high-pass part has negative values and the sum can go past 255
    hybrid_image=np.zeros_like(lowImage, dtype=float)
    for i in range(lowImage.shape[0]):
        for j in range(lowImage.shape[1]):
            hybrid_image[i][j]=low_filtered[i][j]+high_filtered[i][j]
    return hybrid_image