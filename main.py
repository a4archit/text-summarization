from textt5 import TEXTT5
import streamlit as st


# loading model
model = TEXTT5()




# some preworking
st.cache_data.clear()
st.cache_resource.clear()
st.set_page_config("Text Summarization | T5-small", page_icon="📝")



# page layout
st.title("Text Summarization")





details = """#### About the Model
- This is a text summarization model.
- This tool is based on a pretrained model named `T5-small`
- Before this pretrained model I had already try about 2 encoder-decoder based models from stratch.
"""

#  Sidebar  
st.sidebar.title("Menu")
st.sidebar.divider()

max_lengh = st.sidebar.slider(
    "Set minimum word limit",
    min_value=20,
    max_value=200,
    step = 10,
    value=50
)

max_lengh = st.sidebar.slider(
    "Set maximum word limit",
    min_value=20,
    max_value=200,
    step = 10,
    value=50
)

st.sidebar.markdown(details)
st.sidebar.write("You can check my social media accounts: ")
st.sidebar.write("[Website](https://a4archit.github.io/my-portfolio)")
st.sidebar.write("[Kaggle](https://www.kaggle.com/architty108)")
st.sidebar.write("[Github](https://www.github.com/a4archit)")
st.sidebar.write("[LinkedIn](https://www.linkedin.com/in/archit-tyagi-191323296)")




# declaring functions
def clear_text():
    st.session_state.user_input_text = ""
    




# taking user input
content = st.text_area('Enter text', height=200, key="user_input_text")

col1, col2 = st.columns([1,1])

with col1:
    # adding clear button
    clear_btn = st.button(
        label = "clear",
        key = "clear_btn_key",
        use_container_width = True,
        on_click=clear_text,
        type = 'secondary'
    )


with col2:
    # adding clear button
    summarize_btn = st.button(
        label = "Summarize",
        key = "summarize_btn_key",
        use_container_width = True,
        type = 'secondary'
    )


if st.session_state.summarize_btn_key:
    content = content.strip()
    if not content:
        st.write(":red[Please provide some text first...]")
        st.rerun()

    words_list = content.split(' ')
    if len(words_list) < 20:
        st.write(":red[Please provide some more text...]")
        st.rerun()


    summarized_text = model.summarize_text(content)

    st.write(summarized_text.capitalize())




# model.summarize_text(article, display=True)

