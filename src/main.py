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

alphabet = "abcdefghijklmnopqrstuvwxyz"
message = "xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!"

def decoding(alphabet, message, offset):
    output = ""
    for i in range (len(message)):
        if message[i] in alphabet:
            index = alphabet.find(message[i])
            output += alphabet[(index + offset) % 26] # Wrap around using modulo 26
        else:
            output += message[i]
    return output

print(decoding(alphabet, message, 10))

reply = "Hello, world! This is a test message to see if the decoding works correctly."
print(decoding(alphabet, reply, 10))

response = "jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud."
print(decoding(alphabet, response, 10))