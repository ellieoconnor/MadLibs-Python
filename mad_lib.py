"""Let's play a game of MadLibs!
Fill in the needed words and see your crazy story come to life."""

relative1 = input("First, enter a relative: ")
adj1 = input("Great! Now enter an adjective: ")
adj2 = input("Enter another adjective: ")
adj3 = input("Enter an adjective: ")
person_in_room1 = input("Now, name a person in the room: ")
adj4 = input("Enter an adjective: ")
adj5 = input("Great! Enter one more adjective: ")
verb_ed1 = input("Enter a verb that ends in -ed: ")
body_part = input("Now, Enter a body part: ")
verb_ing1 = input("Enter a verb that ends in -ing: ")
n_plural1 = input("Enter a plural noun: ")
n1 = input("Enter a noun: ")
adverb1 = input("Next, you need to enter an adverb: ")
verb1 = input("Enter a verb: ")
verb2 = input("Enter a second verb: ")
relative2 = input("Enter one more relative: ")
person_in_room2 = input("Lastly, enter a person in the room: ")

lib = """Dear {},\n
I am having a(n) {} time at camp. The counselour is {} and the food is {}. I met {} and we became {} friends. Unfortunately,
{} is {} and I {} my {} so we couldn't go {} like everybody else. I need more {} and a {} sharpener, so please {} {} more when you
{} back.\n
Your {},\n
{}""".format(relative1,
             adj1,
             adj2,
             adj3,
             person_in_room1,
             adj4,
             person_in_room1,
             adj5,
             verb_ed1,
             body_part,
             verb_ing1,
             n_plural1,
             n1,
             adverb1,
             verb1,
             verb2,
             relative2,
             person_in_room2)
print(lib)
