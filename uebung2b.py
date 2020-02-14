print("Gebe dein Alter ein")
Alter=int(input())
if Alter <0:
    print ("bleib realistisch!")

elif Alter <=3:
    print("Du bist ein Baby und definitiv zu jung hierfür!")

elif Alter <=5:
    print("Du bist ein Kleinkind")

elif Alter <=13:
    print("Du bist ein Kind")

elif Alter <=17:
    print("Du bist ein Teenager")

else:
    print("Du bist ein Erwachsener")