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
        csv_list=list(csv_reader)
        length=len(csv_list)
        for i in fields: 
            field.append(header.index(i))#tkae index of required fields from header
        group=list(zip(field, range(list_len)))#group together the field nad the index of list its values will be enteed into
        for k in group:   
            x=k[0]
            y=k[1]
            for a in range(length):
               csv_file.seek(1)#reseting to begining of csv
               lis[y].append(csv_list[a][x])#input values of each column in each list now only entering one column
    return lis
    for i in range(len(lis[0])):
        for j in range(list_len): 
            print(lis[j][i],end="      ")
        print()


if __name__=="__main__":
    FILE_NAME="onlinefoods.csv"
    FIELDS=['Gender','Occupation','Feedback']
    lis=exctract_from_csv(FILE_NAME,FIELDS)
    for i in range(len(lis[0])):
        for j in range(len(FIELDS)): 
            print(lis[j][i],end="      ")
        print()