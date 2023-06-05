# ISBN-Checking-and-Validation
Solution to a challenge on Edabit, found at the following link: https://edabit.com/challenge/DpFmDxcyesPfPoFMn

The International Standard Book Number (ISBN) is a unique identifying number given to each published book. ISBNs assigned after January 2007 are 13 digits long (ISBN-13), however books with 10-digit ISBNs are still in wide use.

This application performs the following:

1. Return "Invalid" if it is not a valid ISBN-10 or ISBN-13.
2. Return "Valid" if it is a valid ISBN-13.
3. If it is a valid ISBN-10, convert it into an ISBN-13 and return the ISBN-13 number.

You can find the deployed streamlit application at: https://tarynnicole-isbn-checking-and-validation-isbn-k0ibn6.streamlit.app/


To download this repo and modify the code, you can follow the instructions at https://docs.streamlit.io/library/get-started/installation on how to setup your virtual environment for Streamlit.
I used Anaconda Navigator, but there are a few options you may choose from.

Once you set up your environment, you can run the application from your terminal by running the command `streamlit run ISBN.py`, ensuring you are in the root folder of the application

# Examples of usage (Testing)

## Entering a valid ISBN-13 number:
![image](https://github.com/TarynNicole/ISBN-Checking-and-Validation/assets/70257895/41c33d19-bae6-4c35-b24d-1f2b91f3851c)


## Entering an invalid ISBN-10 number:
![image](https://github.com/TarynNicole/ISBN-Checking-and-Validation/assets/70257895/0106d0b6-e0fd-4b08-a0c7-db86e4fb61e5)

## Entering a valid ISBN-10 number




