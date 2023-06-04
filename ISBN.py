#!/usr/bin/env python
# coding: utf-8

import streamlit as st

def is_valid_isbn(isbn):
    sum_isbn_product = 0
    if len(isbn) not in (10, 13):
        return "Invalid"

    if len(isbn) == 10:
        if isbn[9] == 'X':
            sum_isbn_product += 10
            for i in range(9):
                sum_isbn_product += int(isbn[i]) * (10 - i)
        else:
            for i in range(10):
                sum_isbn_product += int(isbn[i]) * (10 - i)
        if sum_isbn_product % 11 != 0:
            return "Invalid"
        else:
            isbn_13 = '978' + isbn
            sum_isbn_13_products = sum(int(isbn_13[i]) if i % 2 == 0 else 3 * int(isbn_13[i]) for i in range(12))
            check_digit = (10 - sum_isbn_13_products % 10) % 10
            isbn += str(check_digit)
            return f"After converting the ISBN-10 number, the new valid ISBN-13 number is {isbn}"
    else:
        sum_products_isbn13 = sum(int(isbn[i]) if i % 2 == 0 else 3 * int(isbn[i]) for i in range(13))
        if sum_products_isbn13 % 10 != 0:
            return "Invalid"
        else:
            return "Valid"

def main():
    st.title("ISBN Validation and Conversion")
    isbn = st.text_input("Enter the ISBN number:")
    if st.button("Validate"):
        result = is_valid_isbn(isbn)
        st.write(result)

if __name__ == "__main__":
    main()



