import re,sys,os
n=int(os.environ.get("N","12")); w=int(os.environ.get("W","230"))
kw=re.compile(r"\b(eat|eats|feed|feeds|diet|prey|venom|sting|toxic|poison|bite|harm|allerg|edible|danger)\w*",re.I)
for i in sys.argv[1:]:
    t=re.sub(r"\s+"," ",open(f"src5/{i}.txt").read()); t=re.sub(r"==+[^=]+==+"," ",t)
    ss=re.split(r"(?<=[.!?]) (?=[A-Z])",t)
    print(f"\n### {i} [{open(f'src5/{i}.title').read()}] {len(t)}"); print(" >",ss[0][:w])
    num=[s for s in ss[1:] if re.search(r"\d",s) and not re.search(r"\b(1[5-9]|20)\d\d\b(?! ?(m|km|mm|cm|kg|g|eggs|species))",s)][:n]
    for s in num: print(" -",s[:w])
    for s in [s for s in ss[1:] if kw.search(s) and s not in num][:5]: print(" D",s[:w])
    wk=open(f"src5/{i}.wiki").read(); m=re.search(r"status\s*=\s*(\w+)",wk); r=re.search(r"status_ref\s*=.{0,400}",wk)
    a=re.findall(r"\|\s*(?:last|author)\d?\s*=\s*([^|}]+)",r.group(0) if r else ""); y=re.findall(r"\|\s*(?:date|year)\s*=\s*([^|}]+)",r.group(0) if r else "")
    print(" IUCN",m.group(1) if m else "-",a[:2],y[:1])
