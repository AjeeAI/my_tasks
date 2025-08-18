# Question 3
# The code receives the name and then prints out a message that includes the name received.

name = input("Enter your name: ")
message = "Hello, !"
print(f" {name}".join(message.split())) # This line splits the message using the "whitespace" and plugs in the input received into it.

