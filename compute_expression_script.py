

replicates = ["T1A", "T1B", "T1C",
              "T4A", "T4B", "T4C",
              "T6A", "T6B", "T6C",
              "T7A", "T7B", "T7C"]

for i,replicate in enumerate(replicates):
    print(replicate)
    expression = []

    for j in range(16):
        expression.append("c" + str(j + (i * 16) + 1))

    expression = "+".join(expression)
    print(expression)
    #print("(" + expression + "")
    
    
