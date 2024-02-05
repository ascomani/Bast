def is_word(user_word, true_mans_word):
    preview = " ".join([x for x in user_word])
    print(preview)
    
    for i in range(len(user_word)):
        if user_word[i] == true_mans_word[i]:
            print('🟩',end =" ")
        elif user_word[i] in true_mans_word:
            print('🟨',end =" ")
        else:
            print('⬛',end =" ")
    
    if user_word == true_mans_word:
        return 1
    else:
        return 0

print(is_word('tab', 'bat'))