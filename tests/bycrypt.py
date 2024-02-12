# import bcrypt
#
# password = "123"
# salt = bcrypt.gensalt(2)
# hashed = bcrypt.hashpw(password, salt)
#
# hashed2 = bcrypt.hashpw("123", hashed)
# print(hashed, hashed2)
# if hashed2 == hashed:
#     print("It matches")
# else:
#     print("It does not match")

import bcrypt

password = "password1234#$"
hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
print(type(hashed_password))
# When verifying, you also use bytes
entered_password = "password1234#$"
if bcrypt.checkpw(entered_password.encode('utf-8'), hashed_password):
    print("Password is correct.")
else:
    print("Password is incorrect.")
