# Invite some people to dinner.
guests = ['John D', 'Sean oyean', 'Reighn llyod']
# Invite the first guest to dinner
name = guests[0].title()
print(f"{name}, please come to dinner.")
# Invite the second guest to dinner
name = guests[1].title()
print(f"{name}, please come to dinner.")
# Invite the third guest to dinner
name = guests[2].title()
print(f"{name}, please come to dinner.")
# Apologize to the second guest who can't make it to dinner
name = guests[1].title()
print(f"\nSorry, {name} can't make it to dinner.")
# Jack can't make it! Let's invite Gary instead.
del(guests[1])
guests.insert(1, 'Sean oyean')
# Print the invitations again.
name = guests[0].title()
print(f"\n{name}, please come to dinner.")
name = guests[1].title()
print(f"{name}, please come to dinner.")
name = guests[2].title()
print(f"{name}, please come to dinner.")
# We got a bigger table, so let's add some more people to the list.
print("\nWe got a bigger table!")
guests.insert(0, 'John D')
guests.insert(1, 'Sean oyean')
guests.append('Reighn llyod')
# Invite the new guests to dinner
name = guests[0].title()
print(f"{name}, please come to dinner.")
name = guests[1].title()
print(f"{name}, please come to dinner.")