import streamlit as st
import requests
from io import BytesIO
from PIL import Image
import streamlit.components.v1 as components

# Set up Streamlit page configuration
st.set_page_config(
    page_title="Exifa.net", 
    page_icon="🌀", 
    layout="wide"
)

particles_js = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Particles.js</title>
  <style>
  #particles-js {
    position: fixed;
    width: 100vw;
    height: 100vh;
    top: 0;
    left: 0;
    z-index: -1; /* Send the animation to the back */
  }
  .content {
    position: relative;
    z-index: 1;
    color: white;
  }
  </style>
</head>
<body>
  <div id="particles-js"></div>
  <div class="content">
    <!-- Placeholder for Streamlit content -->
  </div>
  <script src="https://cdn.jsdelivr.net/particles.js/2.0.0/particles.min.js"></script>
  <script>
    particlesJS("particles-js", {
      "particles": {
        "number": {
          "value": 300,
          "density": {
            "enable": true,
            "value_area": 800
          }
        },
        "color": {
          "value": "#ffffff"
        },
        "shape": {
          "type": "circle",
          "stroke": {
            "width": 0,
            "color": "#000000"
          },
          "polygon": {
            "nb_sides": 5
          },
          "image": {
            "src": "img/github.svg",
            "width": 100,
            "height": 100
          }
        },
        "opacity": {
          "value": 0.5,
          "random": false,
          "anim": {
            "enable": false,
            "speed": 1,
            "opacity_min": 0.2,
            "sync": false
          }
        },
        "size": {
          "value": 2,
          "random": true,
          "anim": {
            "enable": false,
            "speed": 40,
            "size_min": 0.1,
            "sync": false
          }
        },
        "line_linked": {
          "enable": true,
          "distance": 100,
          "color": "#ffffff",
          "opacity": 0.22,
          "width": 1
        },
        "move": {
          "enable": true,
          "speed": 0.2,
          "direction": "none",
          "random": false,
          "straight": false,
          "out_mode": "out",
          "bounce": true,
          "attract": {
            "enable": false,
            "rotateX": 600,
            "rotateY": 1200
          }
        }
      },
      "interactivity": {
        "detect_on": "canvas",
        "events": {
          "onhover": {
            "enable": true,
            "mode": "grab"
          },
          "onclick": {
            "enable": true,
            "mode": "repulse"
          },
          "resize": true
        },
        "modes": {
          "grab": {
            "distance": 100,
            "line_linked": {
              "opacity": 1
            }
          },
          "bubble": {
            "distance": 400,
            "size": 2,
            "duration": 2,
            "opacity": 0.5,
            "speed": 1
          },
          "repulse": {
            "distance": 200,
            "duration": 0.4
          },
          "push": {
            "particles_nb": 2
          },
          "remove": {
            "particles_nb": 3
          }
        }
      },
      "retina_detect": true
    });
  </script>
</body>
</html>
"""

def favicon_app():
    st.title("Favicon Finder")  # Main title

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
            st.image(img, caption='Favicon Retrieved!', use_container_width=False)

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

if "show_animation" not in st.session_state:
    st.session_state.show_animation = True

if st.session_state.show_animation:
    components.html(particles_js, height=370, scrolling=False)

# Run the app when executed directly
if __name__ == "__main__":
    favicon_app()
