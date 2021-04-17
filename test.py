from sklearn.ensemble import RandomForestClassifier

trainlist=[]
testlist=[]
class Domain:
    def __init__(self,_name,_label):
        self.name=_name
        self.label=_label
    def returnData(self):
        sum=0
        for i in range(len(self.name)):
            if (ord(self.name[i]) in range(48,58)):
                sum=sum+1

        return [len(self.name),sum/len(self.name)]
    def returnLabel(self):
        if self.label=="notdga":
            return 0
        else:
            return 1

def initData(myfile,mylist,type):
    with open(myfile) as f:
        for line in f:
            line=line.strip()
            if (type==0):
               tokens=line.split(",")
               name=tokens[0]
               label=tokens[1]
            else:
              if (type == 1):
                 name = line
                 label ="unknown"
            mylist.append(Domain(name,label))

def WriteData(myfile,mylist1,mylist2):
    with open(myfile,'w') as f:
        for i in range(len(mylist2)):
            f.write(str(mylist1[i]))
            f.write(",")
            if (mylist2[i]==0):
                f.write("notdga\n")
            else:
                f.write("dga\n")


if __name__=='__main__':
    initData("train.txt",trainlist,0)
    initData("test.txt",testlist,1)
    feature1=[]
    labelList1=[]
    for item in trainlist:
        feature1.append(item.returnData())
        labelList1.append(item.returnLabel())
    clf= RandomForestClassifier(random_state=0)
    feature2 = []
    labelList2 = []
    Name2=[]
    for item in testlist:
        feature2.append(item.returnData())
        Name2.append(item.name)


    clf = RandomForestClassifier(random_state=0)
    clf.fit(feature1,labelList1)
    labelList2=clf.predict(feature2)

    WriteData("result.txt",Name2,labelList2)




