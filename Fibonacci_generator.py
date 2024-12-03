import streamlit as st
import random

#streamlit run Fibonacci_generator.py

color = "placeholder"
st.markdown(
    f"""
    <style>
    /* Import Great Vibes font */
    @import url('https://fonts.googleapis.com/css2?family=Great+Vibes&display=swap');

    /* Apply the font to Streamlit title */
    .title {{
        font-family: 'Great Vibes', cursive;
        font-size: 60px;
        color: #333333;
    }}
    .stButton > button {{
        display: block;
        margin: 0 auto;
    }}
    .text {{
        font-family: 'Great Vibes', cursive;
        font-size: 20px;
        color: #333333; }}
    
    .stApp {{
       background-color: {color};
       }}
    </style>
   
    """,
    unsafe_allow_html=True
)

st.markdown("<h1 class='title'>Hello World and welcome to a cool Fibonacci Generator!</h1>", unsafe_allow_html=True)

agree = st.checkbox("I agree to use this powerful tool only for ethical reasons")
if agree:


    limit = st.slider("How many numbers would you like to generate?", 3, 100)
    button_1 = st.button("Submit")

    if button_1:

        fs = [0, 1]
        for i in range(101):
            if i == 0:
                continue
            a = fs[i - 1] + fs[i]
            fs.append(a)
            #print(a)
            if len(fs) > limit -1:
                #print(fs)
                break
        st.write(f"<div class = 'text'> Your result is {fs}</div", unsafe_allow_html=True)


    action = st.radio("Or select advanced action based on:", ["Specific index", "Date of birth", "Eloi, Eloi, lemba sabachthani", "Random"])
    if action == "Specific index":
        number = st.number_input("Enter an index", min_value=3, max_value=1000, value=50)
        fs = [0, 1]
        for i in range(number + 1):
            if i == 0:
                continue
            a = fs[i - 1] + fs[i]
            fs.append(a)
        specific = fs[number]
            # print(a)
            #if len(fs) > limit - 1:
                # print(fs)
                #break
        st.write("Here you go: ", specific)
    if action == "Random":
        random = random.randint(1, 100)
        fs = [0, 1]
        result = 0
        for i in range(random + 1):
            if i == 0:
                continue
            a = fs[i - 1] + fs[i]
            fs.append(a)
            # print(a)
            if len(fs) > random - 1:
                result = str(fs[i - 1:])
                #print(fs)
                break
        st.write("Random fibonacci: " + result)
    if action == "Date of birth":
        lucky = None
        date = str(st.date_input("Select a date"))
        fs = [0, 1]
        fate = int(date[5:7]) + int(date[8:10])
        for i in range(fate + 1):
            if i == 0:
                continue
            a = fs[i - 1] + fs[i]
            fs.append(a)
            # print(a)
            if len(fs) > fate - 1:
                # print(fs)
                lucky = fs[i + 1]
                break
        st.write("Your lucky Fibonacci number is :", lucky)

    if action == "Eloi, Eloi, lemba sabachthani":
        st.write("\'Then I began to bear fruit, and to know many things, to grow and well thrive: word by word I sought out words, fact by fact I sought out facts\'")
        st.image("https://orig00.deviantart.net/dfae/f/2017/177/d/d/yggdrasil_by_ektrom-dbe3zz0.jpg",use_container_width=True)


st.image("https://thegardendiaries.files.wordpress.com/2013/08/fibonacci_galaxy.png", use_container_width=True)

st.markdown("\n")
st.markdown("\n")
st.markdown("\n")
st.markdown("\n")
st.markdown("\n")
st.markdown("\n")
st.markdown("\n")
st.markdown("\n")
st.markdown("\n")
st.markdown("\n")
st.markdown("\n")
st.markdown("\n")
st.markdown("\n")
st.markdown("\n")
st.markdown("\n")
st.markdown("\n")
st.markdown("\n")
st.markdown("\n")
st.markdown("\n")
st.markdown("\n")
st.markdown("\n")
st.markdown("\n")
st.markdown("\n")
st.markdown("\n")
st.markdown("\n")
st.markdown("\n")
st.markdown("\n")
st.markdown("\n")
st.markdown("\n")
st.markdown("\n")
st.markdown("\n")
st.markdown("\n")
st.markdown("\n")
st.markdown("\n")
st.markdown("\n")
st.markdown("\n")
st.markdown("\n")
st.markdown("\n")
st.markdown("\n")
st.markdown("\n")



banana = st.checkbox("Banana?", value = False)

banana_url = "https://th.bing.com/th/id/OIP.DxSiKzSxcdU4HO20F-zEaQHaE8?rs=1&pid=ImgDetMain"

if banana:
    st.markdown(
        f"""
            <style>
            .stApp {{
                background-image: url("{banana_url}");
                background-size: cover;
                background-position: center;
                height: 100vh;
            }}
            
             /* Media query for mobile devices */
            @media (max-width: 768px) {{
                .stApp {{
                    background-size: contain; /* Keeps the entire image within view */
                    background-position: top;
                    height: auto; /* Adjusts height based on content */
        }}
    }}
    </style>
            """,
        unsafe_allow_html=True
    )
color = st.color_picker("Or pick a color:", "#FFFFFF", key="bg_color")
# Check if the color has changed and rerun if needed
if "previous_color" not in st.session_state:
    st.session_state.previous_color = color

# Rerun the app when the color changes
if color != st.session_state.previous_color:
    st.session_state.previous_color = color
    st.rerun()

st.markdown(
    f"""
    <style>
    .stApp {{
        background-color: {color};
    }}
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<div class ='text'>🚀🌌🌠 made with Python and Streamlit by Rafal Py🚀🌌🌠 </div>", unsafe_allow_html=True)