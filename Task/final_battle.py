player = {""
          "hp": 0, 
          "damage": 20}

monster = {"name": "Orc", "hp": 60, "damage": 15}

while player["hp"] > 0 and monster["hp"]>0:

  print(player["hp"], monster["hp"])
  
  monster["hp"] -= player["damage"]
  
  if monster["hp"] > 0:
    player["hp"] -= monster["damage"]
    
else:
  print(player["hp"], monster["hp"])

