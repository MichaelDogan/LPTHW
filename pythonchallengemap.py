text_string = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

def code_break(my_string):
    new_string = ""
    for letter in my_string:
        if letter == " ":
            new_string += letter
        else:
            if ord(letter) + 2 > 122:
                my_letter = ord(letter) - 26 + 2
                new_string += chr(my_letter)
            else:
                new_string += chr(ord(letter) + 2)
    return new_string

print code_break(text_string)