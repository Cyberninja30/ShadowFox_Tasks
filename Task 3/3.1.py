# Justice League members list
justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]

# Task 1: Calculate the number of members in the Justice League.
print("Number of members in the Justice League:", len(justice_league))

# Task 2: Batman recruited Batgirl and Nightwing as new members. Add them to the list.
justice_league.extend(["Batgirl", "Nightwing"])
print("Justice League after adding Batgirl and Nightwing:", justice_league)

# Task 3: Wonder Woman is now the leader. Move her to the beginning of the list.
justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")
print("Justice League after making Wonder Woman the leader:", justice_league)

# Task 4: Separate Aquaman and Flash with another member.
# Here, we choose to move "Superman" between Aquaman and Flash.
justice_league.remove("Superman")
justice_league.insert(justice_league.index("Flash"), "Superman")
print("Justice League after separating Aquaman and Flash:", justice_league)

# Task 5: Replace the existing list with a new team assembled by Superman.
new_team = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
justice_league = new_team
print("Justice League after assembling the new team by Superman:", justice_league)

# Task 6: Sort the Justice League alphabetically.
justice_league.sort()
print("Justice League after sorting alphabetically:", justice_league)

# The hero at the 0th index will become the new leader.
print("New leader of the Justice League:", justice_league[0])
