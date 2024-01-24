import math
import numpy as np

AttackTroops = int(input("Met hoeveel troepen wordt er aangevallen? "))
DefenceTroops = int(input("Met hoeveel troepen wordt er verdedigd? "))

WinChanceAttack = 0
WinChanceDefence = 0

# gezien vanuit aanvallers perspectief
Win = '(-2,0)'
Tie = '(-1,-1)'
Loss = '(0,-2)'
Chances = dict([
    ('3v2(-2,0)', 2275/7776),
    ('3v2(-1,-1)', 2611/7776),
    ('3v2(0,-2)', 2890/7776),
    ('2v2(-2,0)', 581/1296),
    ('2v2(-1,-1)', 420/1296),
    ('2v2(0,-2)', 295/1296),
    ('3v1(-1,0)', 49/144),
    ('3v1(0,-1)', 95/144),
    ('2v1(-1,0)', 91/216),
    ('2v1(0,-1)', 125/216),
    ('1v2(-1,0)', 161/216),
    ('1v2(0,-1)', 55/216),
    ('1v1(-1,0)', 7/12),
    ('1v1(0,-1)', 5/12)
])
AttackOutcomeList = [AttackTroops]
DefenceOutcomeList = [DefenceTroops]
ChancesList = [1]
stop = False

# while stop == False:
while stop == False:
    stop = True
    ListLength = len(AttackOutcomeList)
    for n in range(0, len(AttackOutcomeList)):
        if AttackOutcomeList[n] >= 3 and DefenceOutcomeList[n] >= 2:
            for L in [-2, -1, 0]:
                AttackOutcomeList.append(AttackOutcomeList[n]+L)
                DefenceOutcomeList.append(DefenceOutcomeList[n]-(L+2))
                ChancesList.append(Chances['3v2('+str((L)) + ',' + str(-L-2)+')']*ChancesList[n])  
                   
        elif AttackOutcomeList[n] >= 2 and DefenceOutcomeList[n] >= 2:
            for L in [-2, -1, 0]:
                AttackOutcomeList.append(AttackOutcomeList[n]+L)
                DefenceOutcomeList.append(DefenceOutcomeList[n]-(L+2))
                ChancesList.append(Chances['2v2('+str((L)) + ',' + str(-L-2)+')']*ChancesList[n])  
                   
        elif AttackOutcomeList[n] >= 1 and DefenceOutcomeList[n] >= 2:
            for L in [-1, 0]:
                AttackOutcomeList.append(AttackOutcomeList[n]+L)
                DefenceOutcomeList.append(DefenceOutcomeList[n]-(L+1))
                ChancesList.append(Chances['1v2('+str((L)) + ',' + str(-L-1)+')']*ChancesList[n])  
                   
        elif AttackOutcomeList[n] >= 3 and DefenceOutcomeList[n] >= 1:
            for L in [-1, 0]:
                AttackOutcomeList.append(AttackOutcomeList[n]+L)
                DefenceOutcomeList.append(DefenceOutcomeList[n]-(L+1))
                ChancesList.append(Chances['3v1('+str((L)) + ',' + str(-L-1)+')']*ChancesList[n]) 
                
        elif AttackOutcomeList[n] >= 2 and DefenceOutcomeList[n] >= 1:
            for L in [-1, 0]:
                AttackOutcomeList.append(AttackOutcomeList[n]+L)
                DefenceOutcomeList.append(DefenceOutcomeList[n]-(L+1))
                ChancesList.append(Chances['2v1('+str((L)) + ',' + str(-L-1)+')']*ChancesList[n])   
                
        elif AttackOutcomeList[n] >= 1 and DefenceOutcomeList[n] >= 1:
            for L in [-1, 0]:
                AttackOutcomeList.append(AttackOutcomeList[n]+L)
                DefenceOutcomeList.append(DefenceOutcomeList[n]-(L+1))
                ChancesList.append(Chances['1v1('+str((L)) + ',' + str(-L-1)+')']*ChancesList[n])    
                
        else:
            AttackOutcomeList.append(AttackOutcomeList[n])
            DefenceOutcomeList.append(DefenceOutcomeList[n])
            ChancesList.append(ChancesList[n])
    del AttackOutcomeList[:ListLength]
    del DefenceOutcomeList[:ListLength]
    del ChancesList[:ListLength]

    # Maak een dictionary om de overeenkomsten bij te houden
    matching_indices = {}

    # Itereer over de indices van AttackOutcomeList en DefenceOutcomeList
    for i, (val1, val2) in enumerate(zip(AttackOutcomeList, DefenceOutcomeList)):
        # Controleer of de combinatie van val1 en val2 al eerder is gezien
        if (val1, val2) in matching_indices:
            # Als ja, voeg de waarden van list3 toe aan de bestaande index
            existing_index = matching_indices[(val1, val2)]
            ChancesList[existing_index] += ChancesList[i]
        else:
            # Als niet, voeg de huidige index toe aan de dictionary
            matching_indices[(val1, val2)] = i
        if val1 != 0 and val2 != 0:
            stop = False
    # Verwijder de overbodige indices uit de lijsten
    AttackOutcomeList = [AttackOutcomeList[i] for i in matching_indices.values()]
    DefenceOutcomeList = [DefenceOutcomeList[i] for i in matching_indices.values()]
    ChancesList = [ChancesList[i] for i in matching_indices.values()]

for i in range(len(AttackOutcomeList)):
    if DefenceOutcomeList[i] == 0:
        WinChanceAttack += ChancesList[i]
    else:    
        WinChanceDefence += ChancesList[i]
    
print('The chance that the attacker wins is ' + str(100*WinChanceAttack)+'%')
print('The chance that the defender wins is ' + str(100*WinChanceDefence)+'%')
