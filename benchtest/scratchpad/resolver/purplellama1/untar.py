import tarfile,sys
src,dst=sys.argv[1],sys.argv[2]
with tarfile.open(src) as t:
    names=t.getnames()
    for n in names:
        assert not n.startswith('/') and '..' not in n.split('/'),n
    t.extractall(dst,filter='data')
    print(len(names),'members')
