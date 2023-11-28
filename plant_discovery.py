num = int(input())
plants_dict = {}
for _ in range(num):
    plant, rarity = input().split("<->")
    if plant not in plants_dict:
        plants_dict[plant] = {"Rarity": int(rarity), "Rating": []}

commands = input()

while commands != "Exhibition":
    current_command, info = commands.split(": ")
    if current_command == "Rate":
        plant, rating = info.split(" - ")
        rating = float(rating)
        if plant in plants_dict:
            plants_dict[plant]["Rating"].append(rating)
        else:
            print("error")
    elif current_command == "Update":
        plant, new_rarity = info.split(" - ")
        new_rarity = int(new_rarity)
        if plant in plants_dict:
            plants_dict[plant]["Rarity"] = new_rarity
        else:
            print("error")
    elif current_command == "Reset":
        plant = info
        if plant in plants_dict:
            plants_dict[plant]["Rating"] = []
        else:
            print("error")
    commands = input()

print("Plants for the exhibition:")
for types, rating_rarity in plants_dict.items():
    if rating_rarity["Rating"]:
        average_rating = sum(rating_rarity["Rating"]) / len(rating_rarity["Rating"])
    else:
        average_rating = 0
    print(f"- {types}; Rarity: {rating_rarity['Rarity']}; Rating: {average_rating:.2f}")
