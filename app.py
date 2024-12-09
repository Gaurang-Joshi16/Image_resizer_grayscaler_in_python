import streamlit as st
from PIL import Image

# Resizing function based on your provided code
def resize_image(input_path, output_path, size):
    try:
        # Open the image
        with Image.open(input_path) as img:
            # Resize the image
            img = img.resize(size)
            # Save the resized image
            img.save(output_path)
            return output_path
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return None

# Grayscale conversion function
def convert_to_grayscale(input_path, output_path):
    try:
        with Image.open(input_path) as img:
            # Convert image to grayscale
            grayscale_image = img.convert("L")
            grayscale_image.save(output_path)
            return output_path
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return None

# Streamlit UI
st.title("Image Resizer and Grayscale Converter")
st.write("This app resizes an image and  You can also convert it to grayscale.")

# Input section
width = st.number_input("Enter the desired width:", min_value=1, value=500)
height = st.number_input("Enter the desired height:", min_value=1, value=600)

uploaded_image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_image:
    input_path = "temp_image.jpg"  # Save the uploaded file as temp_image.jpg
    uploaded_image = Image.open(uploaded_image)
    uploaded_image.save(input_path)

    # Resize option
    if st.button("Resize Image"):
        output_path = "resized_temp_image.jpg"
        resized_path = resize_image(input_path, output_path, (width, height))

        if resized_path:
            st.success(f"Image resized successfully! Saved as `{output_path}`.")

            # Download link for resized image
            with open(resized_path, "rb") as file:
                st.download_button(
                    label="Download Resized Image",
                    data=file,
                    file_name="resized_temp_image.jpg",
                    mime="image/jpeg",
                )

    # Grayscale conversion option
    if st.button("Convert to Grayscale"):
        grayscale_output_path = "grayscale_temp_image.jpg"
        grayscale_path = convert_to_grayscale(input_path, grayscale_output_path)

        if grayscale_path:
            st.success(f"Image converted to grayscale successfully! Saved as `{grayscale_output_path}`.")

            # Download link for grayscale image
            with open(grayscale_path, "rb") as file:
                st.download_button(
                    label="Download Grayscale Image",
                    data=file,
                    file_name="grayscale_temp_image.jpg",
                    mime="image/jpeg",
                )
