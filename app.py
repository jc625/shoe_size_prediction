import streamlit as st
import pickle


st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Introduction", "Shoe Size Prediction"])


if page == "Introduction":
    st.markdown("""
    <div style="text-align: center; color:white;background-color:black;">
    <h1>Shoe Size Prediction App</h1>
    </div>
    """, unsafe_allow_html=True)
    st.image('shoe_size.jpg',  use_container_width=True)
    st.markdown("""
    <h5 style='text-align: center; color: Green;'>This app can predict your shoesize by simply using your height and Gender</h5>
    """, unsafe_allow_html=True)





elif page == "Shoe Size Prediction":
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)


    st.title("Shoe Size Prediction App")
    st.markdown("""
    <div style='color:yellow;font-size:1.5rem;'>
    Enter Your height and Gender to predict your shoe Size
    </div>
    """, unsafe_allow_html=True)

    height = st.number_input("Enter Height (in cm):", min_value=70, max_value=1000, value=150)
    gender = st.selectbox("Gender:", options=["Male", "Female"])
    gender_code = 1 if gender == "Male" else 2
    btn=st.button("Predict Shoe Size")
    prediction =model.predict([[height,gender_code]]).astype(int)[0]
    if btn:
        st.write("Predicted Shoe Size is: ", str(prediction))
