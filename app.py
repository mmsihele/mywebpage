from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

# Load Lottie animation from URL
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Set page configuration
st.set_page_config(page_title="I'M AN ENGINEERING STUDENT!", page_icon="💻", layout="wide")

# Load local CSS
def local_css(file_name):
    try:
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        st.error("CSS file not found. Make sure the path is correct.")

local_css("style/style.css")

# Load Lottie animation
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")

# Load images
try:
    img_contact_form = Image.open("462567014_1092285125367772_5253116121943760911_n.jpg")
    img_github = Image.open("462567014_1092285125367772_5253116121943760911_n.jpg")
except FileNotFoundError:
    st.error("Image file not found. Make sure the paths are correct.")

# Header section
with st.container():
    st.subheader("Hi, I am Mishele Ann")
    st.title("let's explore how computer engineering can do!")
    st.write(
        """
        Welcome to my page! Embark on a journey with me into the fascinating realm of Computer Engineering. 
        I’ll share my experiences, challenges, and the joys of life as a Computer Engineering student.
        """
    )
    st.write("[Message me on Gmail >](mailto:misheleann024@gmail.com)")

# First-year perspective section
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Computer Programming: the Experiences!")
        st.write(
            """
            Starting university was a blend of excitement and nervous anticipation. 
            Diving into programming felt like uncovering a hidden language.
            From binary to algorithms, every step has been an adventure worth taking!
            """
        )
        st.write("[Learn more >](https://www.youtube.com/watch?v=VqgUkExPvLY)")
    with right_column:
        if lottie_coding:
            st_lottie(lottie_coding, height=300, key="coding")
        else:
            st.error("Lottie animation could not load.")

# Insights and reflections
with st.container():
    st.write("---")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_contact_form, caption="Computer enineering student: The selcouth of taking risk")
    with text_column:
        st.write(
            """
           Programming assignments are both exciting and challenging.
           Debugging can feel like a daily mental workout, but the satisfaction of solving a tough problem is truly rewarding. 
           Balancing academics, personal time, and social life is a constant juggling act, but staying organized makes it all manageable.
            """
        )

# Pros and cons of programming
with st.container():
    st.write("---")
    st.subheader("PROS AND CONS")
    st.write("### PROS:")
    st.write("""
    1. Access to lucrative career opportunities with a growing demand for programmers.  
2. Enhancement of logical thinking and problem-solving abilities.  
3. Opportunities to express creativity by developing innovative solutions.  
4. Flexible work environments, including the possibility of remote work.  
5. Ongoing learning in a constantly evolving field.  
6. The chance to connect with a global network of developers.
    """)
    st.write("### CONS:")
    st.write("""
   1. A steep learning curve can be challenging for beginners.  
2. Sedentary work may have an impact on physical health.  
3. Debugging can be both time-consuming and frustrating.  
4. Rapid technological advancements require constant learning.  
5. Some work environments can feel isolating.  
6. Managing the complexity of code in large projects can be difficult.
    """)

# Contact form section
with st.container():
    st.write("---")
    st.header("For Comments:")
    st.write("##")
    
    contact_form = """
    <form action="https://formspree.io/f/{your-form-id}" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
