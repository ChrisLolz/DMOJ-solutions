N = int(input())
races = []
for i in range(N):
    race = {}
    line = input().split()
    race['time'] = int(line[0])
    race['pos'] = int(line[1])
    races.append(race)
    
def gettime(dict):
    return dict['time']

races.sort(key=get_time)


maxspeed = None
prevtime = None
prevpos = None

for race in races:
    time = race['time']
    pos = race['pos']
    if prevtime == None:
      prevtime = time
      prevpos = pos
      continue
    diff = time-prevtime
    distance = abs(pos-prevpos)
    speed = distance/diff
  
    if maxspeed == None or speed > maxspeed:
      maxspeed = speed
    prevtime = time
    prevpos = pos
    
print(maxspeed)
