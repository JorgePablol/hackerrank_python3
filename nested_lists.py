#NESTED LISTS:
    
    #Given the names and grades for each student in a class of N students, store them in a nested list and
    #print the name(s) of any student(s) having the second lowest grade.
    #Link = https://www.hackerrank.com/challenges/nested-list/problem

if __name__ == '__main__':
    n = int(input())
    names_and_marks = []
    marks_only = []

    for i in range(n):
        name = input()
        marks = float(input())
   
        names_and_marks += [[name,marks]]
        marks_only += [marks]  
   
    marks_only = list(set(marks_only))   
    marks_only = sorted(marks_only)
    second_lowest_mark = marks_only[1]

    for n,s in sorted(names_and_marks):
        if s == second_lowest_mark:
            print(n)
