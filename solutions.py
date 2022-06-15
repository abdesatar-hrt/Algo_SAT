def read_solution(path):
    solution = []

    try:
        file = open(path,"r")

        for line in file:
            if line.startswith("v"):
                
                split_solution = line[3:].split(" ")

                for i in range(len(split_solution)):
                    solution.append(split_solution[i])

        # converting list to int and removing last item "0"
        solution = list(map(int, solution))[:-1]

        file.close()       

    except IOError:
        print("Can not find input file or read data")
        exit()

    return solution