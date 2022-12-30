def translation(paragraph):
    translated=""
    for letter in paragraph:
        if letter=="a":
            translated=translated+"g"
        else:
            translated=translated+letter
    return translated            
paragraph=input("Enter any word to convert a letter into g:")
print(translation(paragraph))
            

