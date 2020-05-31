def Menu(List):
    def Clear():
        for Val in range(100):
            print("")

    ListToShow=[]
    ListToShow.append([])

    GroupCounter=0

    for Val in List:
        ListToShow[GroupCounter].append(Val)

        if len(str(len(ListToShow[GroupCounter])/6))==3:
             if str(len(ListToShow[GroupCounter])/6)[-1]=="0":
                 GroupCounter+=1
                 ListToShow.append([])

    GroupCounterToShow=0
    while True:
        Clear()

        OptionCounter=1
        for Val in ListToShow[GroupCounterToShow]:
            if str(Val)[0]=="<" and str(Val)[-1]==">":
                print(str(OptionCounter)+")"+str(Val.Name))
                OptionCounter+=1

            else:
                print(str(OptionCounter)+")"+str(Val))
                OptionCounter+=1

        IsPreShow=1
        IsNextShow=1

        if GroupCounterToShow==0:
            IsPreShow=0

        if GroupCounterToShow==len(ListToShow)-1:
            IsNextShow=0

        if IsPreShow==1:
            print("\n7)Previous")

        else:
            print("\n")

        if IsNextShow==1:
            print("8)Next")

        else:
            print("")

        print("9)Cancel")

        OptionInput=int(input("\n:"))

        if OptionInput==7 and IsPreShow==1:
            GroupCounterToShow-=1
            continue

        elif OptionInput==8 and IsNextShow==1:
            GroupCounterToShow+=1
            continue

        elif OptionInput==9:
            return 0

        elif OptionInput>0 and OptionInput<OptionCounter:
            return List[GroupCounterToShow*6+OptionInput-1]
