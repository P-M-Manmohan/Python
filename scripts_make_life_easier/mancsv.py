import csv
import operator as op

def exctract_from_csv(file,fields):
    list_len=len(fields)
    lis=[]
    for i in range(list_len):
        lis.append([])
    #print(list)
    with open (file,mode='r') as csv_file:
        csv_reader=csv.reader(csv_file)
        header=next(csv_reader)
        field=[]
        for i in fields: 
            field.append(header.index(i))
        print(field)
        group=list(zip(field, range(list_len)))
        for k in group:   
            print(k)
            i=k[0]
            j=k[1]
            for row in csv_reader:
               lis[j].append(row[i])
    print(lis)
    for i in range(len(lis[0])):
         print(lis[0][i])
    positive=op.countOf(lis[1],"Positive")
    print(positive, (len(lis[1])-positive))


if __name__=="__main__":
    exctract_from_csv("onlinefoods.csv",['Monthly Income','Feedback'])