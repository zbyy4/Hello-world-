#Invite some people.
guests = ['mike','tom','jerry',]
name = guests[0].title()
print(name + ", please come to dinner.")
name = guests[1].title()
print(name + ", please come to dinner.")
name = guests[2].title()
print(name + ", please come to dinner.")

#Tom can't make it! Let's invite Amy.
name = guests[1].title()
print("\nSorry, " + name + " can't make it to dinner.")
del guests[1]
guests.insert(1,'amy')

#Print the invitation again.
name = guests[0].title()
print("\n" + name + ", please come to dinner.")
name = guests[1].title()
print(name + ", please come to dinner.")
name = guests[2].title()
print(name + ", please come to dinner.")

#We got a big table!
print("\nWe got a big table!")
guests.insert(0,'dick')
guests.insert(2,'pig')
guests.append('jack')

name = guests[0].title()
print(name + ", please come to dinner.")
name = guests[1].title()
print(name + ", please come to dinner.")
name = guests[2].title()
print(name + ", please come to dinner.")
name = guests[3].title()
print(name + ", please come to dinner.")
name = guests[4].title()
print(name + ", please come to dinner.")
name = guests[5].title()
print(name + ", please come to dinner.")

#Oh,no! The table won't arrive on time
print("\nSorry, we can only invite two people to dinner.")
name = guests.pop()
print("Sorry, " + name.title() + ", there is no room at table.")
name = guests.pop()
print("Sorry, " + name.title() + ", there is no room at table.")
name = guests.pop()
print("Sorry, " + name.title() + ", there is no room at table.")
name = guests.pop()
print("Sorry, " + name.title() + ", there is no room at table.")

#There should be two people left.
name = guests[0].title()
print(name + ", please come to dinner.")
name = guests[1].title()
print(name + ", please come to dinner.")

#Empty the list
del(guests[0])
del(guests[0])

#Prove the list is empty
print(guests)
