from clauses import read_clauses
from solutions import read_solution
from test_satis import check_satisfation
def main():
    
    clauses = read_clauses("bmc-ibm-7.cnf")
    solution = read_solution("test.cnf")

    check_satisfation(clauses,solution)
    


if __name__ == "__main__":
    main()