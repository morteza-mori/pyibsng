import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import required header
from ibsng import IBSng

# Connect and authenticate
conn = IBSng("myusername:mypassword@http://192.168.1.1:1237")
conn.auth()

# Call method
s_users = conn.user().searchUser(1, 20, 10000, '<')

# Print the server result
print("OBJ Result:", s_users.result)
print("JSON Result:", s_users.json)