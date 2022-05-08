import string

alphabets = string.ascii_lowercase + string.ascii_lowercase

sentence = list(input('Enter your text: \n').lower())

what_to_do = input(
    'Enter encrypt to ENCRYPT, decrypt to DECRYPT, exit to EXIT the program \n').lower()

shift_number = int(input('Enter your shift number  3: \n'))

end_program = False

while not end_program:
    # search through the enter text
    if what_to_do == 'encrypt':
        for i in range(len(sentence)):
            # get the position of each character within the sentence
            if sentence[i] == ' ':
                sentence[i] = ' '
            elif shift_number==3 :
                
                new_letter = alphabets.index(sentence[i]) + shift_number
                sentence[i] = alphabets[new_letter]
                   
            else:
                print("try agin")
                
                   
        # convert the list back to a string
        print(''.join(map(str, sentence)))
        end_program = True
    elif what_to_do == 'decrypt':
        for i in range(len(sentence)):
            if sentence[i] == ' ':
                sentence[i] = ' '
            elif shift_number==3:
                new_letter = alphabets.index(sentence[i]) - shift_number
                sentence[i] = alphabets[new_letter]
            else:
                print("try agin")
            # convert the list back to a string
        print(''.join(map(str, sentence)))
        end_program = True
    else:
        decide = input(
            'invalid entry, try again Y for YES, N for NO: \n').lower()
        if decide == 'y':
            sentence = list(input('enter your text: \n').lower())
            what_to_do = input(
                'enter encrypt to ENCRYPT, decrypt to DECRYPT, exit to EXIT the program \n').lower()
            shift_number = int(input('enter your shift number from 3: \n'))
        else: 
            end_program = True