from instapy_cli import client

username = "SIGUEME EN INSTAGRAM: davidarmendarizp"

password = "SIGUEME EN INSTAGRAM: davidarmendarizp"

text = '''
SIGUEME EN INSTAGRAM: davidarmendarizp
'''

image = "SIGUEME EN INSTAGRAM: davidarmendarizp.png"

with client(username,password) as cli:
    cli.upload(image,text)
