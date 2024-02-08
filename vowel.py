#wap to check whether the entered character is a vowel or not.
def vowel(): 
    char = input('Enter a character: ')  
    if ((char == 'a') or (char == 'e') or (char == 'i') or \
        (char == 'o') or (char == 'u')):  
        print ('The character is Vowel')  
    else:    
        print ('The character is Consonant')    
vowel() 