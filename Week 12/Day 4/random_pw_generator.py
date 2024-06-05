'''
How long should the password be?: 10
Your new password is: Ne4ifKclF0

How long should the password be?: 20
Your new password is: DPK2qwikrefxpyW580u4

How long should the password be?: 30
Your new password is: FHjsCYKqGh7i6NwL00SEOdbm5AfRvV
'''

import random

pw_length = int(input("How long should the password be?: "))
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMOPQRSTUVWXYZ1234567890"
password = ""

for i in range(pw_length):
    password += characters[random.randrange(len(characters))]

print(f"Your new password is: {password}")