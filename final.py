"""
In this program we will write a program that is going to calculate the grades of students for their final exam. 
This program will display the number of grades and also the average grade. 
By reading the final.txt file where the grades are located. 

It will also include the percentage of grades with an above average score. 

In order to begin the program we will have a main function that will start the program. 

"""


"""

def calculate_percent_above_average():
    count= 0 
    for grade in grades:
        grade > average:
            count +=1
    count / grades

def main():
    file = open(final.txt)
    grades = []
    for line in file:
        grades
    average = 0 
    for grades in grades:
        average += grades
    average /= grades
    print (average grades)
    print (percentage of grades above average)
    file.close

main()



"""


def calculate_percent_above_average(grades, average): 
    count = 0 
    for grade in grades:
        if grade > average: 
            count += 1
    return(count * 100) / len(grades)


def main():
    file = open('final.txt')
    grades = []
    for line in file:
        grades.append(int(line.strip()))
    print("Number of grades: ", len(grades))
    average = 0 
    for grade in grades:
        average += grade
    average /= len(grades)
    print("Average grade:", average)
    print("percentage of grades above averge: {:.2f}%".format(calculate_percent_above_average(grades, average)))

main()