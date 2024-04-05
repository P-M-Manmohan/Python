import csv
import operator as op

def exctract_from_csv(file,fields):#take fiL and list of columns required
    list_len=len(fields)#find number of columns
    lis=[]
    for i in range(list_len):
        lis.append([])#create empty lists in list to append value of each coloums one list for one column
    with open (file,mode='r') as csv_file:
        csv_reader=csv.reader(csv_file)
        header=next(csv_reader)#take first row (header)
        field=[]
        for i in fields: 
            field.append(header.index(i))#tkae index of required fields from header
        group=list(zip(field, range(list_len)))#group together the field nad the index of list its values will be enteed into
        for k in group:   
            print(k)
            i=k[0]
            j=k[1]
            for row in csv_reader:
               lis[j].append(row[i])#trying to input values of each column in each list now only entering one column
    for i in range(len(lis[0])):
         print(lis[0][i],"\t",print[1][i])
    positive=op.countOf(lis[1],"Positive")
    print(positive, (len(lis[1])-positive))#find numeber of positive and negative feedback


if __name__=="__main__":
    exctract_from_csv("onlinefoods.csv",['Monthly Income','Feedback'])