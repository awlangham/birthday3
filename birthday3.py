import random
random.seed(42)

num_people = 10
num_sims = 10000
runs = [None]*num_sims
  
def getBirthdays(people):
  for n in range(people):
    birthdays[n] = random.randrange(365)
  if any(birthdays.count(x) > 2 for x in birthdays):
  #if len(set(birthdays)) == len(birthdays):
      return(1)
  else:
      return(0)

while True:
  birthdays = [None]*num_people

  for run in range(num_sims):
    runs[run] = getBirthdays(num_people)
    
  odds = runs.count(1)/num_sims
  print(odds)
  
  input("Press ENTER to try " + str(num_people+1) + " people...")
  num_people += 1