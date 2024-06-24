import streamlit as st
from streamlit_option_menu import option_menu as om
import requests
from streamlit_lottie import st_lottie
from PIL import Image



st.set_page_config(layout="wide")

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)
local_css("E:/Portfolio/style/style.css")


# def load_lottieurl(url):
#     r = requests.get(url)
#     if r.status_code != 200:
#         return None
#     return r.json()

# lottie_coder = "https://lottiefiles.com/animations/coder-jAUpeq1je0?from=search"
image = Image.open('E:/Portfolio/bg.png')
# image1 = Image.open('E:/Portfolio/contact.jpg')

st.write("##")
st.subheader("Hey Guys :wave:")
st.title("Riya's Portfolio Website!")
st.write("""
        Aspiring data scientist with a solid foundation in Python and generative AI techniques.
Proficient in machine learning, data analysis, and statistical modeling. Passionate about
leveraging analytical skills and innovative solutions in a collaborative environment.
Eager to contribute fresh perspectives and technical expertise to a forward-thinking
data science team.

""")
st.write("[Read More](https://streamlit.io/)")

with st.container():
    selected = om (
        menu_title = None,
        options = ['About','Projects','Contact'],
        icons = ['person','code-slash','chat-left-text-fill'],
        orientation='horizontal'
    )

if selected == 'About':
    with st.container():
        col1,col2 = st.columns(2)
        with col1:
            st.write("##")
            st.subheader("I am Riya Yadav")
            st.title("Undergrad at BIT")
        # with col2:
        #     st_lottie(lottie_coder)
    st.write("____")

    with st.container():
        col3,col4 = st.columns(2)
        with col3:
            st.subheader("""
    Education
    -Noble University
                        -Bechlor of Engineering(GTU)
                        -Computer Science
                        -CGPA:8.36    
    -N.P.Bhalodiya High School
                        -11-12th
                        -Science(Gujarat /board)
                        -Grade:B
    -R.S.Kalariya Primary School
                        -10th
                        -Gujarat board
                        -Grade:A            
 """)

if selected=="Projects":
    with st.container():
        st.header("My Projects")
        st.write("##")
        col5,col6 = st.columns({1,2})
        with col5:
            st.image(image)
        with col6:
            st.subheader("Project 1")
            st.write("____")
            st.markdown("{github repo link}")


if selected == "Contact":
    st.header("Get in touch!")
    st.write("##")
    st.write("##")

    contact_form = """
        <form action="https://formsubmit.co/riyay5051@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your Name" required>
        <input type="email" name="email" placeholder="Your Email" required>
        <textarea name = "message" placeholder="Your Message" required></textarea>
        <button type="submit">Send</button>
        </form>
    """

    left_col,right_col = st.columns({2,1})
    with left_col:
        st.markdown(contact_form,unsafe_allow_html=True)
    # with right_col:
    #     st.image(image1)       
