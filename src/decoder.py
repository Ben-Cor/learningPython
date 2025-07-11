message = "xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!"

def decoding(message, offset):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    output = ""
    for i in range (len(message)):
        if message[i] in alphabet:
            index = alphabet.find(message[i])
            output += alphabet[(index + offset) % 26] # Wrap around using modulo 26
        else:
            output += message[i]
    return output

print(decoding(message, 10))

reply = "Hello, world! This is a test message to see if the decoding works correctly."
print(decoding(reply, 10))

response = "jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud."
print(decoding(response, 10))

response_two = "bqdradyuzs ygxfubxq omqemd oubtqde fa oapq kagd yqeemsqe ue qhqz yadq eqogdq!"
print(decoding(response_two, 14))

response_unknown = "vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx."
for i in range(26):
    decoded_message = decoding(response_unknown, i+1)
    print(f"Offset {i}: {decoded_message}")