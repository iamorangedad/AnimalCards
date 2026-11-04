# generates assets/logo.svg and assets/banner.svg (original artwork). PNG exports: headless Chrome screenshot of the SVGs.
INK="#1f2328"; GREY="#5d6268"; PAPER="#f7f6f1"; GREEN="#3f9a5b"; GREENL="#dcefe1"; BLUE="#2f7fc1"; BLUEL="#d9e9f6"; ORG="#e8692e"; YEL="#f6c343"
def grid(w,h,step=32,iso=True):
    s=[f'<rect width="{w}" height="{h}" fill="{PAPER}"/>','<g stroke="#1f2328" stroke-opacity=".07" stroke-width="1.5">']
    for x in range(0,w+1,step): s.append(f'<line x1="{x}" y1="0" x2="{x}" y2="{h}"/>')
    for y in range(0,h+1,step): s.append(f'<line x1="0" y1="{y}" x2="{w}" y2="{y}"/>')
    s.append('</g>')
    if iso:
        import math
        t=math.tan(math.radians(30)); s.append('<g stroke="#1f2328" stroke-opacity=".05" stroke-width="1.2">')
        for k in range(-h*2,w*2,step*2):
            s.append(f'<line x1="{k}" y1="0" x2="{k+h/t}" y2="{h}"/>'); s.append(f'<line x1="{k}" y1="0" x2="{k-h/t}" y2="{h}"/>')
        s.append('</g>')
    return '\n'.join(s)
def icon():
    # 400x400 design space
    return f'''
<g stroke-linejoin="round" stroke-linecap="round">
  <!-- back cards -->
  <g transform="rotate(-12 200 220)"><rect x="95" y="60" width="210" height="300" rx="16" fill="{GREENL}" stroke="{GREEN}" stroke-width="6"/></g>
  <g transform="rotate(8 200 220)"><rect x="95" y="60" width="210" height="300" rx="16" fill="{BLUEL}" stroke="{BLUE}" stroke-width="6"/></g>
  <!-- front card -->
  <rect x="95" y="55" width="210" height="300" rx="16" fill="#fff" stroke="{INK}" stroke-width="7"/>
  <rect x="113" y="73" width="52" height="20" rx="4" fill="{INK}"/>
  <text x="139" y="88.5" font-family="'Helvetica Neue',Arial,sans-serif" font-size="14" font-weight="700" fill="#fff" text-anchor="middle" letter-spacing="1">001</text>
  <circle cx="281" cy="83" r="10" fill="{YEL}" stroke="{INK}" stroke-width="4"/>
  <!-- art window with grid -->
  <clipPath id="win"><rect x="113" y="104" width="174" height="150" rx="8"/></clipPath>
  <g clip-path="url(#win)">
    <rect x="113" y="104" width="174" height="150" fill="#fff"/>
    <g stroke="{INK}" stroke-opacity=".09" stroke-width="1.3">{''.join(f'<line x1="{x}" y1="104" x2="{x}" y2="254"/>' for x in range(113,288,14))}{''.join(f'<line x1="113" y1="{y}" x2="287" y2="{y}"/>' for y in range(104,255,14))}</g>
    <!-- globe -->
    <circle cx="200" cy="182" r="54" fill="{BLUEL}" stroke="{INK}" stroke-width="5"/>
    <ellipse cx="200" cy="182" rx="22" ry="54" fill="none" stroke="{INK}" stroke-width="3.5"/>
    <path d="M146 182 H254 M153 155 H247 M153 209 H247" fill="none" stroke="{INK}" stroke-width="3.5"/>
    <path d="M176 140 q14 6 10 20 q-6 10 6 18 q10 8 0 18 q-10 4 -18 -6 q-8 -12 -14 -2" fill="{GREENL}" stroke="{GREEN}" stroke-width="3.5"/>
    <!-- leaf -->
    <path d="M232 238 C228 206 248 186 282 182 C284 214 266 236 232 238 Z" fill="{GREENL}" stroke="{GREEN}" stroke-width="4.5"/>
    <path d="M236 234 C250 218 262 204 276 190" fill="none" stroke="{GREEN}" stroke-width="3.5"/>
  </g>
  <rect x="113" y="104" width="174" height="150" rx="8" fill="none" stroke="#cfd2d6" stroke-width="3"/>
  <!-- paw on card -->
  <g fill="{ORG}" stroke="{INK}" stroke-width="3.5">
    <ellipse cx="142" cy="236" rx="15" ry="12"/>
    <circle cx="125" cy="216" r="6"/><circle cx="137" cy="208" r="6"/><circle cx="150" cy="208" r="6"/><circle cx="161" cy="217" r="6"/>
  </g>
  <!-- stat bars -->
  <g stroke="{INK}" stroke-width="4">
    <rect x="113" y="272" width="174" height="12" rx="6" fill="#fff"/><rect x="113" y="272" width="110" height="12" rx="6" fill="{GREEN}"/>
    <rect x="113" y="296" width="174" height="12" rx="6" fill="#fff"/><rect x="113" y="296" width="70" height="12" rx="6" fill="{BLUE}"/>
    <rect x="113" y="320" width="174" height="12" rx="6" fill="#fff"/><rect x="113" y="320" width="140" height="12" rx="6" fill="{ORG}"/>
  </g>
</g>'''
FONT="font-family=\"'Helvetica Neue','Inter','Segoe UI',Arial,sans-serif\""
def wordmark(x,y,size,anchor="start"):
    return f'<text x="{x}" y="{y}" {FONT} font-size="{size}" font-weight="800" fill="{INK}" text-anchor="{anchor}" letter-spacing="-1">Animal<tspan fill="{GREEN}">Cards</tspan></text>'
logo=f'''<svg xmlns="http://www.w3.org/2000/svg" width="512" height="512" viewBox="0 0 512 512">
<title>AnimalCards logo</title>
{grid(512,512)}
<g transform="translate(76 8) scale(0.9)">{icon()}</g>
{wordmark(256,440,64,"middle")}
<rect x="176" y="462" width="160" height="6" rx="3" fill="{ORG}"/><circle cx="350" cy="465" r="6" fill="{YEL}"/>
</svg>'''
banner=f'''<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="400" viewBox="0 0 1600 400">
<title>AnimalCards banner</title>
{grid(1600,400)}
<g transform="translate(40 -8) scale(1.0)">{icon()}</g>
{wordmark(470,200,120)}
<text x="474" y="262" {FONT} font-size="38" font-weight="500" fill="{GREY}">1500 illustrated species cards · animals · plants · fungi</text>
<rect x="474" y="292" width="220" height="8" rx="4" fill="{ORG}"/><circle cx="712" cy="296" r="8" fill="{YEL}"/><circle cx="738" cy="296" r="8" fill="{GREEN}"/><circle cx="764" cy="296" r="8" fill="{BLUE}"/>
</svg>'''
import os; D=os.path.dirname(os.path.abspath(__file__)); open(os.path.join(D,'logo.svg'),'w').write(logo); open(os.path.join(D,'banner.svg'),'w').write(banner)
