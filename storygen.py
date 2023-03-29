import random


places = ['forest', 'beach', 'mountain', 'cave']
actions = ['hiking', 'swimming', 'exploring', 'camping']
adjectives = ['beautiful', 'mysterious', 'dangerous', 'enchanting']


def generate_story():
    
    place = random.choice(places)
    action = random.choice(actions)
    adjective = random.choice(adjectives)


    story = f"Once upon a time, there was a group of adventurers who went to the {place}. They were {action} when they stumbled upon a {adjective} sight. They couldn't believe their eyes and decided to investigate further. As they got closer, they realized that it was a {adjective} {place} that nobody had ever discovered before!"

    print(story)


generate_story()
