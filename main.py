sandwiches  = ["grilled cheese", "ruben", "pbj", "philly cheese steak", "cucumber", "tuna melt", "band mi"]

print("these are my sandwiches:")
for sandwich in sandwiches:
    print(f'deliciuos sandwich {sandwich}')




for i in range(len(sandwiches)):
    print(f"{i+1}.{sandwiches[i]}")