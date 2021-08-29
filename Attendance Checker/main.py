import sqlite3
 #connecting to sqlite
conn = sqlite3.connect('data.sqlite')
cur = conn.cursor()

students_list = list()
cur.execute('SELECT * FROM a_batch')
rows = cur.fetchall()
i = 0
for row in rows:
    row_list = list(row)
    students_list.append(row_list)
    students_list[i].append("a")
    i = i + 1

cur.execute('SELECT * FROM b_batch')
rows = cur.fetchall()
i = 50
for row in rows:
    row_list = list(row)
    students_list.append(row_list)
    students_list[i].append("b")
    i = i + 1


print("Enter the attendance list")

#inputing students present
inputs = []
while True:
    inp = input()
    if inp == "":
        break
    inputs.append(inp)

#common students
common_students = []
for i in students_list :
    for j in inputs :
        if( i[1] == j) :
            x =str(i[0]) + " " + i[1]
            common_students.append(x)



#students present in A batch
students_a = []
for i in students_list :
    if(i[2]== 'a') :
        x = str(i[0]) + " " + i[1]
        students_a.append(x)


print("LIST OF ABSENTEES IN A BATCH")

#absentees in A batch
absentees_a = list(set(students_a) - set(common_students))
count_a = len(absentees_a)
f = open("aba.txt", "a")
f.truncate(0)
for i in absentees_a :
    f.write(i)
    f.write("\n")
    print(i)
print("Number of students absent  in A batch = " + str(count_a))

f.close()


# students present in B batch
students_b = []
for i in students_list:
    if (i[2] == 'b'):
        x = str(i[0]) + " " + i[1]
        students_b.append(x)

print("\nLIST OF ABSENTEES IN B BATCH")

#absentees in B batch
absentees_b = list(set(students_b) - set(common_students))
count_b = len(absentees_b)
f = open("abb.txt", "a")
f.truncate(0)
for i in absentees_b:
    f.write(i)
    f.write("\n")
    print(i)
print("Number of students absent in B batch = " + str(count_b))
f.close()

#unidentified students
unknown_list = []
for i in students_list :
    for j in inputs :
        if( i[1] == j) :
            unknown_list.append(j)


print("\nLIST OF UNIDENTIFIED STUDENTS")

#unknown students list
unknown_students = list(set(inputs) - set(unknown_list))
f = open("stun.txt", "a")
f.truncate(0)
for i in unknown_students :
    f.write(i)
    f.write("\n")
    print(i)
f.close()

print("Total number of Absentees : " + str(count_a + count_b))