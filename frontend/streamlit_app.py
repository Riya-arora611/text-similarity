import streamlit as st
import requests



def get_similarity_score(text1, text2):
    url = "http://0.0.0.0:8000/text-similarity" # if you want to run it on local
    # Uncomment the following if running on docker and comment the above one
    # url = "http://backend:8000/text-similarity"
    data = {"text1": text1, "text2": text2}
    response = requests.post(url, json=data)

    if response.status_code == 200:
        result = response.json()
        return result.get("similarity_score", "Error")
    else:
        return f"Error: {response.status_code}"

def main():
    st.title("Text Similarity App")

    text1 = st.text_area("Enter Text 1:", height=200)
    text2 = st.text_area("Enter Text 2:", height=200)

    if st.button("Calculate Similarity"):
        if text1 and text2:
            similarity_score = get_similarity_score(text1, text2)
            st.success(f"Similarity Score: {similarity_score:.2f}")
        else:
            st.warning("Please enter both texts.")

if __name__ == "__main__":
    main()