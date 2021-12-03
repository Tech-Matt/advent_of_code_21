#input file
input_file = r"C:\Users\TechMatt\Documents\Programming\Python\advent_of_code\day_1\input.txt"

sum = 0 #sum of increasing triplets (Output)


elements = []
# value = 0
value2 = 0
with open(input_file, "r") as f:
    elements = [int(x) for x in f] #all numbers
    list_triplets = []
    n = 0 #variable to iterate through elements
    i = 1 #useful to initialite triplets
    tripl = 0 #single triplet

    #General idea of the algorithm: Use variable i to sum 3 consecutive numbers from elements, and then add the
    #variable tripl to list_triplets.
    while n < len(elements):
        if (i % 4 == 0): #Triplets are 3 in lenght
            list_triplets.append(tripl)
            tripl = 0
            i = 1
            n = n - 2 #Go with the next triplet

        tripl += elements[n]
        i += 1
        n += 1
    
    list_triplets.append(tripl) #add the last triplet

    value = list_triplets[0] #Take first element

    for j in range(1, len(list_triplets)):
        value2 = list_triplets[j]
        if (value2 > value):
            sum += 1
        value = value2

print(sum)