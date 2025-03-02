import time
import json
import os
from PIL import Image, UnidentifiedImageError
import streamlit as st
from streamlit_lottie import st_lottie

# Set up page configuration
st.set_page_config(page_title="Vintage Shutter", page_icon="📸", layout="wide")

# Load Lottie animation file
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

# Apply local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

# Custom CSS for vintage and elegant theme with black touches
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cardo:wght@400;700&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700&display=swap');

    body {
        background-color: #fff;
        color: #6e011c;
        font-family: 'Cardo', serif;
        margin: 0;
    }
    h1, h2, h3, h4, h5, h6 {
        font-family: 'Cinzel', serif;
        color: #fff;
        text-align: center;
        font-weight: 700;
    }
    h2 {
        color: #d6af87;  /* Elegant gold accent */
    }
    h3 {
        font-family: 'Cardo ', serif;
        font-weight: 500;
        color: #E6B8A1;
    }
    /* Black touch to buttons */
    .stButton > button {
        background-color: #1e1e1e;  /* Black button background */
        color: #fff;
        border-radius: 30px;
        padding: 1rem 3rem;
        font-family: 'Cardo ', serif;
        font-weight: 600;
        letter-spacing: 1px;
        transition: all 0.3s ease;
        cursor: pointer;
        border: none;
        box-shadow: 0 8px 15px rgba(0, 0, 0, 0.1);
    }
    .stButton > button:hover {
        background-color: #fff;  /* Darker grey for hover effect */
        color: #d6af87;  /* Elegant golden hue */
        box-shadow: 0 12px 25px rgba(0, 0, 0, 0.15);
    }

    /* Black touch for the footer */
    .cta-section {
        background-color: #1e1e1e;  /* Black background */
        color: white;
        padding: 4rem;
        text-align: center;
        border-radius: 15px;
        margin-top: 5rem;
    }
    .cta-section h2 {
        font-family: 'Cinzel', serif;
        font-size: 2.8rem;
        margin-bottom: 2rem;
    }
    .cta-section a {
        font-size: 1.2rem;
        color: #fff;
        padding: 1rem 2.5rem;
        background-color: #d6af87;
        border-radius: 30px;
        text-decoration: none;
        transition: background-color 0.3s ease;
    }
    .cta-section a:hover {
        background-color: #fff;
        color: #d6af87;
    }

    /* Update sidebar background color to black */
    .stSidebar {
        background-color: #1e1e1e;  /* Dark background */
    }
    .stSidebar .sidebar-content {
        font-family: 'Cinzel', serif;
        font-weight: 700;
        text-align: center;
        color: white;
    }
    .stSidebar .sidebar-content select {
        font-family: 'Cardo ', serif;
        font-weight: 500;
        padding: 0.8rem;
        border-radius: 12px;
        border: 2px solid #fff;
        background-color: #6e011c;  /* Darker select background */
        color: #1e1e1e;  /* Light text color */
    }
    .stSidebar .sidebar-content select:focus {
        border-color: #6e011c;  /* Focus border color */
    }

    /* Section containers with black touches */
    .block-container {
        background-color: #fff;
        padding: 4rem;
        border-radius: 20px;
        box-shadow: 0 8px 15px rgba(0, 0, 0, 0.05);
    }
    .gallery-container img {
        border-radius: 20px;
        box-shadow: 0 8px 15px rgba(0, 0, 0, 0.1);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    .gallery-container img:hover {
        transform: scale(1.05);
        box-shadow: 0 12px 25px rgba(0, 0, 0, 0.15);
    }

    /* Update text color in sidebar */
    .stSidebar .sidebar-content select:focus {
        color: #fff;
    }

    /* Black background for the homepage banner */
    .stContainer {
        padding: 5rem 0;
        background-color: #1e1e1e;  /* Dark background */
    }
    .stContainer h1 {
        color: white;  /* White text for better contrast */
    }

    /* Styling for dropdown with Cinzel font */
    .stSelectbox div[data-baseweb="select"] {
        font-family: 'Cardo', serif;
        color: #6e011c;
    }
    .stSelectbox div[data-baseweb="select"] > div {
        font-family: 'Cardo', serif;
        color: #6e011c;
    }
    .stSelectbox div[data-baseweb="popover"] > div {
        font-family: 'cardo', serif;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# List of image file paths
image_paths = [
    "Images\\car (20).JPG", "Images\\car (24).jpg", "Images\\car (25).jpg",
    "Images\\car (1).jpg", "Images\\car (2).jpg", "Images\\car (3).jpg",
    "Images\\car (6).jpg", "Images\\car (7).jpg", "Images\\car (9).jpg",
    "Images\\car (10).jpg", "Images\\car (30).jpg", "Images\\car (26).jpg",
    "Images\\car (27).jpg", "Images\\car (28).jpg", "Images\\car (29).jpg",
    "Images\\car (5).jpg", "Images\\car (15).jpg", "Images\\car (22).jpg",
    "Images\\car (17).jpg", "Images\\car (23).jpg", "Images\\car (21).jpg"
]
# --- Load Images with Caching ---
@st.cache_data
def load_images(image_paths):
    img_list = []
    for image_path in image_paths:
        if os.path.exists(image_path):
            try:
                img = Image.open(image_path)
                img = img.resize((500, 700))  # Set uniform image size
                img_list.append(img)
            except UnidentifiedImageError:
                st.write(f"Error displaying image: {image_path}")
    return img_list

# --- Top Navigation Bar ---
st.markdown("<h1 style='font-family: Cinzel; text-align: center; color: #6e011c;'>Vintage Shutter</h1>", unsafe_allow_html=True)
selected_page = st.selectbox("", ["Home", "Gallery", "Contact"], index=0)

# --- Home Page ---
if selected_page == "Home":

    # Load Lottie animation
    lottie_coding = load_lottiefile("mein.json")

    # --- About Us Section ---
    with st.container():
        st.markdown("<h3 style='font-family: Cardo; text-align: center; color: #6e011c;'>Capturing Timeless Automotive Beauty 🏎️📸</h3>", unsafe_allow_html=True)
        st.markdown("<h5 style='font-family: Cardo; text-align: center; color: #6e011c;'>📍 Serving NJ, PA, DE, and NY</h5>", unsafe_allow_html=True)

        left_column, right_column = st.columns([1, 1])

        with left_column:
            st.markdown("<h4 style='font-family: Cardo; color: #6e011c;'>What We Offer</h4>", unsafe_allow_html=True)
            st.write(
                 """ 
        - **Capture the Dream** – Transforming your vision into breathtaking automotive & portrait photography.

        - **Timeless Beauty** – Crafting cinematic, high-end images that tell a story beyond the frame.

        - **Precision & Passion** – Every shot is carefully composed to highlight details, power, and elegance.

        - **Unforgettable Experience** – Whether it’s your car, graduation, or a special moment, we create stunning visuals you’ll cherish forever.
        """
            )
            st.markdown("<h5 style='font-family: Cardo; text-align: center; color: #6e011c;'>📸 Ready for a photoshoot? Scroll down to explore our packages.</h5>", unsafe_allow_html=True)

        with right_column:
            st_lottie(
                lottie_coding,
                speed=0.05,
                reverse=False,
                loop=True,
                quality="high",
                height=350,
                width=700,
                key="coding"
            )

    # --- Photography Packages ---
    st.markdown("<h2 style='font-family: Cardo; text-align: center; color: #6e011c;'>📸 Photography Packages</h2>", unsafe_allow_html=True)

    # Car Photography Packages
    st.markdown("<h3 style='font-family: Cardo; color: #6e011c;'>🚗 Car Photography</h3>", unsafe_allow_html=True)
    st.markdown(
        """
        <ul style="font-family: Cardo; color: #6e011c;">
            <li><strong>Basic </strong> – 30-minute session | 5 high-resolution images | 1 location.</li>
            <li><strong>Premium </strong> – 1-hour session | 10 high-resolution images | 2 locations | Rolling shots.</li>
            <li><strong>Elite </strong> – 2-hour session | 20 high-resolution images | 3 locations | Rolling & night shots.</li>
        </ul>
        """, unsafe_allow_html=True
    )

    # Graduation & Portrait Packages
    st.markdown("<h3 style='font-family: Cardo; color: #6e011c;'>🎓 Graduation & Portraits</h3>", unsafe_allow_html=True)
    st.markdown(
        """
        <ul style="font-family: Cardo; color: #6e011c;">
            <li><strong>Standard </strong> – 45-minute session | 8 high-resolution images | 1 outfit | 1 location.</li>
            <li><strong>Premium </strong> – 1-hour session | 15 high-resolution images | 2 outfits | 2 locations.</li>
            <li><strong>Deluxe </strong> – 1.5-hour session | 25 high-resolution images | Unlimited outfits | Multiple locations.</li>
        </ul>
        """, unsafe_allow_html=True
    )

    # Custom Event Photography
    st.markdown("<h3 style='font-family: Cardo; color: #6e011c;'>📅 Custom & Event Photography</h3>", unsafe_allow_html=True)
    st.markdown(
        """
        <ul style="font-family: Cardo; color: #6e011c;">
            <li><strong>💍 Weddings</strong> – Elegant and timeless photography for your special day.</li>
            <li><strong>🏢 Corporate Events</strong> – Professional coverage of conferences, launches, and company events.</li>
            <li><strong>📢 Advertisements</strong> – High-quality images for marketing and promotions.</li>
            <li><strong>🎂 Special Occasions</strong> – Birthdays, anniversaries, and personal celebrations.</li>
        </ul>
        """, unsafe_allow_html=True
    )

    st.markdown(
        "<p style='font-family: Cardo; color: #6e011c; text-align: center;'>Need a **custom package**? Contact us for a personalized photography experience.</p>",
        unsafe_allow_html=True
    )

    # Contact Us Section
    st.markdown(
        """
        <h3 style='font-family: Cardo; text-align: center; color: #6e011c;'>📩 Ready to Book Your Photoshoot?</h3>
        <p style="font-family: Cardo ; text-align: center; color: #6e011c;">Fill out the contact form with your details and let us know which package or event you're interested in.</p>
        """, unsafe_allow_html=True
    )

# --- Gallery Page ---
if selected_page == "Gallery":
    img_list = load_images(image_paths)
    with st.container():
        st.markdown("<h2 style='font-family: Cardo; text-align: center; color: #6e011c;'>Car Portfolio 📸</h2>", unsafe_allow_html=True)
        st.markdown("<h5 style='font-family: Cardo; text-align: center; color: #6e011c;'> Capturing the finest moments! </h5>", unsafe_allow_html=True)
    st.markdown(""" 
        <p style='font-family: Cardo; text-align: left;'>  <a href='https://www.instagram.com/vintage._.shutter/' target='_blank'>Instagram</a>
        """, unsafe_allow_html=True)
    
    num_cols = 7  # Number of columns for image display
    for i in range(0, len(img_list), num_cols):
            cols = st.columns(num_cols)
            for col, img in zip(cols, img_list[i:i + num_cols]):
                col.image(img, use_container_width=True)

# --- Contact Page ---
if selected_page == "Contact":

    # Contact Form Section
    with st.container():
        st.markdown("<h3 style='font-family: Cardo; text-align: center; color: #6e011c;'>Let’s Collaborate 🤝</h3>", unsafe_allow_html=True)

    # Dropdown for selecting a package
    package_option = st.selectbox(
        "", 
        ["Find the Packages here", "Car Photography Packages", "Graduation & Portrait Packages", "Other Events & Custom Packages"]
    )

    # Package-specific options (display as text instead of dropdown)
    package_details = {
        "Car Photography Packages": """
        Basic Package ($150): 30-minute shoot, 5 high-resolution images, 1 location.
        Premium Package ($250): 1-hour shoot, 10 high-resolution images, 2 locations, rolling shots.
        Elite Package ($400): 2-hour shoot, 20 high-resolution images, 3 locations, rolling & night shots.
        """,
        "Graduation & Portrait Packages": """
        Standard Package ($200): 45-minute shoot, 8 high-resolution images, 1 outfit, 1 location.
        Premium Package ($300): 1-hour shoot, 15 high-resolution images, 2 outfits, 2 locations.
        Deluxe Package ($450): 1.5-hour shoot, 25 high-resolution images, unlimited outfits, multiple locations.
        """,
        "Other Events & Custom Packages": """
        Wedding Photography: Capture your special day with elegant and romantic photography.
        Corporate Events: Professional shots for conferences, product launches, and more.
        Advertisements: High-quality images to showcase your brand or product.
        Special Occasions: Birthdays, anniversaries, or any milestone worth celebrating.
        """
    }

    # Display package details dynamically based on user selection
    if package_option in package_details:
        st.markdown(f"<h4 style='font-family: Cardo; text-align: center; color: #6e011c;'>Package Details:</h4>", unsafe_allow_html=True)
        st.markdown(f"<p style='font-family: Cardo; color: #6e011c;'>{package_details[package_option]}</p>", unsafe_allow_html=True)

    # Contact Form
    contact_form = """
        <form action="https://formsubmit.co/shleopard15@gmail.com" method="POST" style="font-family: Cardo;">
            <input type="hidden" name="_captcha" value="false"> 
            <input type="text" name="Name" placeholder="Your Name" required style="font-family: Cardo;">
            <input type="text" name="Phone Number" placeholder="Phone Number" required style="font-family: Cardo;">
            <input type="email" name="Email" placeholder="Your Email" required style="font-family: Cardo;">
            <input type="text" name="Email" placeholder="Selected Package" required style="font-family: Cardo;">
            <textarea name="message" placeholder="Tell us about your project or event..." required style="font-family: Cardo;"></textarea>
            <button type="submit" style="
                background-color:#6e011c; 
                color: #d9b48b; 
                border-radius: 25px;
                padding: 0.8rem 2rem;
                font-family: Cardo;
                font-size: 1.1rem;
                cursor: pointer;
                border: none;
                transition: background-color 0.3s ease;
            " onmouseover="this.style.backgroundColor='#D9B48B'" onmouseout="this.style.backgroundColor='#6e011c'">Send Request</button>
        </form>
    """

    # Display contact form after package selection
    st.markdown(contact_form, unsafe_allow_html=True)

    # Message
    st.write("<p style='font-family: Cardo; text-align: center;'>Let’s bring your vision to life! 🏎️📸</p>", unsafe_allow_html=True)

    # Insta Logo
st.markdown(
    """
    <div style="text-align: center;">
        <a href="https://www.instagram.com/vintage._.shutter/" target="_blank">
            <img src="https://upload.wikimedia.org/wikipedia/commons/a/a5/Instagram_icon.png" 
                 alt="Instagram" 
                 style="width:25px; height:25px; vertical-align:middle; margin-left:5px;">
        </a>
    </div>
    """,
    unsafe_allow_html=True,
)  


#Car Photography
#Basic ($125) – 30-minute session | 5 high-resolution images | 1 location.
#Premium ($225) – 1-hour session | 10 high-resolution images | 2 locations | Rolling shots.
#Elite ($350) – 2-hour session | 20 high-resolution images | 3 locations | Rolling & night shots.
#Graduation & Portraits
#Standard ($175) – 45-minute session | 8 high-resolution images | 1 outfit | 1 location.
#Premium ($275) – 1-hour session | 15 high-resolution images | 2 outfits | 2 locations.
#Deluxe ($400) – 1.5-hour session | 25 high-resolution images | Unlimited outfits | Multiple locations.
# 




# Car Photography:

#Basic Package ($150): A 30-minute session at one location.

#Premium Package ($250): A 1-hour session at two locations, including rolling shots.

#Elite Package ($400): A 2-hour session at three locations, featuring rolling and night shots.

#Graduation & Portrait Photography:

#Standard Package ($200): A 45-minute session with one outfit at a single location.

#Premium Package ($300): A 1-hour session with two outfits at two locations.

#Deluxe Package ($450): A 1.5-hour session with unlimited outfits at multiple locations.
