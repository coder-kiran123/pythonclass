income = int(input("enter your monthly income from part time work : "))
income1 = int(input("enter your monthly income from full time work : "))
income3= int(input("enter your monthly income from bank intrest : "))


expences= int(input("enter your total expences from food: "))

expences1= int(input("enter your total expences from health: "))

expences3= int(input("enter your total expences from education: "))

expences4= int(input("enter your total expences from travel: "))

expences5= int(input("enter your total expences from other: "))


a= income+ income1+income3
b=expences+expences1+expences3+expences4+expences5

c=a-b

print(f"your total income is rs {a}")
print(f"your total expences is rs {b}")
print(f"your total saving is rs {c}")