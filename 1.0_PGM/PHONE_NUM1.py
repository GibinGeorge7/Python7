
#FIND REGULAR EXpression - ALL 12-DIGHIT US PHONE NUMbers from GIVEN string

string2=("""call me at 415-000-4446 mom
and come home to 999-000-3243 and murphy456 also called.
we also want  to seee 9999-234-58568""")

#string2=input("Enter String :\n")
i=0
for word in (string2.split()):
    try:
        if word[3]=='-' and word[7]=='-' and len(word)==12 :
            i += 1
            print("Phone number listed " + str(i) +" : "+ word )
        else:
            continue
    except IndexError:
            continue
