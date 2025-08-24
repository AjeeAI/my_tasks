# Check if a given string startswith "https://"
""" The use case of this particular program, at least to me might be to check if a website 
is secure by checking if it is https and not just http so as to warn users about potential 
security risks"""

string_data = "https://eportal.oauife.edu.ng"

if string_data.startswith("https://"):
    print("This url(string) starts with https://") 
else:
    print("This website is not secure. Do you still want to proceed? ")
    