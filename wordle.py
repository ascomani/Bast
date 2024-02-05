from random import choice

def wordle(user_word, true_mans_word):
    preview = " ".join([x for x in user_word])
    print(preview)
    
    for i in range(len(user_word)):
        if user_word[i] == true_mans_word[i]:
            print("\033[92m" + '▉' + "\033[0m",end =" ")
        elif user_word[i] in true_mans_word and user_word[i] != true_mans_word[i]:
            print("\033[93m" + '▉' + "\033[0m",end =" ")
        else:
            print("\033[90m" + '▉' + "\033[0m",end =" ")
    
    print()
    
    if user_word == true_mans_word:
        return 1
    else:
        return 0

def main():
    words = ('which', 'there', 'their', 'about', 'would', 'these', 'other', 'words', 'could', 'write', 'first', 'water', 'after', 'where', 'right', 'think')
    word = choice(words)
    print("Take a chance, find out what word I hide")
    message,i  = {0:"Ok",1:"Good",2:"Nice",3:"Very good",4:"Marvellous!",5:"Amazing!!"}, 6

    while i>0:
        user_word = input("\nEnter Word ")
        if (len(user_word) == 5 and user_word.isalpha()):
            i -= 1
            if wordle(user_word, word):
                print("\n",message[i])
                break
            else:
                continue
        else:
            print("Do not test me child! Enter a valid word")
        
    else:
        print("End of Game, the correct word is:",random_word)
    
if __name__ == "__main__":
    main()