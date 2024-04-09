# # Ask user for their name and Remove whitespace from str, and capitalize the input
# _name = input("What's your name? ").strip().title()

# # Say hello to user
# print(f"Hello, {_name}") 

def hello(to = 'World'):
    print("Hello, ", to)

_name = input("What's your name? ").strip().title()

hello(_name)

