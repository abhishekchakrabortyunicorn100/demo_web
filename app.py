import streamlit as st
# st.write('# Streamlit calculator')
# number1= st.number_input('number 1')
# number2 = st.number_input('number 2')
# num3 = number1+number2
# st.write('# Answer is ',num3)

# st.title("Welcome to OpenAI")
# st.header("Python")
# st.subheader("Java")
# st.markdown("I love Python")
# st.code(""" for i in range(1,5,1):
              #  print("Hello")
    #  """)


# import pandas as pd
# data =  pd.read_csv("/content/twcs.csv")
# st.dataframe(data)

name = st.text_input("Enter your Name: ")
fname = st.text_input("Enter your fater name: ")
adr = st.text_area("Enter your text: ")
classdata = st.selectbox("Enter your class: ",(6,7,8,9,10,11,12))

button = st.button("Done")

if button:
  st.markdown(f""" 
     Name:  {name}
     Father Name:  {fname}
     address:  {adr}
     class:  {classdata}
  
  
  """)





