def check_satisfation(clauses, solution):
    
    total_clauses = len(clauses)
    total_satistied = 0
    total_non_satisfied = 0

    # iterating over all clauses
    for i in range(len(clauses)):
        
        satistied = False

        for j in range(len(clauses[i])):
                
            if clauses[i][j] in solution:
                satistied = True
        
        if satistied:
            total_satistied += 1
        else:
            total_non_satisfied += 1    
    
    print("Total Clauses: " + str(total_clauses))
    print("Satisfied Clauses: " + str(total_satistied))
    print("Non Satisfied Clauses: " + str(total_non_satisfied))