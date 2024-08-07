# Image Data Augmentation App 📸✨

Welcome to the **Image Data Augmentation App**! This Streamlit-powered web application allows you to effortlessly augment your images with various transformations, making your dataset more diverse and ready for machine learning tasks. 🚀

## Features

- **Image Upload**: Easily upload your images for augmentation.
- **Customizable Augmentation**: Adjust parameters such as rotation, width and height shifts, shear, and zoom ranges to fit your needs.
- **Download Augmented Images**: Generate multiple augmented images and download them all at once in a ZIP file.

## How It Works

1. **Upload an Image**: Click on the "Upload an image" button to select an image file.
2. **Adjust Parameters**: Use the sliders to set augmentation parameters like rotation, shifts, shear, and zoom.
3. **Specify Quantity**: Enter the number of augmented images you wish to generate.
4. **Download**: Click the "Download Augmented Images (ZIP)" button to get a ZIP file with your augmented images.

## Getting Started

### Prerequisites

- Docker
- Python 3.6 or higher
- Streamlit
- Required libraries listed in `requirements.txt`

### Installation and Running

1. **Clone the Repository**:
   
   ```bash
   git clone https://github.com/Shiv-D-Coder/Gadget-Price-Prediction.git
   cd Gadget-Price-Prediction
    ```
   
2. **Run command**:
   
   ```bash
   streamlit run app2.py
    ```

### Run using docker

Type below command to make Docker image and run it:

   ```bash
   docker build -t image-augmentation-app .
   docker run -p 8501:8501 image-augmentation-app
   ```
This will start the Streamlit app, accessible at http://localhost:8501.

### How to Use

1. Upload an Image: Click the file uploader to select an image.
2. Set Augmentation Parameters: Use the sliders to adjust the augmentation settings.
3. Generate Images: Input the number of images to create and click "Download Augmented Images (ZIP)".
4. Download Your Images: Receive a ZIP file with all your augmented images.     
