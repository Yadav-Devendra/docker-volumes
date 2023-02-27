"""
name = input("Enter your name: ")
print("Hello ",name)
file = open('./data/names.txt','a')
file.write("This is the write command\n")
file.write("It allows us to write in a particular file\n")
file.write(name)
file.close()
"""
import os
entries = os.listdir("/data")
print(entries)

file = open("/data/names.txt", "r")
print (file.read())
file.close()