"""
KyawPyaeSone
"""

username = input("Please enter your name: ")

if " " in username:
    print(" ** Should not contain spaces ** ")
    username = input("Please enter your name : ")
    print(username[1])
else:
    print(username[1])
