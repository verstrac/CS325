'''
Implement a function min_Lateness(assinnments)

Sample value for assinnments = [("A",2,2),("B",3,4),("C",1,6),("D",5,7)]
where A, B, C, D are name of assignments
2,3,1,5 represent time timetaken by the assignment
2,4,6,7 represent deadline

Example:
assinnments = [("A",2,2),("B",3,4),("C",1,6),("D",5,7)]
(min_Lateness(assinnments))

would return

(4, ['A', 'B', 'C', 'D'])

4 is the maximum min_Lateness
'''

def main():
    print(min_lateness([("A", 2, 2), ("B", 3, 4), ("C", 1, 6), ("D", 5, 7)]))

def min_lateness(assinnments):
    sorted(assinnments, key=lambda assinnment: assinnment[2])

    start_time = 0
    max_lateness = 0
    schedule = []
    finish_time = 0

    for assignment in assinnments:
        finish_time = start_time + assignment[1]
        if(finish_time > assignment[2]):
            max_lateness = max(max_lateness, finish_time - assignment[2])
        start_time = finish_time
        schedule.append(assignment[0])

    return max_lateness, schedule


if __name__ == '__main__':
    main()