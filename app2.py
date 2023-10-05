import streamlit as st
import os
# import cv2
import numpy as np
from PIL import Image
import zipfile
import io
import base64
from keras.preprocessing.image import ImageDataGenerator

st.set_page_config(
    page_icon='📃',
    initial_sidebar_state="auto",
    layout="wide"
)

# Function to perform image data augmentation
def augment_image(image, num_images, rotation_range, width_shift_range, height_shift_range, shear_range, zoom_range):
    augmented_images = []

    # Create an ImageDataGenerator for augmentation with user-adjustable parameters
    datagen = ImageDataGenerator(
        rotation_range=rotation_range,
        width_shift_range=width_shift_range,
        height_shift_range=height_shift_range,
        shear_range=shear_range,
        zoom_range=zoom_range,
        horizontal_flip=True,
        fill_mode='nearest'
    )

    # Convert the PIL image to a NumPy array
    image_array = np.array(image)
    image_array = image_array.reshape((1,) + image_array.shape)

    # Generate augmented images
    i = 0
    for batch in datagen.flow(image_array, batch_size=1):
        augmented_image = batch[0].astype('uint8')
        augmented_images.append(augmented_image)
        i += 1
        if i >= num_images:
            break

    return augmented_images

# Streamlit app
def main():
    st.title("Image Data Augmentation App 📝📝")
    st.sidebar.image("im5.webp", use_column_width=True)
    st.sidebar.title("Instructions")

    st.sidebar.markdown(
        """
        1. Upload an image by clicking on the "Upload an image" button.
        2. Adjust the data augmentation parameters as needed.
        3. Specify the number of augmented images you want to generate.
        4. Click the "Download Augmented Images (ZIP)" button to generate and download the augmented images in a ZIP file.

        You can fine-tune the augmentation parameters to customize the image augmentation.
        """
    )
    

    # Upload an image
    uploaded_image = st.file_uploader("Step 1: Upload an image", type=["jpg", "png", "jpeg"])

    if uploaded_image is not None:
        image = Image.open(uploaded_image)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        # Adjust data augmentation parameters
        rotation_range = st.slider("Step 2: Rotation Range", 0, 360, 40)
        width_shift_range = st.slider("Width Shift Range", 0.0, 1.0, 0.2)
        height_shift_range = st.slider("Height Shift Range", 0.0, 1.0, 0.2)
        shear_range = st.slider("Shear Range", 0.0, 1.0, 0.2)
        zoom_range = st.slider("Zoom Range", 0.0, 1.0, 0.2)

        # Input number of images to generate
        num_images = st.number_input("Step 3: Enter the number of images to generate", min_value=1, value=10)

        # Perform data augmentation
        augmented_images = augment_image(image, num_images, rotation_range, width_shift_range, height_shift_range, shear_range, zoom_range)

        # Create a ZIP file containing augmented images
        if st.button("Step 4: Download Augmented Images (ZIP)"):
            with st.spinner("Generating augmented images..."):
                zip_buffer = io.BytesIO()
                with zipfile.ZipFile(zip_buffer, "w") as zipf:
                    for i, augmented_image in enumerate(augmented_images):
                        augmented_image = Image.fromarray(augmented_image)
                        img_byte_array = io.BytesIO()
                        augmented_image.save(img_byte_array, format="PNG")
                        zipf.writestr(f"augmented_image_{i}.png", img_byte_array.getvalue())

                # Provide a download link for the ZIP file
                zip_buffer.seek(0)
                st.markdown(
                    f'<a href="data:application/zip;base64,{base64.b64encode(zip_buffer.read()).decode()}" download="augmented_images.zip">Download Augmented Images (ZIP)</a>',
                    unsafe_allow_html=True,
                )
                st.success("Your Image has been Augmented successfully")
                st.balloons()

if __name__ == "__main__":
    main()
