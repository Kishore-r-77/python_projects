# Reading the file
# with open("file.txt") as text_file:
#     content = text_file.read()
#     print(content)

# Appending the text
with open("file.txt",mode="a") as text_file:
    text_file.write("\nI Excel more than Anyone Around Me.")
