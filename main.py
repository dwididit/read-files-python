from slash_null_sig import slash_null_sig
import csv
import json

compromised_users = []
with open("password.csv") as password_file:
    password_csv = csv.DictReader(password_file)
    compromised_users = []
    for password_row in password_csv:
        username_compromised = password_row["Username"]
        compromised_users.append(username_compromised)

with open("compromised_users.txt", "w") as compromised_users_file:
    for user in compromised_users:
        compromised_users_file.write(f"{user}\n")

boss_message_dict = {
    "recipient" : "The Boss",
    "message": "Mission Success"
}
with open("boss_message.json", "w") as boss_message:
    json.dump(boss_message_dict, boss_message)

with open("new_passwords.csv", "w") as new_passwords_obj:
    new_passwords_obj.write(slash_null_sig)


