import os
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
from utility import *

# Define paths
dir_path = r"C:\Users\rashi\OneDrive\Desktop\Underwater-image-enhancement\Underwater-image-enhancement-\images"
results_path = r"C:\Users\rashi\OneDrive\Desktop\Underwater-image-enhancement\Underwater-image-enhancement-\results"

# Create results directory if it doesn't exist
if not os.path.exists(results_path):
    os.makedirs(results_path)

# Process single image if needed
single_image_path = r"C:\Users\rashi\OneDrive\Desktop\Underwater-image-enhancement\Underwater-image-enhancement-\1.png"
if os.path.exists(single_image_path):
    img = cv.imread(single_image_path)
    if img is not None:
        print(f"Processing single image: {single_image_path}")
        nuce_img = NUCE(img)
        cv.imwrite(os.path.join(results_path, "1_enhanced.png"), nuce_img)
        
        # Display results
        plt.figure(figsize=(12, 6))
        plt.subplot(1, 2, 1)
        plt.title("Original Image")
        plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))
        plt.axis('off')
        
        plt.subplot(1, 2, 2)
        plt.title("Enhanced Image")
        plt.imshow(cv.cvtColor(nuce_img, cv.COLOR_BGR2RGB))
        plt.axis('off')
        
        plt.tight_layout()
        plt.savefig(os.path.join(results_path, "single_result.jpg"))
        plt.show()

# Process entire directory
original_images = []
NUCE_images = []

if os.path.exists(dir_path) and os.path.isdir(dir_path):
    print(f"Processing images in directory: {dir_path}")
    for im in os.listdir(dir_path):
        if im.lower().endswith(('.png', '.jpg', '.jpeg')):
            img_path = os.path.join(dir_path, im)
            img = cv.imread(img_path)
            if img is not None:
                original_images.append(img)
                
                print(f"Enhancing image: {im}")
                nuce_img = NUCE(img)
                NUCE_images.append(nuce_img)
                
                cv.imwrite(os.path.join(results_path, im), nuce_img)

    # Display multiple results if any
    if len(original_images) > 0:
        fig, ax = plt.subplots(min(4, len(original_images)), 2, figsize=(8, 10))
        ax[0][0].set_title("Original Images")
        ax[0][1].set_title("Enhanced Images")
        
        for i in range(min(4, len(original_images))):
            ax[i][0].imshow(cv.cvtColor(original_images[i], cv.COLOR_BGR2RGB))
            ax[i][1].imshow(cv.cvtColor(NUCE_images[i], cv.COLOR_BGR2RGB))
            ax[i][0].axis('off')
            ax[i][1].axis('off')
            
        fig.tight_layout()
        plt.savefig(os.path.join(results_path, "output.jpg"))
        plt.show()

print('Processing complete!')