wo = input()
if((wo>='a' and wo<= 'z') or (wo>='A' and wo<='Z')):
    if(wo=='A' or wo=='a' or wo=='E' or wo =='e' or wo=='I' or wo=='i' or wo=='O' or wo=='o' or wo=='U' or wo=='u'):
        print(wo, "is a Vowel")
    else:
        print(wo, "is a Consonant")
else:
    print("Invalid")
