entrada = int(raw_input())
while entrada > 0:
        

    linha1 = raw_input().split()
    linha3 = raw_input().split()
    linha5 = raw_input().split()
    linha7 = raw_input().split()
    linha9 = raw_input().split()


    tijolo37 = int(linha9[0])
    tijolo38 = (int(linha7[0]) - tijolo37 - int(linha9[1])) / 2
    tijolo39 = int(linha9[1])
    tijolo29 = tijolo37 + tijolo38
    tijolo30 = tijolo38 + tijolo39

    tijolo40 = (int(linha7[1]) - tijolo39 - int(linha9[2])) / 2
    tijolo41 = int(linha9[2])
    tijolo31 = tijolo39 + tijolo40
    tijolo32 = tijolo40 + tijolo41

    tijolo42 = (int(linha7[2]) - tijolo41 - int(linha9[3])) / 2
    tijolo43 = int(linha9[3])
    tijolo33 = tijolo41 + tijolo42
    tijolo34 = tijolo42 + tijolo43

    tijolo44 = (int(linha7[3]) - tijolo43 - int(linha9[4])) / 2
    tijolo45 = int(linha9[4])
    tijolo35 = tijolo43 + tijolo44
    tijolo36 = tijolo44 + tijolo45

    tijolo22 = int(linha7[0])
    tijolo23 = (int(linha5[0]) - tijolo22 - int(linha7[1])) / 2
    tijolo24 = int(linha7[1])
    tijolo16 = tijolo22 + tijolo23
    tijolo17 = tijolo23 + tijolo24

    tijolo25 = (int(linha5[1]) - tijolo24 - int(linha7[2])) / 2
    tijolo26 = int(linha7[2])
    tijolo18 = tijolo24 + tijolo25
    tijolo19 = tijolo25 + tijolo26

    tijolo27 = (int(linha5[2]) - tijolo26 - int(linha7[3])) / 2
    tijolo28 = int(linha7[3])
    tijolo20 = tijolo26 + tijolo27
    tijolo21 = tijolo27 + tijolo28

    tijolo11 = int(linha5[0])
    tijolo12 = (int(linha3[0]) - tijolo11 - int(linha5[1])) / 2
    tijolo13 = int(linha5[1])
    tijolo7 = tijolo11 + tijolo12
    tijolo8 = tijolo12 + tijolo13

    tijolo14 = (int(linha3[1]) - tijolo13 - int(linha5[2])) / 2
    tijolo15 = int(linha5[2])
    tijolo9 = tijolo13 + tijolo14
    tijolo10 = tijolo14 + tijolo15

    tijolo4 = int(linha3[0])
    tijolo5 = (int(linha1[0]) - tijolo4 - int(linha3[1])) / 2
    tijolo6 = int(linha3[1])

    tijolo2 = tijolo4 + tijolo5
    tijolo3 = tijolo5 + tijolo6

    tijolo1 = int(linha1[0])

    print tijolo1
    print tijolo2,tijolo3
    print tijolo4,tijolo5,tijolo6
    print tijolo7,tijolo8,tijolo9,tijolo10
    print tijolo11,tijolo12,tijolo13,tijolo14,tijolo15
    print tijolo16,tijolo17,tijolo18,tijolo19,tijolo20,tijolo21
    print tijolo22,tijolo23,tijolo24,tijolo25,tijolo26,tijolo27,tijolo28
    print tijolo29, tijolo30, tijolo31, tijolo32, tijolo33, tijolo34, tijolo35, tijolo36
    print tijolo37, tijolo38, tijolo39, tijolo40, tijolo41, tijolo42, tijolo43, tijolo44, tijolo45
    entrada -= 1
    
