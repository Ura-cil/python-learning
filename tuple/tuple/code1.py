t=("india","pak","russia","america","china")
temp=list(t)
temp.append("italy")
temp.pop(1)
temp[2]="fin"
t=tuple(temp)

print(t)