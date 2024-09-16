def emoji_converter():
    message = input("Type your message: ")
    separated_words = message.split()
    
    Emoji = {
        ":)": "😊",
        ":(": "😢"
    }
    
    output = ""
    for word in separated_words:
        output += Emoji.get(word, word) + " "
    
    print(output.strip())

emoji_converter()
