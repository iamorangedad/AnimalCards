import re, sys
i, pat = sys.argv[1], sys.argv[2]; n = int(sys.argv[3]) if len(sys.argv) > 3 else 6
t = re.sub(r"\s+", " ", open(f"src4/{i}.txt").read())
k = 0
for s in re.split(r"(?<=[.!?])\s+(?=[A-Z])", t):
    if re.search(pat, s, re.I):
        print(f"[{i}]", s[:260]); k += 1
        if k >= n: break
