#!/usr/bin/python
strings=['we','are','a',' team!',' You','are','so','brave']
string=[]
for string in strings:
    if 'are' in string:
        index=strings.index(string)
        strings[index]='[were]'
        print strings
    print strings
