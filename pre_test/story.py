#!/usr/bin/python

def story(**kwd):
    return 'Once upon a time,there was a %(job)s called %(name)s' % kwd
print story(job='king',name='Chicory')
print story(name='Mr Robet',job='engneer')
para={'job':'teacher','name':'Mr green'}
print story(**para)

del para['job']
print story(job='doctor',**para)
