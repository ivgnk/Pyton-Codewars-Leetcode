vowel = "aeiouAEIOU"
def replace_exclamation(st):
    st1 =list(st)
    for i,s in enumerate(st1):
        if s in vowel: st1[i] = "!"
    return ''.join(st1)

# Bet of Codewars
# def replace_exclamation(s):
# 	for i in "aeuioAEUIO":	s = s.replace(i, "!")
# 	return s

print(replace_exclamation("Hi!"))
print(replace_exclamation("ABCDE"))