text_file = open("demo1.txt", "r")
print(text_file.read())
text_file.close()


text_file = open("demo1.txt", "a")
text_file.write("Good Luck!")
text_file.close()

text_file = open("demo1.txt", "r")
print(text_file.read())

text_file = open('demo2.txt', "w")
text_file.write("We're studying Python.")
text_file = open("demo2.txt", "r")
print(text_file.read())
text_file.close()


with open('demo1.txt', "r") as text_file:
    text_file.read()


