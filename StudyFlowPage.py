import os
import streamlit as st

# App config
st.set_page_config(page_title="Study Flow", page_icon="studyflownew.png", layout="wide")

# Top-left logo
st.image("studyflownew.png", width=150)

# Navigation helper
def navigate(page_name):
    st.session_state.page = page_name
    st.rerun()

# Session state initialization
if "page" not in st.session_state:
    st.session_state.page = "home"

# Sidebar navigation
with st.sidebar:
    st.title("Navigation")
    if st.button("Home"):
        navigate("home")
    if st.button("Meet the Team"):
        navigate("team")
    if st.button("How to Use"):
        navigate("howto")
    if st.button("Product Pricing"):
        navigate("pricing")
    if st.button("Product Specifications"):
        navigate("specs")
    if st.button("User Persona"):
        navigate("persona")

# Page rendering logic
if st.session_state.page == "home":
    st.title("Welcome to Study Flow")
    st.markdown("""
        Our software application aims to help students who want a centralized platform for studying and scheduling tools, resulting in increased organization and decreased subscription costs, instead of previous reliance on multiple software platforms. 
        
        
    """)

    st.markdown("""
**Our Story**
            : Study Flow started with a question: Why does studying still feel so disorganized, even with a hundred apps out there? 
                We didn’t want to guess the answers, so we talked to students. They told us what was missing: a tool that actually adapts to their schedules, learning styles, and exam stress. 
                We listened to what worked, what didn’t, and what they wished it could do. From that, we kept refining: simplifying the calendar, making study algorithm quicker, and designing features that respond to real academic situations. 
                Our mission is to build with students in our center focus!        
        
    """)
    st.image("figma5.png", width=1000)

elif st.session_state.page == "team":
    st.title("Meet the Team")

    st.subheader("Avyukth Sai Rangarajan")
    if st.button("About Sai"):
        navigate("sai")

    st.subheader("Willow Shannon")
    if st.button("About Willow"):
        navigate("willow")

    st.subheader("Kashish Patel")
    if st.button("About Kashish"):
        navigate("kashish")

    st.subheader("Nick Rinala")
    if st.button("About Nick"):
        navigate("nick")

elif st.session_state.page == "sai":
    st.title("About Sai")
    st.image("linkedin.jpg", width=300)
    st.markdown("""
    I am an undergraduate student at The Ohio State University studying computer science with a minor in business as part of the Integrated Business and Engineering (IBE) Honors Program. I possess strong leadership and communication skills, and I am nteresting in blending software development with artificial intelligence while developing a strong understanding of marketing software products in the business world. 
    """)
    if st.button("← Back to Team"):
        navigate("team")

elif st.session_state.page == "willow":
    st.title("About Willow")
    st.image("willow.JPEG", width=300)
    st.markdown("""
    I am a first year Aerospace Engineering student at The Ohio State University, where I am on track to minor in Business and am also part of the Honors Program.
My passion lies in both the aircraft and space sectors of aerospace, with more interest in the space sector. I am enthusiastic about space exploration, particularly in the areas of rockets and satellites.    """)
    if st.button("← Back to Team"):
        navigate("team")

elif st.session_state.page == "kashish":
    st.title("About Kashish")
    st.image("kashish.png", width=300)
    st.markdown("""
    I am an undergraduate student at The Ohio State University in the Integrated Business and Engineering Honors program on the Software Innovation track specializing in Finance and minoring in Computer Science Engineering. Through numerous volunteer experiences, diverse background, and school organizations such as DECA, KEY Club, Women in Business, and IBE I have learned valuable skills in leadership, problem solving, and presentation. 
    """)
    if st.button("← Back to Team"):
        navigate("team")

elif st.session_state.page == "nick":
    st.title("About Nick")
    st.image("nickrinala.png", width=300)
    st.markdown("""
     I am a current student within the Integrated Business and Engineering Honors Program in the Fisher College of Business at The Ohio State University. I am looking towards a future in financial management, with aspirations within the financial analysis, management, and investment banking sub-sectors. As a student at The Ohio State University, I am apart of Buckeye Capital Investors, Buckeye Ventures, Scarlet Investment Group, and the IBE Honors Cohort. 
    """)
    if st.button("← Back to Team"):
        navigate("team")

elif st.session_state.page == "howto":
    st.title("How to Use Study Flow")
    st.markdown("""
    
    1. Install application: find it on the App Store/Google Play Store.
    2. Download to device. This app should sync across your accounts to access on any device. 
    3. Log into the app/create an account to select subscription type.
    4. Use the app features as you see fit!
    5. Personalized schedules can be created by importing PDF syllabi and course documents.
    6. Flashcards can be created by importing handwritten notes taken by you!
    """)

    st.write("")
    st.write("")
    st.markdown("""
    
    Here is a sample walkthrough of our interface!
    """)
    st.write("")

    st.image("figma1.png", width=1000)
    st.image("figma2.png", width=1000)
    st.image("figma3.png", width=1000)
    st.image("figma4.png", width=1000)
    st.image("figma5.png", width=1000)
    st.image("figma6.png", width=1000)
    st.image("figma7.png", width=1000)

    



elif st.session_state.page == "pricing":
    st.title("Product Pricing")
    st.markdown("""
    | Plan                             | Price                      |
    |----------------------------------|----------------------------|
    | Free Trial (2 weeks)             | $0.00                      |
    | Individual                       | $14.99/month               |
    | Tiered Business Subscription     | Scaled by business size    |
    """)
elif st.session_state.page == "specs":
    st.title("Academic Study Tools")

    st.markdown("We are currently testing the study AI and scheduling AI feature through a preexisting AI model (Google Gemini), in which we have obtained an API key for. We have developed a local website where we can test the model by uploading downloaded PDF schedules which then output assignments and their due dates. To test the model, we are timing how long it takes to output the correct information. We are also keeping track of if the output is correct information and in the desired format. So far, we have been able to achieve output generations around 5 seconds of uploading, which is far quicker than our target goal of 20 seconds. Our team is happy with these results and will continue to refine our model in order to create the best output generation possible. ")
    st.image("studyflowdemo.png", width = 1000)
    st.markdown("## Study Tools")
    st.markdown("- Study AI")

    st.markdown("## Practice & Planning")
    st.markdown("- Practice Exams\n- Assignment Checklist\n- Assignment Calendar")

    st.markdown("---")

    st.markdown("## Calendar Tools")

    st.markdown("### Smart Scheduling")
    st.markdown("- Calendar AI")

    st.markdown("### Layout & Organization")
    st.markdown("- Calendar Layout\n- Assignment Links\n- Event Description and Map")




elif st.session_state.page == "persona":
    st.image("fredpersona.png", width=1000)


# (Optional) Generation config display — if needed later
# generation_config = {
#     "temperature": 1,
#     "top_p": 0.95,
#     "top_k": 40,
#     "max_output_tokens": 8192,
#     "response_mime_type": "text/plain",
# }


