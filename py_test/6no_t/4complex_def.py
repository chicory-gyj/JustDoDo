#!/usr/bin/python
def init(date):
    date['first']={}
    date['middle']={}
    date['last']={}
# storage={}
# init(storage)

def lookup(date,label,name):
    return date[label].get(name)

def store(date,*full_names):
    for full_name in full_names:
        names=full_name.split()
        if len(names)==2:
            names.insert(1,'')
        labels='first','middle','last'
        for label,name in zip(labels,names):
            people=lookup(date,label,name)
            if people:
                people.append(full_name)
            else:
                date[label][name]=[full_name]

MyNames={}
init(MyNames)
store(MyNames,'Magus Lie Hetland')
store(MyNames,'Robin Hood')
store(MyNames,'Robin Lcksley Parl')
store(MyNames,'Gao Ya Jie')
store(MyNames,'Fang Zheng')
store(MyNames,'Gao Ya Jie')
print MyNames
print lookup(MyNames,'last','Parl')
print lookup(MyNames,'middle','dd')
print lookup(MyNames,'first','Gao')

store(MyNames,'Guo xin','Zhang yu','Zhao Jian Ling')
print MyNames
