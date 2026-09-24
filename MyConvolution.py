import numpy as np

def image_channel_padding(image, kernel):
    image_shape=image.shape
    kernel_shape=kernel.shape
    padding_rows=int(np.floor((kernel_shape[0])/2))
    padding_cols=int(np.floor((kernel_shape[1])/2))
    # float, so images with non-integer values are not rounded down
    padding=np.zeros((image_shape[0]+2*padding_rows, image_shape[1]+2*padding_cols), dtype=float)

    for i in range(image_shape[0]):
        for j in range(image_shape[1]):
            padding[i+padding_rows][j+padding_cols]=image[i][j]
    
    return padding

def convolve_channel(padded_channel, flip_kernel, convolved_A,padded_channel_shape):
    for i in range(padded_channel_shape[0]):
        for j in range(padded_channel_shape[1]):
            sum = 0
            for k in range(flip_kernel.shape[0]):
                for l in range(flip_kernel.shape[1]):
                    if i+flip_kernel.shape[0]-1 >= padded_channel_shape[0] or j+flip_kernel.shape[1]-1 >= padded_channel_shape[1]:
                        break
                    sum +=  padded_channel[i+k][j+l] * flip_kernel[k][l]
            if k==flip_kernel.shape[0]-1 and l==flip_kernel.shape[1]-1:
                convolved_A[i][j]=sum 
    return convolved_A

def convolve(image, kernel): 

    flip_kernel=np.flip(kernel)
    output = np.zeros_like(image, dtype=float)

    if image.ndim == 2:
        padded=image_channel_padding(image, kernel)
        output=convolve_channel(padded,flip_kernel, output, padded.shape)
    else:
        channels=image.shape[2]
        for i in range(channels):
            padded=image_channel_padding(image[:,:,i], kernel)
            output[:,:,i]=convolve_channel(padded,flip_kernel, output[:,:,i], padded.shape)


    return output