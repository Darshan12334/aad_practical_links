import streamlit as st

st.header("Closest to Zero")
st.subheader("Enter 5 integers:")

num = [0] * 5  # Initialize a list with zeros

for i in range(5):
    num[i] = st.number_input(f"Number {i + 1}")
min=[]
num1=[]
num2=[]
for i in range(0,4):
    for j in range(i+1,5):
        min.append(abs(num[i]+num[j]))

# st.write("## Numbers are:",num,min)
min.sort()
for i in range(0,4):
    for j in range(i+1,5):
        if(abs(num[i]+num[j])==min[0]):
            num1.append(num[i])
            num2.append(num[j])
# st.write("sum closest to zero is ",min[0])
combined_list=[]
for i in range(len(num1)):
    combined_list.append(f"{num1[i]} {num2[i]}")

result = ", ".join(combined_list)

st.write("".join(str(x) for x in result))