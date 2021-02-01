matsedel = [
  [
    "Kebabgryta med ris",
    "Oumphchili med ris"
  ],
  [
    "Pastagratäng med kyckling och örter",
    "Pastagratäng med oump och örter"
  ],
  [
    "Panerad fisk med remouladsås och potatismos",
    "Morotsbiff med remouladsås och potatismos"
  ],
  [
    "Chili con carne med ris",
    "Chili med bönor och ris"
  ],
  [
    "Fläskkarre med rostad potatis och aioli",
    "Quornfile med rostad potatis och aioli"
  ]
]

dag = 0
dagar = ["måndag", "tisdag", "onsdag", "torsdag", "fredag"]

for mat in matsedel:
  print(f"-- {dagar[dag].capitalize()} --")
  print(f"Dagens köttis: {mat[0]}")
  print(f"Dagens veggis: {mat[1]}\n")
  dag += 1