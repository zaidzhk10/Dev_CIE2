import sys

if len(sys.argv) == 4:
    mobile=sys.argv[1]
    email=sys.argv[2]
    password=sys.argv[3] 

else:
   mobile="000"
   email="000"
   password="000"

stored_mobile="8050274413"
stored_email="tncsentinel@gmail.com"
stored_password="abc@123"

if mobile == stored_mobile and email == stored_email and password == stored_password:
   print("login successful")

else:  
   print("login unsuccessful")


