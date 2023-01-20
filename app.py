import streamlit as st
st.image("https://as1.ftcdn.net/v2/jpg/05/15/63/82/1000_F_515638234_Leo0UBEay0ozXWnObkkxLRNJXM9xhdWG.jpg")
st.title("String App")
message=st.text_area("Enter some text")
button=st.button("Process text")

if button:
    st.write(message)
    if st.checkbox("Show words"):
        words=message.split()
        st.write(words)
    if st.checkbox("character count"):
        for char in message:
            st.write(f'{char} : {message.count(char)}')
            
        