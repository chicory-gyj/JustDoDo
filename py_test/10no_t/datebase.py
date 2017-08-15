#!/usr/bin/python
import shelve,sys
def store_person(db):
    pid=raw_input('Enter unique ID number:')
    person={}
    person['name']=raw_input('Enter name:')
    person['age']=raw_input('Enter age:')
    person['phone']=raw_input('Enter phone:')
    db[pid]=person

def lookup_person(db):
    pid=raw_input('Enter ID number:')
    field=raw_input('What would you want to know?(name,age,phone)')
    field=field.strip().lower()
    print field.capitalize()+':'+db[pid][field]

def print_help():
    print 'The available commands are:'
    print 'store :Store information about a person'
    print 'lookup:Looks up a person from ID number'
    print 'quit  :Save changes and exit'
    print '?     :Print this message'

def enter_command():
    cmd=raw_input('Enter a command(? for help)')
    cmd=cmd.strip().lower()
    return cmd
def main():
    datebase=shelve.open('/Users/gaoyajie/github/JustDoDo/py_test/6no_t/dateb2')
    try:
        while True:
            cmd=enter_command()
            if cmd=='store':
                store_person(datebase)
            elif cmd=='lookup':
                lookup_person(datebase)
            elif cmd=='?':
                print_help()
            elif cmd=='quit':
                return
    finally:
        datebase.close()
if __name__=='__main__':
    main()
