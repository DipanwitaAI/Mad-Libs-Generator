def mad_libs_generator():
    print("Welcome to the Mad Libs Generator!")
    
    # Collecting user inputs   
    noun1 = input("Enter a noun: ") 
    noun2 = input("Enter another noun: ") 
    verb1 = input("Enter a verb: ")  
    adjective1 = input("Enter an adjective: ") 
    adjective2 = input("Enter another adjective: ")
    adjective3 = input("Enter another adjective: ")
    adjective4 = input("Enter another adjective: ") 
    adjective5 = input("Enter another adjective: ")
    adjective6 = input("Enter another adjective: ") 
    
    # Story template
    story = f"""
    One day, a {adjective1} {noun1} {verb1} a {noun2} for dinner. {noun2} was very happy with the invitation – she reached the {noun1}’s 
    home on time and knocked at the door with her {adjective2} beak. The {noun1} took her to the dinner table and served some soup in
    {adjective3} bowls for both of them. As the bowl was too {adjective3} for the {noun2}, she couldn’t have soup at all. But, the {noun1}
    licked up his soup quickly.

    The {noun2} was {adjective4} and {adjective5}, but she didn’t show her anger and behaved politely. To teach a lesson to the {noun1}, she
    then invited him for dinner the next day. She too served soup, but this time the soup was served in two tall {adjective6} vases. The {noun2}
    devoured the soup from her vase, but the {noun1} couldn’t drink any of it because of his {adjective6} neck. The {noun1} realised his mistake
    and went home famished
    """
    
    # Displaying the complete story
    print("\nHere is your story:")
    print(story)

# Run the Mad Libs generator
mad_libs_generator()