print("Let's play a game of MadLibs! \nFill in the needed words and see your crazy story come to life.")
name = input("\nWhat's your name: ")
print("\nExcellent " + name +"! Now let's play!")

relative1 = input("\nFirst, enter a relative: ")
adj1 = input("\nGreat! Now enter an adjective: ")
adj2 = input("\nEnter another adjective: ")
adj3 = input("\nEnter an adjective: ")
person_in_room1 = input("\nNow, name a person in the room: ")
adj4 = input("\nEnter an adjective: ")
adj5 = input("\nGreat! Enter one more adjective: ")
verb_ed1 = input("\nEnter a verb that ends in -ed: ")
body_part = input("\nNow, Enter a body part: ")
verb_ing1 = input("\nEnter a verb that ends in -ing: ")
n_plural1 = input("\nEnter a plural noun: ")
n1 = input("\nEnter a noun: ")
adverb1 = input("\nNext, you need to enter an adverb: ")
verb1 = input("\nEnter a verb: ")
verb2 = input("\nEnter a second verb: ")
relative2 = input("\nEnter one more relative: ")
person_in_room2 = input("\nLastly, enter a person in the room: ")

lib = """\nDear {},
\nI am having a(n) {} time at camp. The counselour is {} and the food is {}. I met {} and we became {} friends. Unfortunately,
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
