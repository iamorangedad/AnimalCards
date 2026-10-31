import re, sys, os
RX = r"\d[\d,.–\-]* ?(kg|g\b|cm|mm|m\b|km|km/h|years|days|months|weeks|°C|%|young|eggs|metres|meters|individuals|hours|minutes|tonnes|tons|μm|µm|ft|in\b|lb|species|seeds|flowers|petals|chromosomes|hectares|ha\b)"
N = int(os.environ.get("N", 11)); L = int(os.environ.get("L", 210))
for i in sys.argv[1:]:
    t = re.sub(r"\s+", " ", open(f"src4/{i}.txt").read())
    t = re.split(r" == (References|See also|Notes|External links|Further reading) ==", t)[0]
    ss = re.split(r"(?<=[.!?])\s+(?=[A-Z])", t)
    w = open(f"src4/{i}.wiki").read() if os.path.exists(f"src4/{i}.wiki") else ""
    st = re.search(r"\|\s*status\s*=\s*([A-Za-z0-9.]+)", w); sy = re.search(r"status_system\s*=\s*([A-Za-z0-9.]+)", w)
    au = re.search(r"cite iucn[^}]*?(?:author1?|last1?)\s*=\s*([^|}]+)[^}]*?year\s*=\s*(\d{4})|cite iucn[^}]*?year\s*=\s*(\d{4})[^}]*?(?:author1?|last1?)\s*=\s*([^|}]+)", w, re.I)
    a = (au.group(1) or au.group(4) or "").strip() if au else ""; y = (au.group(2) or au.group(3)) if au else ""
    title = open(f"src4/{i}.title").read() if os.path.exists(f"src4/{i}.title") else "?"
    print(f"\n### {i} [{title}] | {st.group(1) if st else '-'} {sy.group(1) if sy else ''} | {a[:30]} {y} | {len(t)}")
    print(" >", " ".join(ss[:2])[:L + 60])
    seen = 0
    for s in ss[2:]:
        if re.search(RX, s) and not re.search(r"(doi|ISBN|Retrieved|archived)", s, re.I):
            print(" -", s[:L]); seen += 1
            if seen >= N: break
