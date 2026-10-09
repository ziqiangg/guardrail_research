import json,sys
for f in sys.argv[1:]:
    d=json.load(open(f,encoding='utf-8'))
    c=d.get('cardData',{})
    print('==',d['id'],'sha',d['sha'],'gated',d['gated'],'lastMod',d['lastModified'])
    print(' license',c.get('license'),'| license_name',c.get('license_name'),'| license_link',c.get('license_link'))
    print(' tags license:',[t for t in d['tags'] if t.startswith('license')])
    p=c.get('extra_gated_prompt','')
    print(' gated_prompt head:',p[:90].replace('\n',' / '))
    print(' gated_fields',json.dumps(c.get('extra_gated_fields'))[:700])
    print(' gated_button',c.get('extra_gated_button_content'),'| heading',c.get('extra_gated_heading'),'| description',str(c.get('extra_gated_description'))[:200])
    print(' inference',d.get('inference'),'| safetensors total',d.get('safetensors',{}).get('total'),'| usedStorage',d.get('usedStorage'))
    print(' siblings',[s['rfilename'] for s in d.get('siblings',[])][:30])
    print(' cardData keys',list(c.keys()))
