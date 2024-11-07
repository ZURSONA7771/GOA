
alphabet = 'abcdefghijklmnopqrstuvwxyz'

def name(bot):
    next = bot[0].lower()
    if next in alphabet:
        finish = alphabet.index(next) + 1
        return f"first letter of the game'{next}' is {finish}  in alphabet order."
    else:
        return 'the frist letter of  the name is not letter of the alphabet..'
    
bot = input('enter your name:')
print(name(bot))




