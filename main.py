import streamlit as st
from scrape import (
    scrape_website, 
    split_dom_content, 
    clean_body_content, 
    extract_body_content,
)


st.title("Ai Web Scraper")
url = st.text_input("Enter a Website URL")

if st.button("Scrape Site"):
    st.write("Scraping Site")
    print("-----------------------------------------------[")

    result = scrape_website(url)
    print("-----------------------------------------------]")

    print(result)
    #st.write(url)
    # Add scraping code here

    body_content = extract_body_content(result)
    clean_content = clean_body_content(body_content)

    st.session_state.dom_content = clean_content

    with st.expander("View Dom Content"):
        st.text_area("Dom Content",clean_content, height=300)

    