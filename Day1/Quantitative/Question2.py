problems,ar,al,ge=80,40,30,10
arAnswered=(80/100)*ar
alAnswered=(60/100)*al
geAnswered=(50/100)*ge
problemsAnswered=(arAnswered+alAnswered+geAnswered)
percentage=(problemsAnswered/problems)*100
percentageRequired=75-percentage
toAnswer=(percentageRequired/100)*80
print("John must have attempted",int(toAnswer),"more question correctly.")
