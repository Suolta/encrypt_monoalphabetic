print("Script to encrypt the way monoalphabetic..!?")
#list letters
letters = [
  "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"
] 
# list keys
key = [
  "m","n","b","v","c","x","z","l","j","k","h","g","f","d","s","a","p","o","i","u","y","t","r","e","w","q"
]
#input text
text = str(input("Enter your text>>  ")).lower()
#list
test = []
#loop 
for l in text:
  key_number = letters.index(l) 

  new_letter = key[key_number] 

  test.append(new_letter)
encrypt_text = ''.join(test)

print(encrypt_text)

