import os,sys,re
A,B=[(chr(92)*2+"?"+chr(92)+os.path.abspath(a)) for a in sys.argv[1:3]]
def files(base):
    out={}
    for r,d,f in os.walk(base):
        for x in f:
            p=os.path.join(r,x); out[os.path.relpath(p,base).replace(chr(92),'/')]=p
    return out
fa,fb=files(A),files(B)
def norm(p): return open(p,'rb').read().replace(b'\r\n',b'\n')
common=sorted(set(fa)&set(fb))
diff=[c for c in common if norm(fa[c])!=norm(fb[c])]
only_a=sorted(set(fa)-set(fb)); only_b=sorted(set(fb)-set(fa))
print('common',len(common),'differ',len(diff),'only A',len(only_a),'only B',len(only_b))
print('non-test .py differing:',[d for d in diff if d.endswith('.py') and '/tests/' not in d])
print('rules/ differing:',[d for d in diff if '/rules/' in d])
print('only B non-rules:',[x for x in only_b if '/rules/' not in x])
print('only B rules:',[x for x in only_b if '/rules/' in x])
print('only A non-.c:',[x for x in only_a if not x.endswith('.c')], 'only A .c count', len([x for x in only_a if x.endswith('.c')]))
print('tests differing',len([d for d in diff if '/tests/' in d]))
def norm2(p):
    t=norm(p).decode('utf-8','replace'); return re.sub(r'\n\s*\n','\n',t)
d2=[c for c in common if norm2(fa[c])!=norm2(fb[c])]
print('differ ignoring blank lines',len(d2))
