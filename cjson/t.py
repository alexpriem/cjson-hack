import cjson, datetime

class b(object):
    pass
a=cjson.encode({1:2})
#print a
a=cjson.encode({2:'3'})
#print a
a=cjson.encode({'3':'4'})
#print a

a=cjson.encode({'3':[1,2]})
#print a
print 'started'
n=datetime.datetime.now()
o=datetime.date(2012,1,7)
p=datetime.time(1,5,7)
#print n.isoformat()
bb=b()
print type(bb)
print bb.__class__
#print bb.__name__
txt=cjson.encode({1:n, 2:'aa', 3:3, 4:o, 5:p, 6:bb})
txt2=cjson.sloppyencode({1:n, 2:'aa', 3:3, 4:o, 5:p, 6:bb})
print 'got [%s]' % txt
print 'and [%s]' % txt2
print cjson.decode (txt)


