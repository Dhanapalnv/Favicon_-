import streamlit as st
import requests
from io import BytesIO
from PIL import Image

def favicon_app():
    # Set up Streamlit page configuration
    st.set_page_config(
        page_title="Extract Favicon",  # Page title
        page_icon="https://freepngimg.com/thumb/world_wide_web/99120-www-free-hd-image.png"  # Page icon
    )

    st.title("Extract Favicon")  # Main title

    # Input field for the website URL
    url = st.text_input("Input URL", placeholder="https://www.google.com")

    # Radio button selection for favicon size
    size = st.radio("Favicon Size...", ["16", "32", "48"])

    # Action when the "Find Favicon" button is clicked
    if st.button("Find Favicon"):
        # Construct API URL with user input
        api_url = f"https://t1.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url={url}&size={size}"

        try:
            # Make a request to the API to fetch the favicon
            response = requests.get(api_url)
            response.raise_for_status()  # Raise an error for failed requests

            # Load the favicon image
            img = Image.open(BytesIO(response.content))
            
            # Display the favicon image
            st.image(img, caption='Favicon Retrieved!', use_column_width=False)

            # Prepare the image for download
            buffer = BytesIO()
            img.save(buffer, format="PNG")
            
            # Create a download button for the favicon
            st.download_button(
                label="Download",
                data=buffer.getvalue(),
                file_name="favicon.png",
                mime="image/png",
            )
        except requests.exceptions.RequestException as e:
            # Handle request errors
            st.write("An error occurred:", e)

# Run the app when executed directly
if __name__ == "__main__":
    favicon_app()
