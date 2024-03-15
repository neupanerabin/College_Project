import pickle
import streamlit as st
import numpy as np

st.header("Book recommendation system")

model = pickle.load(open('/Users/rabin/College_Project_Seven/artifacts/model.pkl','rb'))
book_name = pickle.load(open('/Users/rabin/College_Project_Seven/artifacts/book_name.pkl','rb'))
final_rating = pickle.load(open('/Users/rabin/College_Project_Seven/artifacts/final_rating.pkl','rb'))
book_pivot = pickle.load(open('/Users/rabin/College_Project_Seven/artifacts/book_pivot.pkl','rb'))

def recommend_books(book_name):
    book_list = []
    nearest_indices = {}
    k = 6
    for i in range(num_rows):
    # Sort distances for the current row
        nearest_indices[i] = np.argsort(distance_matrix[i])[:k]


    poster_url = fetch_poster(nearest_indices)
    for i in range(len(nearest_indices)):
        books = book_pivot.index[nearest_indices[i]]
        for j in books:
            book_list.append(j)
    return book_list, poster_url


selected_books = st.selectbox(
    "Type or select a book",
    book_name
)

if st.button('Show recommendations '):
    recommendations_books, poster_url = recommend_books(selected_books)