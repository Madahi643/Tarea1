import calendar
dias=['MONDAY','TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY','SUNDAY']
m,d,y= map(int,input().split())

f=calendar.weekday(y,m,d)
j=dias[f]
print(j)