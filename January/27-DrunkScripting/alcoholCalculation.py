# Don't drink and drive, no guarantee for correctness -> Today is drunk scripting day

print("how much vodka or other spirits did you drink? (ml)")
ml = input()
print("female or male?")
gender = input()
print("how much do you weight? (kg)")
weight = input()

alc = (0.4* int(ml) * 0.789)

if gender == "female":
    w = alc/float(weight) * 0.6
    print("your bloodalcohol is: "+ str(w) )
if gender == "male":
    w = alc/float(weight) * 0.7
    print("your bloodalcohol is: "+ str(w) )




