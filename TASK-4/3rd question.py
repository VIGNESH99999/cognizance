k = int(input("Give The Number of Students : "))

x = [["Roll Number", "Name", "Scored marks"]]

for i in range(k):

      Roll = input("Give Roll Number : ")
      name = input("Give Student Name : ")
      score = int(input("Give Scored marks : "))

      x.append([Roll , name, score])

for i in range(len(x)):

    for j in range(len(x[i])):
        r = x[i][j]

        print(r, end='\t')

    print('\n')

l = int(input("which row should be displayed : "))

for i in x[l]:
    print(i, end='\t')