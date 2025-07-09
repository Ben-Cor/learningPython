# # 8 ball code
#
# name = input("Hello, what is your name?")
# while name == "":
#     name = input("You didn't enter a name, please enter your name: "
#                  "If you wish to exit, please type exit and press enter: ")
# if name.lower() == "exit":
#     print("Goodbye!")
#     exit()
#
#
# question = input(f"Hello {name}. What question do you want to ask the 8 ball? ")
# while question == "":
#     question = input(f"You didn't ask a question, {name}. Please ask a question for the 8 ball. "
#                      "If you wish to exit, please type exit and press enter: ")
# if question.lower() == "exit":
#     print("Goodbye!")
#     exit()
#
# import random
# random_number = random.randint(1, 9)
#
# match random_number:
#     case 1:
#         answer = "Yes - definitely."
#     case 2:
#         answer = "It is decidedly so."
#     case 3:
#         answer = "Without a doubt."
#     case 4:
#         answer = "Reply hazy, try again."
#     case 5:
#         answer = "Ask again later."
#     case 6:
#         answer = "Better not tell you now."
#     case 7:
#         answer = "My sources say no."
#     case 8:
#         answer = "Outlook not so good."
#     case 9:
#         answer = "Very doubtful."
#     case default :
#         answer = "Error: Invalid response."
#
# print(f"{name}, you asked - {question}. The 8 ball says: {answer}")
#
#
# weight = input("How much does your parcel weigh?")
#
# while True:
#     if weight.lower() == "exit":
#         print("Goodbye!")
#         exit()
#
#     # Check if it's a valid number (either integer or float)
#     try:
#         # Try to convert to float
#         weight_float = float(weight)
#         weight = weight_float
#         break  # Exit the loop if conversion succeeds
#     except ValueError:
#         # If conversion fails, ask for input again
#         weight = input("Invalid input. Please enter a valid weight (number), or type 'exit' to quit: ")
#
# cost = 0
# # Ground shipping
# if weight <= 2:
#   cost = (weight * 1.5) + 20
# elif weight <= 6:
#   cost = (weight * 3) + 20
# elif weight <= 10:
#   cost = (weight * 4) + 20
# else:
#   cost = (weight * 4.75) + 20
#
# print(f"Total cost (Ground) = ${cost:.2f}")
# #premium is a flat rate
# print("Premium cost (Ground) = $125")
#
# #Drone Shipping
#
# drone_cost = 0
# if weight <= 2:
#   drone_cost = (weight * 4.5)
# elif weight <= 6:
#   drone_cost = (weight * 9)
# elif weight <= 10:
#   drone_cost = (weight * 12)
# else:
#   drone_cost = (weight * 14.25)
#
# print(f"Total cost (Drone) = ${drone_cost:.2f}")

# string methods
authors = "Audre Lorde,Gabriela Mistral,Jean Toomer,An Qi,Walt Whitman,Shel Silverstein,Carmen Boullosa,Kamala Suraiyya,Langston Hughes,Adrienne Rich,Nikki Giovanni"

author_names = authors.split(',')

print(author_names)

author_last_names = []
for name in author_names:
  author_last_names.append(name.split()[-1])

print(author_last_names)

reapers_line_one_words = ["Black", "reapers", "with", "the", "sound", "of", "steel", "on", "stones"]

reapers_line_one = ' '.join(reapers_line_one_words)

winter_trees_lines = ['All the complicated details', 'of the attiring and', 'the disattiring are completed!', 'A liquid moon', 'moves gently among', 'the long branches.', 'Thus having prepared their buds', 'against a sure winter', 'the wise trees', 'stand sleeping in the cold.']

winter_trees_full = "\n".join(winter_trees_lines)

love_maybe_lines = ['Always    ', '     in the middle of our bloodiest battles  ', 'you lay down your arms', '           like flowering mines    ','\n' ,'   to conquer me home.    ']

love_maybe_lines_stripped = []
for word in love_maybe_lines:
  love_maybe_lines_stripped.append(word.strip())

love_maybe_full = "\n".join(love_maybe_lines_stripped)
print(love_maybe_full)

toomer_bio = \
"""
Nathan Pinchback Tomer, who adopted the name Jean Tomer early in his literary career, was born in Washington, D.C. in 1894. Jean is the son of Nathan Tomer was a mixed-race freedman, born into slavery in 1839 in Chatham County, North Carolina. Jean Tomer is most well known for his first book Cane, which vividly portrays the life of African-Americans in southern farmlands.
"""
toomer_bio_fixed = toomer_bio.replace('Tomer', 'Toomer')

god_wills_it_line_one = "The very earth will disown you"

disown_placement = god_wills_it_line_one.find("disown")

def poem_title_card(title, poet):
  return "The poem {} is written by {}".format(title, poet)

print(poem_title_card("I Hear America Singing", "Walt Whitman"))

def poem_description(publishing_date, author, title, original_work):
  poem_desc = "The poem {title} by {author} was originally published in {original_work} in {publishing_date}.".format(publishing_date=publishing_date, author=author, title=title, original_work=original_work)
  return poem_desc

my_beard_description = poem_description("1974", "Shel Silverstein", "My Beard", "Where the Sidewalk Ends")

highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"

print(highlighted_poems)

highlighted_poems_list = highlighted_poems.split(",")
print(highlighted_poems_list)

highlighted_poems_stripped = []
for poem in highlighted_poems_list:
  highlighted_poems_stripped.append(poem.strip())

print(highlighted_poems_stripped)