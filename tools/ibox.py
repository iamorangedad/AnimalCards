import re, sys
for i in sys.argv[1:]:
    w = open(f"src4/{i}.wiki").read()
    m = re.search(r"\{\{\s*Infobox[^\n]*\n(.*?)\n\}\}", w, re.S)
    body = m.group(1) if m else ""
    out = []
    for ln in body.split("\n"):
        mm = re.match(r"\s*\|\s*([a-z_ ]*(height|weight|life|status|coat|colou?r|country|origin|maleweight|femaleweight|maleheight|femaleheight|use|altname)[a-z_ ]*)\s*=\s*(.+)", ln, re.I)
        if mm and mm.group(3).strip(): out.append(f"{mm.group(1).strip()}={re.sub(r'<ref.*?(</ref>|/>)', '', mm.group(3))[:110]}")
    print(f"[{i}]", " | ".join(out)[:700])
