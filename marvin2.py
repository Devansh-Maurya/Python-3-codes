paranoid_android='Marvin,the Paranoid Android'
letters=list(paranoid_android)

for char in letters[:6]:
    print('\t',char)

for char in letters[11:19]:
    print('\t'*2,char)

for char in letters[20:]:
    print('\t'*3,char)
