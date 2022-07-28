import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('NBA_Team_Stats2.csv')

print("Shkruani sezonen qe deshironi:")
given_year = input()
#Ne varesi nga inputi i sezones i grupojme top 5 ekipat sipas ati sezoni sipas pikeve
filt=df.groupby("Year")
topfive = filt.get_group(given_year).head(5)

x=list(topfive['Team'])
y=list(topfive['Points'])

#Ato informata i vendosim ne graf per qartim me te lehte
ax=plt.axes()
plt.title('Top 5 Ekipat sipas pikeve,sezoni ' + given_year)
plt.xlabel('Team')
plt.ylabel('Points')
plt.bar(x,y,color='b',ls='-',lw=0.5,width=0.6)
plt.show()

#E formojne edhe nje graf per te treguar top 5 ekipat sipas ofenzives se pergjithshme
PRO=df.sort_values(by='Offensive Overall',ascending=False).head(5)
plt.title('Top 5 Ekipat sipas sulmit ,sezoni ' + given_year)
plt.xlabel('Ekipa')
plt.ylabel('Offensive Overall')
plt.bar(x,y,color='b',ls='--',lw=0.5,width=0.6)
ax.set_facecolor('Black')
plt.show()

#E formojme edhe nje graf per te treguar top 5 ekipat sipad defenzives se pergjithshme

DRBS=df.sort_values(by='Defensive Overall',ascending=False).head(5)
plt.title('Top 5 Ekipat sipas mbrojtjes , sezoni ' + given_year)
plt.xlabel('')
plt.ylabel('Deffensive Overall')
plt.bar(x,y,color='b',ls='--',lw=0.5,width=0.6)
plt.show()

#Best 5 teams average Points per Game team from 1997-2022

print('Best 5 teams average Points per Game team from 1997-2022')
filt=df.sort_values(by='Points',ascending=False).head(5)
print(filt)

#Best defensive team

print("Top 5 all time deffensive team")
DRBS=df.sort_values(by='Defensive Overall',ascending=False).head(5)
print(DRBS)

#Permes inputit i marrim statistikat dhe ekipen dhe e paraqesim ne graf
print('Shkruani ekipen:')
x=input()
print('Shkruani statistiken:')
y=input()
a=df[df['Team']==x]
b=pd.DataFrame(a,columns=['Year',y])
plt.plot(b['Year'],b[y],color='blue',marker='o')
plt.title( x + " " + y + " " + 'from 1997-2022')
plt.xlabel('Year')
plt.ylabel(y)
plt.grid(True)
plt.show()