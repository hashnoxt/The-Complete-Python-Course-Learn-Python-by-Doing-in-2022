# if one arg have a name all args should have names

# default values can't be changed later

""" Lambda functions """

# Can't use without name

divide = lambda x, y: x / y

print(divide(4, 0))

# can use like

print((lambda x, y: x / y)(1, 4))

# usages

# ave = lambda seq : sum(seq) / len(seq)


