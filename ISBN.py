#!/usr/bin/env python
# coding: utf-8

import streamlit as st

def TESTING_FOR_ISBN_10_13(isbn):
    sum_isbn_product = 0
    # First test to see if the ISBN number is ISBN-10 or ISBN-13
    if len(isbn) not in (10, 13):
        return "Invalid"

    #Now test if it is ISBN-10:
    if len(isbn)==10:
        #If last digit is an X, add 10 to the sum of products
        if isbn[9]=='X':
            sum_isbn_product+=10
        #Now calculate the total sum of products by multiplying the rest of the digits by their corresponding number
            for i in range(9):
                sum_isbn_product+=(int(isbn[i])*(10-i))
         #If the last digit is not an X, calculate the sum of products by multiplying each digit by the corresponding number and adding it together       
        else:
            for i in range(10):
                sum_isbn_product+=(int(isbn[i])*(10-i))
    # If not divisible by 11, it is not a valid ISBN-10, and thus return :invalid"
        if sum_isbn_product%11 !=0:
            return "invalid"
        #If it is valid, append 978 and determine the check digit to convert it to ISBN-13
        else:
            isbn_13= '978'+isbn

         #We now need to determine the new sum of products
        sum_isbn_13_products = 0

        for i in range(12):
            if i%2 == 0:
                sum_isbn_13_products += int(isbn_13[i])
            else: 
                sum_isbn_13_products += 3*int(isbn_13[i])

        # Next we calculate the last digit (check digit) to make it a valid ISBN-13 number
        #A valid ISBN-13 number has the sum of products divisible by 10
        check_digit = (10 - sum_isbn_13_products % 10) % 10

        #We then append the check digit to the isbn number to make it a valid ISBN-13 number
        #We also return the valid ISBN-13 numbwe
        isbn_13 += str(check_digit)
        return f"After converting the ISBN-10 number, the new valid ISBN-13 number is {isbn_13}"
    else:
        sum_products_isbn13=0
        #Calculate sum of products for ISBN-13. 
        #We use an else as we assume that if its not ISBN-10 (10-digit number),
        #it must be a 13 digit number since we would have simply returned invalid if it was not a 10 or 13 digit number at the beginning of this function
        for i in range(13):
            if i%2==0:
                sum_products_isbn13 += (int(isbn[i]))
            else:
                sum_products_isbn13+= (int(isbn[i])*3)

        #deterimine whether it is a valid ISBN-13 number by determining if its sum of products is divisible by 10
        if sum_products_isbn13 % 10 !=0:
            return "invalid"
        else:
            return "valid"

def main():
    st.title("ISBN Validation and Conversion")
    isbn = st.text_input("Enter the ISBN number:")
    if st.button("Validate"):
        result = TESTING_FOR_ISBN_10_13(isbn)
        st.write(result)

if __name__ == "__main__":
    main()



