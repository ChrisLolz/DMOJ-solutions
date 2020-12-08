text = {
    "CU":"see you", 
    ":-)":"I'm happy",
    ":-(":"I'm unhappy", 
    ";-)":"wink",
    ":-P":"stick out my tongue",
    "(~.~)":"sleepy",
    "TA":"totally awesome",
    "CCC":"Canadian Computing Competition",
    "CUZ":"because",
    "TY":"thank-you",
    "YW":"you're welcome",
    "TTYL":"talk to you later"
}
end = False
while end == False:
    read = input()
    if read in text:
        if read == "TTYL":
            print(text[read])
            end = True
        else:
            for i in text:
                if i in read:
                    print(text[read])
    
    else:
        print(read)
