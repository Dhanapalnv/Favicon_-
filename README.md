# Extract Favicon App

## Overview
This Streamlit app allows users to extract favicons from any website by entering a URL. The extracted favicon can be displayed and downloaded in PNG format.

## Features
- Input a website URL to fetch its favicon.
- Choose the favicon size (16x16, 32x32, or 48x48 pixels).
- Display the favicon within the app.
- Download the extracted favicon as a PNG file.

## Requirements
Make sure you have the following dependencies installed:

```sh
pip install streamlit requests pillow
```

## How to Run
1. Clone this repository or copy the script.
2. Install the required dependencies using the command above.
3. Run the Streamlit app using:

```sh
streamlit run app.py
```

4. Enter a URL in the input field and select a favicon size.
5. Click the "Find Favicon" button to extract the favicon.
6. View the favicon and download it as a PNG file.

## File Structure
```
/Extract-Favicon-App
  ├── app.py          # Main Streamlit script
  ├── README.md       # Documentation file
  ├── requirements.txt # List of dependencies (optional)
```

## API Used
This app fetches favicons using Google's Favicon API:

```
https://t1.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url={}&size={}
```

## Error Handling
- Ensures valid HTTP response before displaying the favicon.
- Catches network errors and displays appropriate messages.
- Handles invalid URLs gracefully.

## License
This project is open-source and free to use. Feel free to modify and enhance it as needed!
