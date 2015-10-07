from sys import argv

script,user_name = argv
propomt = '>'

print("hello %s ,I'm %s")%(script,user_name)

print("DO you like me %s")%user_name
like = raw_input(propomt)

print('Where do you live')
live = raw_input(propomt)

print("What kind of computer do you have?")
computer = raw_input(propomt)

print("Hello %s you said %s to like me, and you live in %s,coding with %s computer")%(user_name,like,live,computer)
