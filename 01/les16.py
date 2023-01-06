# zip function

friends = ['a', 'b', 'c']
time = [1,2,3]

time_friend = dict(zip(friends,time))

print(time_friend)

for counter, friend in enumerate(friends, start=1):
    print(friend, counter)

print(list(enumerate(friends)))
print(dict(enumerate(friends)))