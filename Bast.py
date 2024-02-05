from random import choice

def process_name(input_name):
    lower_name = input_name.lower()
    nu_name = lower_name
    if "i am" in lower_name or "my name is" in lower_name:
        nu_name = lower_name.replace("i am ","").replace("my name is ", "")
    return nu_name.title()
        
        
def welcome_message(name):
    return(f"""Welcome to damnation {name.title()}
            \nIn order to be the salvation humanity needs
            \nyou have to guess the password for a nuclear launch code
            \nin order to override the launch process
            \nTo help, we'll leave clues in the form of letters you correctly guess. Good Luck!""")

def main():
    name = input("Who do you say you are? ")
    processed_name = process_name(name)
    print(welcome_message(processed_name))

    words = ['fig', 'tart', 'rihnoceros', 'beetle', 'dolorosa',
            'singularity', 'angel', 'hydrangea', 'spiral',
            'staircase', 'nine', 'ropes', 'polarized', 'light'
            'crow', 'declaration', 'within', 'without', 'purple']

    word = choice(words)

    print("You may begin!")
    
    guesses = ''
    turns = 12
    
    while turns > 0:
        display_string = ' '.join([char if char in guesses else '_' for char in word])
        print(display_string)
        if '_' not in display_string:
            print('\nYou have saved the world')
            break
		
        guess = input('Guess a letter ')
        if len(guess) != 1 or not guess.isalpha():
            print("Do not test the gods, speak only letters as instructed")
        guesses += guess
        if guess not in word:
        	turns -= 1
        	print("Wrong. You dance precariously close to the edge of destruction, child")
        	print("You have", + turns, 'more guesses')
    	
        if turns == 0:
        	print("You have doomed us all")
        	break
        
    
if __name__ == "__main__":
    main()