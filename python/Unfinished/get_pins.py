def get_pins(observed):
  observed_number = [int(i) for i in str(observed)]
  adjacent_number = ["08", "124", "2135", "326", "4157", "52468", "6359", "748", "8057", "968"]
  all_adjacents = []
  pins = []
  for elt in observed_number:
    adjacent_number_list = [elt for elt in adjacent_number[elt]]
    all_adjacents.append(adjacent_number_list)
  for i in range(len(all_adjacents)**len(all_adjacents)):
    print()
  return all_adjacents

print(get_pins("81"))