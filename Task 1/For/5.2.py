total_jumping_jacks = 100
jumping_jacks_per_set = 10
jumping_jacks_completed = 0

while jumping_jacks_completed < total_jumping_jacks:
    print(f"You have {total_jumping_jacks - jumping_jacks_completed} jumping jacks remaining.")
    
    tired = input("Are you tired? (yes/no): ").lower()
    if tired in ["yes", "y"]:
        skip_remaining = input("Do you want to skip the remaining sets? (yes/no): ").lower()
        if skip_remaining in ["yes", "y"]:
            print(f"You completed a total of {jumping_jacks_completed} jumping jacks.")
            break
    
    # Perform 10 jumping jacks
    for _ in range(jumping_jacks_per_set):
        jumping_jacks_completed += 1
        if jumping_jacks_completed == total_jumping_jacks:
            print("Congratulations! You completed the workout.")
            quit()
        
        # Ask if tired after every set of 10 jumping jacks
        if jumping_jacks_completed % jumping_jacks_per_set == 0:
            tired = input("Are you tired? (yes/no): ").lower()
            if tired in ["yes", "y"]:
                skip_remaining = input("Do you want to skip the remaining sets? (yes/no): ").lower()
                if skip_remaining in ["yes", "y"]:
                    print(f"You completed a total of {jumping_jacks_completed} jumping jacks.")
                    quit()
            else:
                print(f"You have {total_jumping_jacks - jumping_jacks_completed} jumping jacks remaining.")

