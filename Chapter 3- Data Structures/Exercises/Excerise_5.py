# Initialize a list of guests for dinner.
guests = ['John D', 'Sean oyean', 'Reingh llyod']

# Generate and print invitations for each guest in title case.
for guest in guests:
    name = guest.title()
    print(f"{name}, please come to dinner.")

# Apologize to Sean oyean, who can't make it to dinner.
name = guests[1].title()
print(f"\nSorry, {name} can't make it to dinner.")

# Substitute Sean oyean with Gary and print updated invitations.
del guests[1]  # Remove Sean oyean from the list
guests.insert(1, 'gary snyder')  # Add Gary to the list
print("\nInvitations after changes:")
for guest in guests:
    name = guest.title()
    print(f"{name}, please come to dinner.")

# Expand the guest list with new attendees.
print("\nWe got a bigger table!")
guests.insert(0, 'frida kahlo')  # Add Frida to the beginning
guests.insert(2, 'reinhold messner')  # Add Reinhold to the middle
guests.append('elizabeth peratrovich')  # Add Elizabeth to the end

# Print invitations for the expanded guest list.
print("\nInvitations for the expanded guest list:")
for guest in guests:
    name = guest.title()
    print(f"{name}, please come to dinner.")
