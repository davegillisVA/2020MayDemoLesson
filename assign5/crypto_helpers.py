ALPHABET = 'abcdefghijklmnopqrstuvwxyz'


def inEngAlpha(instring):
#    chars = instring.split()
#    print(chars)
    for item in instring:
        if item.lower() not in ALPHABET:
            return False
        elif item == " ":
            return False
        else:
            return True
        
def shift_char(instring, offset):
    if len(instring) != 1:
        print("Error: Instring > one character")
    else:
        if inEngAlpha(instring):
            return ALPHABET[(ALPHABET.index(instring)+offset)%26]
        else:
            return instring

def get_keys(instring):
    indexlist = []
    for count in range(len(instring)):
        indexlist.append(ALPHABET.index(instring[count]))
    return indexlist


def pad_keyword(instring, n):
    if len(instring) < n:
        outstring = instring*n
        outstring = outstring[:n]
    elif len(instring) == n:
        outstring = instring
    else:
        outstring = instring[:n]
    return outstring

def main():
   keylist = []
   validPhrase = True
   phrase = input("Enter your phrase to encode: ")
   print(validPhrase)
   if validPhrase:
       phrase = phrase.lower()
       eval = shift_char(phrase[0], 6)
       print(eval)
       #keylist = get_keys(phrase)
       #print(keylist)
       #keyword = pad_keyword(phrase, 6)
       #print(keyword)
    
main()



