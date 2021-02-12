import requests

# This function will pass your text to the machine learning model
# and return the top result with the highest confidence
def Genrify(text):
    key = "bddca630-4dd1-11eb-a9dc-4f2f63870dd9c4b11656-fc68-40a5-9408-f88924dd49cc"
    url = "https://machinelearningforkids.co.uk/api/scratch/"+ key + "/classify"

    response = requests.get(url, params={ "data" : text })

    if response.ok:
        responseData = response.json()
        topMatch = responseData[0]
        return topMatch
    else:
        response.raise_for_status()

def Agify(text):
    key = "9d9b8210-4dd1-11eb-a9dc-4f2f63870dd95ee92d40-386c-47d7-8b75-10ebb1fd317b"
    url = "https://machinelearningforkids.co.uk/api/scratch/"+ key + "/classify"

    response = requests.get(url, params={ "data" : text })

    if response.ok:
        responseData = response.json()
        topMatch = responseData[0]
        return topMatch
    else:
        response.raise_for_status()

# CHANGE THIS to something you want your machine learning model to Genrify
search=input("Enter Search Terms:-")
demo = Genrify(search)

genre = demo["class_name"]
confidence1 = demo["confidence"]

demo_age = Agify(search)

age = demo_age["class_name"]
confidence2 = demo_age["confidence"]

# CHANGE THIS to do something different with the result
print ("result: '%s' with %d%% confidence" % (genre, confidence1))
print ("result: '%s' with %d%% confidence" % (age, confidence2))

G_Dict={
    'Platformers':['Sonic Colors','Alto','Kirby','Mario','Mario Galaxy','Sonic','Donkey Kong','Banjo and Kazooie','Crash Bandicoot'],
    'Shooters':['Splatoon','CSGO','Counter Strike 1.6','Call of Duty' , ' Overwatch' , 'Valorant' ,'Paladins' ,'Mass Effect','Gears of War'],
    'Puzzles':['Tetris','Minesweeper','Suduko','Monument Valley','Portal','Monument Valley','Candy Crush SAGA','2048','Angry Birds','The Room','Hello Neighbor'],
    'Open_World':['Assassins Creed','Far Cry','Genshin Impact','Legend of Zelda:Ocarina of Time','Legend of Zelda:Breath of the Wild','GTA 5','Minecraft','Skyrim','Watch Dogs']
    }

A_Dict={
    'E':['Minecraft','Mario','Sonic','Legend of Zelda:Ocarina of Time','Paladins','Donkey Kong','Crash Bandicoot','Angry Birds','Candy Crush SAGA','Alto'],
    'PG13':['Tetris','2048','Hello Neighbor','Portal','Genshin Imapact','Kirby','Splatoon','Overwatch','Valorant','Skyrim'],
    'M':['GTA 5','Assassins Creed','Far Cry','Watch Dogs','CSGO','Call of Duty','Gears of War','Mass of Effect','The Room']
}

G_List=G_Dict[genre]
A_List=A_Dict[age]

print('People who played this game also tried:-')
c=1
for i in G_List:
    print(str(c)+'.'+ i)
    c=c+1

print('People who are in the same age range you also tried:-')
c=1
for i in A_List:
    print(str(c)+'.'+ i)
    c=c+1

