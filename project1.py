user_input = str(input("Enter your text: "))
text = user_input.split()

a = ""
for x in text:
    a = a + str(x[0]).upper()
print(f"The acronym for {user_input} is: {a}")