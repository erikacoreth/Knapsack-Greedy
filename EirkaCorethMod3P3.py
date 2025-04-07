#ErikaCoreth
#knapsack-greedy approach

def knapsack(v, w, cap):
    rwv = [] #triplet: ratio, weight(vol), value, index
    for i in range(len(v)):
        rwv.append([v[i]/w[i], w[i], v[i], i]) #value/vol, vol, value, index
    rwv.sort(reverse=True) #sort from high to low rate
    ans = [] #the list of added items
    tw = 0 #total weight(volume)
    found = True

    while found: #until no fitting item is found
        found = False
        for t in rwv: #search for an item to add
            if (t[1] + tw) <= cap: #if the item fits
                ans.append(t[3]) #store the index
                tw += t[1]
                found = True
                break
    return ans

def main():
    filename = "items.csv" #imported items list
    capacity = int(input("Enter maximum volume (in cubic inches): "))

    names, values, weights = [], [], []

    with open(filename, 'r') as file: #read only for file
        for line in file:
            parts = line.strip().split(',')
            if len(parts) == 5: #if 5 items in the list
                name = parts[0] #first part of list is name
                value = int(parts[1]) #2nd is the value
                h = int(parts[2]) #3rd is the height
                w = int(parts[3]) #4th is the weight
                d = int(parts[4]) #5th is the depth
                volume = h * w * d #volume is equal to h*w*d and this we will use to do val/vol

                names.append(name)
                values.append(value)
                weights.append(volume)

    answer = knapsack(values, weights, capacity)

    ans = {}
    tv = 0
    tw = 0

    for a in answer:
        name = names[a]
        ans[name] = ans.get(name, 0) + 1
        tv += values[a]
        tw += weights[a]

    if ans:
        summary = [f"{count} {name}{'s' if count > 1 else ''}" for name, count in ans.items()]
        print(f"\nThe suggested items are: {', '.join(summary)} with a total value of ${tv}.")
    else:
        print("\nNo items could fit within the given volume.")

    leftover = capacity - tw
    print(f"There were {leftover} cubic inches left unused.")

main()