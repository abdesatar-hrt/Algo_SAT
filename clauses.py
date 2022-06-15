import re
def read_clauses(path):
    clauses = []

    try:
        file = open(path,"r")

        clauses_lines = False

        for line in file:
            if line.startswith("p"):
                clauses_lines = True
                continue

            if clauses_lines:                    
                # removing trailing spaces, removing last 0 items and converting to number
                clause = [int(s) for s in re.split('[\s]+',line.strip())][:-1] 

                clauses.append(clause)            

        file.close()       

    except IOError:
        print("Can not find input file or read data")
        exit()

    return clauses