import string

def ispangram(str1, alphabet=string.ascii_lowercase):
    check = False
    for letter in alphabet:
        if letter in str1:
          check = True
        else:
          check= False
          break
        
      
    print(check)
            
ispangram("The quick brown fox jumps over the lazy dog")