import hashlib
import sys


def get_user():
    # try to get mail from terminal
    try:
        usermail = sys.argv[1]
        userpass = sys.argv[2]
        return [usermail, userpass]

    except IndexError:
        # if mail is not written on terminal while opening software
        # then check data folder and see cached mail acc
        users_info = ["", ""]
        try:
            data_file = open("data.txt", "r")
            users_info = data_file.read().replace("\n", "").split(":")
        except Exception as e:
            pass

        # if account is not cached then prompt the user to enter email
        if(users_info[0] == "" or users_info[1] == ""):
            mail_input = ""
            pass_input = ""
            while("@" not in mail_input):
                mail_input = input("Enter your E-Mail: ")
                if("@" not in mail_input):
                    print("Wrong E-Mail formatting")
            users_info[0] = mail_input
            while(len(pass_input)<5):
                pass_input = input("Enter your Password: ")
                if(len(pass_input)<5):
                    print("Please enter correct password")
            users_info[1] = pass_input

            # cache file
            data_file = open("data.txt", "w+")
            data_file.write(users_info[0]+":"+users_info[1])
        data_file.close()
        return users_info


# get command line arguments of mail and password
user = get_user();
print(user)