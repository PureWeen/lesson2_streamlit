import streamlit as st  
  
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."

st.text("Select operation:")
st.text("1. Add")
st.text("2. Subtract")
st.text("3. Multiply")
st.text("4. Divide")

choice = st.text_input("Enter choice (1/2/3/4): ")

if choice in ('1', '2', '3', '4'):
    num1Str = st.text_input("Enter first number: ")
    num2Str = st.text_input("Enter second number: ")

    if num1Str and num2Str:
        num1 = float(num1Str)
        num2 = float(num2Str)
        if choice == '1':
            st.text(f"{num1} + {num2} = {add(num1, num2)}")

        elif choice == '2':
            st.text(f"{num1} - {num2} = {subtract(num1, num2)}")

        elif choice == '3':
            st.text(f"{num1} * {num2} = {multiply(num1, num2)}")

        elif choice == '4':
            st.text(f"{num1} / {num2} = {divide(num1, num2)}")

        next_calculation = st.text_input("Do you want to perform another calculation? (yes/no): ")
   # if next_calculation.lower() != 'yes':
    #    break
else:
    st.text("Invalid Input")