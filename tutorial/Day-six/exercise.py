
#? Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
brothers = ('Jacob', 'Michel', 'Josef', 'word')
sisters = ('life', 'Afi', 'love')

siblings = brothers + sisters
print('list of siblings:', siblings)

# How many siblings do you have?
print('The number of siblings i have is :', len(siblings))

# check if Josef is found in you siblings 
check_sibling= 'Josef' in brothers or 'Josef' in sisters
print('The name of brother or sister found is :',check_sibling)

