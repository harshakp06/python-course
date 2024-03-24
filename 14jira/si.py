if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    


    if query_name in student_marks:
        print(f"{query_name} , is queary name")
        print(student_marks.get(query_name))

        sum = 0

        for i in student_marks.get(query_name):
            # sum = 0
            sum = sum + i
        d = len(student_marks.get(query_name))
        print(float(sum/d))

    else:
        print('enter from below list of names' )
        print(list(student_marks.keys()))

        









    # s = list(student_marks.keys())

    # print(s)
    # print(type(s))

    # print(student_marks.keys())
    # print(type(student_marks.keys()))
        
    # if query_name in list(student_marks.keys()):
    #     print(f"{query_name} , is queary name")
    #     print(list(student_marks[]))
    