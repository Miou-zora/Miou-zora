#!/usr/bin/env python3
"""Generate light/dark SVG variants for each README theme.

Canvases are transparent; Evangelion and Automata paint an inset field, Replicant
paints nothing at all. Pairs are served through <picture>, which GitHub resolves
with its own theme setting.

Automata tokens come from the yorha-css framework source:
  --main-bg-color #d1cdb7 · --bg-grid-color #ccc8b1 · --text-primary #454138
  --text-secondary #dcd8c0 · --text-shadow #bab5a1
  h1: uppercase, normal weight, 0.5rem tracking, 0.3rem hard offset shadow
  left marker: border-width 0 0.2rem 0 0.6rem  (fat bar + thin bar)
  panels: border-width 0 0.2rem 0.2rem 0  (right + bottom edge only)
"""
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent / "assets"

NAME = "MIOUZORA"
REAL = "ALEXANDRE FRANQUET"
SUB = "GAME DEV · WEIRD TECHNOS · MACRO PHOTOGRAPHY"

PAL = {
    "evangelion": {
        "light": dict(FIELD="#E7E3D8", INK="#0A0A0A", RED="#D62300", PURPLE="#6B2BA8",
                      LIME="#5E8500", RULE="#0A0A0A"),
        "dark":  dict(FIELD="#0A0A0A", INK="#E7E3D8", RED="#FF3B00", PURPLE="#7B2FBE",
                      LIME="#B8FF3B", RULE="#E7E3D8"),
    },
    "nier-automata": {
        "light": dict(FIELD="#D1CDB7", GRID="#CCC8B1", INK="#454138", REV="#DCD8C0",
                      SHADOW="#BAB5A1", SWEEP="#FFFFFF", SWEEPO="0.16"),
        "dark":  dict(FIELD="#3E3B33", GRID="#454138", INK="#DCD8C0", REV="#3E3B33",
                      SHADOW="#5D594E", SWEEP="#DCD8C0", SWEEPO="0.07"),
    },
    "nier-replicant": {
        "light": dict(INK="#3B342C", GOLD="#9C7F45", HAIR="#8C7E68"),
        "dark":  dict(INK="#EDE7DA", GOLD="#C9A968", HAIR="#9C8F79"),
    },
}

EVA_BANNER = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 300" width="1200" height="300" role="img" aria-label="Miouzora, Alexandre Franquet. Special operations, game dev division. System active: C++, C, Python.">
  <style>
    .l {{ font-family: "Helvetica Neue", Helvetica, Arial, sans-serif; font-weight: 700; }}
    .j {{ font-family: "Hiragino Mincho ProN", "Yu Mincho", "MS Mincho", serif; font-weight: 700; }}
    .t {{ font-size: 11px; letter-spacing: 5px; }}
    .alert {{ animation: blink 1.9s steps(1, end) infinite; }}
    @keyframes blink {{ 0%, 58% {{ opacity: 1; }} 59%, 100% {{ opacity: 0.1; }} }}
    .drift {{ animation: drift 11s linear infinite; }}
    @keyframes drift {{ from {{ transform: translateX(0); }} to {{ transform: translateX(96px); }} }}
  </style>
  <defs>
    <clipPath id="panel"><rect x="10" y="10" width="1180" height="280"/></clipPath>
    <clipPath id="band"><rect x="10" y="10" width="1180" height="24"/></clipPath>
  </defs>

  <rect x="10" y="10" width="1180" height="280" fill="{FIELD}"/>

  <g clip-path="url(#band)">
    <g class="drift" fill="{RED}">
      <path d="M-110 34 L-62 10 h48 L-14 34 Z"/><path d="M-14 34 L34 10 h48 L82 34 Z"/>
      <path d="M82 34 L130 10 h48 L178 34 Z"/><path d="M178 34 L226 10 h48 L274 34 Z"/>
      <path d="M274 34 L322 10 h48 L370 34 Z"/><path d="M370 34 L418 10 h48 L466 34 Z"/>
      <path d="M466 34 L514 10 h48 L562 34 Z"/><path d="M562 34 L610 10 h48 L658 34 Z"/>
      <path d="M658 34 L706 10 h48 L754 34 Z"/><path d="M754 34 L802 10 h48 L850 34 Z"/>
      <path d="M850 34 L898 10 h48 L946 34 Z"/><path d="M946 34 L994 10 h48 L1042 34 Z"/>
      <path d="M1042 34 L1090 10 h48 L1138 34 Z"/><path d="M1138 34 L1186 10 h48 L1234 34 Z"/>
    </g>
  </g>

  <g clip-path="url(#panel)">
    <text class="j" x="1020" y="300" font-size="340" text-anchor="middle" fill="{PURPLE}" opacity="0.92">創</text>
    <rect x="884" y="150" width="272" height="6" fill="{RED}"/>
  </g>

  <g stroke="{RULE}" opacity="0.5">
    <line x1="66" y1="70" x2="700" y2="70"/>
    <line x1="66" y1="242" x2="700" y2="242"/>
  </g>

  <text class="l t" x="66" y="60" fill="{INK}">SPECIAL OPERATIONS · GAME DEV DIVISION</text>
  <text class="l" x="64" y="148" font-size="84" letter-spacing="6" fill="{RED}">{NAME}</text>
  <text class="l" x="66" y="180" font-size="17" letter-spacing="9" fill="{INK}">{REAL}</text>
  <text class="j" x="66" y="216" font-size="24" letter-spacing="8" fill="{INK}" opacity="0.9">創造せよ、何度でも</text>

  <g class="alert">
    <rect x="66" y="254" width="130" height="24" fill="{RED}"/>
    <text class="j" x="131" y="271" font-size="15" fill="{FIELD}" text-anchor="middle" letter-spacing="3">起動中</text>
  </g>
  <text class="l t" x="212" y="271" fill="{LIME}">SYSTEM ACTIVE · C++ / C / PYTHON</text>

  <g fill="{INK}" opacity="0.9">
    <rect x="1150" y="256" width="30" height="3"/><rect x="1177" y="232" width="3" height="27"/>
  </g>
</svg>
"""

EVA_DIVIDER = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 32" width="1200" height="32" role="img" aria-label="">
  <style>
    .l {{ font-family: "Helvetica Neue", Helvetica, Arial, sans-serif; font-weight: 700; font-size: 10px; letter-spacing: 5px; }}
    .p {{ animation: p 3.4s ease-in-out infinite; }}
    @keyframes p {{ 0%, 100% {{ opacity: 0.25; }} 50% {{ opacity: 1; }} }}
  </style>
  <rect x="10" y="4" width="1180" height="24" fill="{FIELD}"/>
  <rect x="10" y="15" width="1180" height="1" fill="{INK}" opacity="0.35"/>
  <rect x="10" y="10" width="120" height="12" fill="{RED}"/>
  <rect class="p" x="138" y="10" width="12" height="12" fill="{LIME}"/>
  <rect x="158" y="10" width="6" height="12" fill="{PURPLE}"/>
  <text class="l" x="1180" y="20" text-anchor="end" fill="{INK}" opacity="0.8">MIOUZORA · GITHUB</text>
</svg>
"""

AUT_BANNER = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 540" width="1200" height="540" role="img" aria-label="Miouzora, Alexandre Franquet. YoRHa personal data. Class: teacher at Epitech. Core: C++ and C. Now: building Wagoon. Off duty: Osu! and macro photography. Languages: C++, C, Python. Tools: Unity, Docker, xmake. Field: game engines, renderers, game protocols. 8709 commits since 30 September 2021.">
  <style>
    .f {{ font-family: helvetica, "Helvetica Neue", Arial, sans-serif; font-weight: 300; }}
    .t {{ font-size: 12px; letter-spacing: 3.4px; }}
    .s {{ font-size: 11px; letter-spacing: 3px; }}
    .lead {{ stroke: {INK}; stroke-width: 1; stroke-dasharray: 1.5 4.5; opacity: 0.45; }}
    .sweep {{ animation: sweep 11s linear infinite; }}
    @keyframes sweep {{ from {{ transform: translateY(-90px); }} to {{ transform: translateY(548px); }} }}
    .cur {{ animation: cur 1.1s steps(1, end) infinite; }}
    @keyframes cur {{ 0%, 50% {{ opacity: 1; }} 51%, 100% {{ opacity: 0; }} }}
  </style>
  <defs>
    <pattern id="grid" width="5" height="5" patternUnits="userSpaceOnUse">
      <rect width="5" height="5" fill="{FIELD}"/>
      <rect width="1" height="5" fill="{GRID}"/>
      <rect width="5" height="1" fill="{GRID}"/>
    </pattern>
    <clipPath id="p"><rect x="10" y="10" width="1180" height="514"/></clipPath>
  </defs>

  <rect x="10" y="10" width="1180" height="514" fill="url(#grid)"/>

  <!-- system bar -->
  <rect x="10" y="10" width="1180" height="34" fill="{INK}"/>
  <rect x="30" y="21" width="12" height="12" fill="{REV}"/>
  <text class="f s" x="52" y="31" fill="{REV}">YoRHa  ·  PERSONAL DATA</text>
  <text class="f s" x="1170" y="31" fill="{REV}" text-anchor="end">8709 COMMITS  ·  SINCE 2021.09.30</text>

  <!-- title, with the framework's hard offset shadow -->
  <text class="f" x="60" y="122" font-size="58" letter-spacing="19" fill="{SHADOW}">{NAME}</text>
  <text class="f" x="55" y="117" font-size="58" letter-spacing="19" fill="{INK}">{NAME}</text>
  <text class="f" x="57" y="146" font-size="14" letter-spacing="10" fill="{INK}" opacity="0.75">{REAL}</text>

  <!-- ── STATUS ── -->
  <line x1="57" y1="170" x2="1143" y2="170" stroke="{INK}" stroke-width="1.6"/>
  <text class="f s" x="70" y="190" fill="{INK}">S T A T U S</text>
  <line x1="57" y1="202" x2="1143" y2="202" stroke="{INK}" stroke-width="1.6"/>

  <g>
    <rect x="57" y="216" width="10" height="30" fill="{INK}"/><rect x="71" y="216" width="3" height="30" fill="{INK}"/>
    <rect x="82" y="216" width="466" height="30" fill="{REV}"/>
    <rect x="548" y="216" width="3" height="30" fill="{SHADOW}"/><rect x="82" y="246" width="469" height="3" fill="{SHADOW}"/>
    <text class="f t" x="98" y="236" fill="{INK}">CLASS</text>
    <line class="lead" x1="212" y1="232" x2="288" y2="232"/>
    <text class="f t" x="302" y="236" fill="{INK}">TEACHER / EPITECH</text>
  </g>
  <g>
    <rect x="640" y="216" width="10" height="30" fill="{INK}"/><rect x="654" y="216" width="3" height="30" fill="{INK}"/>
    <rect x="665" y="216" width="478" height="30" fill="{REV}"/>
    <rect x="1143" y="216" width="3" height="30" fill="{SHADOW}"/><rect x="665" y="246" width="481" height="3" fill="{SHADOW}"/>
    <text class="f t" x="681" y="236" fill="{INK}">NOW</text>
    <line class="lead" x1="795" y1="232" x2="871" y2="232"/>
    <text class="f t" x="885" y="236" fill="{INK}">BUILDING WAGOON</text>
  </g>
  <g>
    <rect x="57" y="258" width="10" height="30" fill="{INK}"/><rect x="71" y="258" width="3" height="30" fill="{INK}"/>
    <rect x="82" y="258" width="466" height="30" fill="{INK}"/>
    <text class="f t" x="98" y="278" fill="{REV}">CORE</text>
    <line x1="212" y1="274" x2="288" y2="274" stroke="{REV}" stroke-width="1" stroke-dasharray="1.5 4.5" opacity="0.55"/>
    <text class="f t" x="302" y="278" fill="{REV}">C++ / C<tspan class="cur" dx="16">▮</tspan></text>
  </g>
  <g>
    <rect x="640" y="258" width="10" height="30" fill="{INK}"/><rect x="654" y="258" width="3" height="30" fill="{INK}"/>
    <rect x="665" y="258" width="478" height="30" fill="{REV}"/>
    <rect x="1143" y="258" width="3" height="30" fill="{SHADOW}"/><rect x="665" y="288" width="481" height="3" fill="{SHADOW}"/>
    <text class="f t" x="681" y="278" fill="{INK}">OFF DUTY</text>
    <line class="lead" x1="795" y1="274" x2="871" y2="274"/>
    <text class="f t" x="885" y="278" fill="{INK}">OSU!  ·  MACRO PHOTOGRAPHY</text>
  </g>

  <!-- ── EQUIPMENT ── -->
  <line x1="57" y1="312" x2="1143" y2="312" stroke="{INK}" stroke-width="1.6"/>
  <text class="f s" x="70" y="332" fill="{INK}">E Q U I P M E N T</text>
  <line x1="57" y1="344" x2="1143" y2="344" stroke="{INK}" stroke-width="1.6"/>

  <g>
    <rect x="57" y="358" width="10" height="30" fill="{INK}"/><rect x="71" y="358" width="3" height="30" fill="{INK}"/>
    <rect x="82" y="358" width="466" height="30" fill="{REV}"/>
    <rect x="548" y="358" width="3" height="30" fill="{SHADOW}"/><rect x="82" y="388" width="469" height="3" fill="{SHADOW}"/>
    <text class="f t" x="98" y="378" fill="{INK}">LANGUAGES</text>
    <line class="lead" x1="212" y1="374" x2="288" y2="374"/>
    <text class="f t" x="302" y="378" fill="{INK}">C++  ·  C  ·  PYTHON</text>
  </g>
  <g>
    <rect x="640" y="358" width="10" height="30" fill="{INK}"/><rect x="654" y="358" width="3" height="30" fill="{INK}"/>
    <rect x="665" y="358" width="478" height="30" fill="{REV}"/>
    <rect x="1143" y="358" width="3" height="30" fill="{SHADOW}"/><rect x="665" y="388" width="481" height="3" fill="{SHADOW}"/>
    <text class="f t" x="681" y="378" fill="{INK}">TOOLS</text>
    <line class="lead" x1="795" y1="374" x2="871" y2="374"/>
    <text class="f t" x="885" y="378" fill="{INK}">UNITY  ·  DOCKER  ·  XMAKE</text>
  </g>
  <g>
    <rect x="57" y="400" width="10" height="30" fill="{INK}"/><rect x="71" y="400" width="3" height="30" fill="{INK}"/>
    <rect x="82" y="400" width="1061" height="30" fill="{REV}"/>
    <rect x="1143" y="400" width="3" height="30" fill="{SHADOW}"/><rect x="82" y="430" width="1064" height="3" fill="{SHADOW}"/>
    <text class="f t" x="98" y="420" fill="{INK}">FIELD</text>
    <line class="lead" x1="212" y1="416" x2="288" y2="416"/>
    <text class="f t" x="302" y="420" fill="{INK}">GAME ENGINES  ·  RENDERERS  ·  GAME PROTOCOLS</text>
  </g>

  <!-- footer -->
  <line x1="57" y1="466" x2="1143" y2="466" stroke="{SHADOW}" stroke-width="1.6"/>
  <rect x="57" y="480" width="8" height="8" fill="{INK}" opacity="0.8"/>
  <text class="f" x="74" y="488" font-size="10" letter-spacing="3" fill="{INK}" opacity="0.65">glory to mankind</text>
  <rect x="10" y="508" width="1180" height="4" fill="{SHADOW}"/>

  <g clip-path="url(#p)"><g class="sweep"><rect x="10" y="0" width="1180" height="70" fill="{SWEEP}" opacity="{SWEEPO}"/></g></g>
</svg>
"""

AUT_DIVIDER = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 30" width="1200" height="30" role="img" aria-label="">
  <defs>
    <pattern id="g2" width="5" height="5" patternUnits="userSpaceOnUse">
      <rect width="5" height="5" fill="{FIELD}"/>
      <rect width="1" height="5" fill="{GRID}"/>
      <rect width="5" height="1" fill="{GRID}"/>
    </pattern>
  </defs>
  <rect x="10" y="5" width="1180" height="20" fill="url(#g2)"/>
  <rect x="10" y="5" width="10" height="20" fill="{INK}"/>
  <rect x="24" y="5" width="3" height="20" fill="{INK}"/>
  <rect x="10" y="25" width="1180" height="3" fill="{SHADOW}"/>
  <line x1="38" y1="15" x2="1180" y2="15" stroke="{INK}" stroke-width="1" opacity="0.3"/>
</svg>
"""

AUT_POD = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 132" width="1200" height="132" role="img" aria-label="Pod 042 transmission. Proposal: contact the unit on Discord. Handle: miouzora.">
  <style>
    .f {{ font-family: helvetica, "Helvetica Neue", Arial, sans-serif; font-weight: 300; font-size: 12px; letter-spacing: 3.4px; }}
    .c {{ animation: c 1.1s steps(1, end) infinite; }}
    @keyframes c {{ 0%, 50% {{ opacity: 1; }} 51%, 100% {{ opacity: 0; }} }}
  </style>
  <defs>
    <pattern id="g3" width="5" height="5" patternUnits="userSpaceOnUse">
      <rect width="5" height="5" fill="{FIELD}"/>
      <rect width="1" height="5" fill="{GRID}"/>
      <rect width="5" height="1" fill="{GRID}"/>
    </pattern>
  </defs>
  <rect x="10" y="6" width="1180" height="116" fill="url(#g3)"/>
  <rect x="10" y="6" width="10" height="116" fill="{INK}"/>
  <rect x="24" y="6" width="3" height="116" fill="{INK}"/>
  <rect x="1187" y="6" width="3" height="116" fill="{SHADOW}"/>
  <rect x="10" y="122" width="1180" height="4" fill="{SHADOW}"/>
  <rect x="10" y="6" width="1180" height="28" fill="{INK}"/>
  <text class="f" x="44" y="25" fill="{REV}">POD 042 : TRANSMISSION</text>
  <text class="f" x="44" y="72" fill="{INK}">PROPOSAL: CONTACT THE UNIT ON DISCORD, ABOUT ANYTHING.</text>
  <text class="f" x="44" y="102" fill="{INK}">HANDLE: miouzora<tspan class="c" dx="10">▮</tspan></text>
</svg>
"""

# Replicant: nothing painted behind it — the page shows through.
REP_BANNER = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 270" width="1200" height="270" role="img" aria-label="Miouzora, Alexandre Franquet. Game dev, weird technos, macro photography. Rebuilt, because I wanted to know how it worked.">
  <style>
    .s {{ font-family: "Iowan Old Style", "Palatino Linotype", Palatino, Georgia, serif; }}
    .b {{ animation: b 7s ease-in-out infinite; }}
    @keyframes b {{ 0%, 100% {{ opacity: 0.4; }} 50% {{ opacity: 1; }} }}
  </style>

  <g stroke="{GOLD}" stroke-width="1.5" fill="none">
    <path d="M44 62 v-24 h24"/><path d="M1156 62 v-24 h-24"/>
    <path d="M44 208 v24 h24"/><path d="M1156 208 v24 h-24"/>
  </g>

  <g stroke="{HAIR}" stroke-width="1" opacity="0.85">
    <line x1="190" y1="92" x2="520" y2="92"/><line x1="680" y1="92" x2="1010" y2="92"/>
    <line x1="190" y1="198" x2="520" y2="198"/><line x1="680" y1="198" x2="1010" y2="198"/>
  </g>
  <g class="b" fill="{GOLD}"><path d="M600 82 L612 92 L600 102 L588 92 Z"/></g>
  <path d="M600 188 L612 198 L600 208 L588 198 Z" fill="{GOLD}" opacity="0.7"/>

  <text class="s" x="600" y="152" font-size="62" letter-spacing="20" text-anchor="middle" fill="{INK}">{NAME}</text>
  <text class="s" x="600" y="180" font-size="14" letter-spacing="10" text-anchor="middle" fill="{HAIR}">{REAL}</text>
  <text class="s" x="600" y="248" font-size="13" letter-spacing="5" text-anchor="middle" fill="{HAIR}" opacity="0.9">{SUB}</text>
</svg>
"""

REP_RULE = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 28" width="1200" height="28" role="img" aria-label="">
  <style>
    .b {{ animation: b 7s ease-in-out infinite; }}
    @keyframes b {{ 0%, 100% {{ opacity: 0.35; }} 50% {{ opacity: 0.95; }} }}
  </style>
  <line x1="150" y1="14" x2="560" y2="14" stroke="{HAIR}" stroke-width="1" opacity="0.8"/>
  <line x1="640" y1="14" x2="1050" y2="14" stroke="{HAIR}" stroke-width="1" opacity="0.8"/>
  <path class="b" d="M600 6 L609 14 L600 22 L591 14 Z" fill="{GOLD}"/>
</svg>
"""


AUT_EQUIP = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 196" width="1200" height="196" role="img" aria-label="Equipment. Languages: C++, C, Python. Tools: Unity, Docker, xmake. Field: game engines, renderers, game protocols.">
  <style>
    .f {{ font-family: helvetica, "Helvetica Neue", Arial, sans-serif; font-weight: 300; }}
    .t {{ font-size: 12px; letter-spacing: 3.4px; }}
  </style>
  <defs>
    <pattern id="g4" width="5" height="5" patternUnits="userSpaceOnUse">
      <rect width="5" height="5" fill="{FIELD}"/>
      <rect width="1" height="5" fill="{GRID}"/>
      <rect width="5" height="1" fill="{GRID}"/>
    </pattern>
  </defs>
  <rect x="10" y="6" width="1180" height="180" fill="url(#g4)"/>
  <rect x="10" y="6" width="1180" height="30" fill="{INK}"/>
  <rect x="30" y="15" width="12" height="12" fill="{REV}"/>
  <text class="f t" x="52" y="26" fill="{REV}">E Q U I P M E N T</text>

  <g>
    <rect x="40" y="54" width="10" height="30" fill="{INK}"/><rect x="54" y="54" width="3" height="30" fill="{INK}"/>
    <rect x="65" y="54" width="1095" height="30" fill="{REV}"/>
    <rect x="1160" y="54" width="3" height="30" fill="{SHADOW}"/><rect x="65" y="84" width="1098" height="3" fill="{SHADOW}"/>
    <text class="f t" x="82" y="74" fill="{INK}">LANGUAGES<tspan dx="14" opacity="0.45">. . . . . .</tspan><tspan dx="14">C++  ·  C  ·  PYTHON</tspan></text>
  </g>
  <g>
    <rect x="40" y="96" width="10" height="30" fill="{INK}"/><rect x="110" y="96" width="3" height="30" fill="{INK}"/>
    <rect x="65" y="96" width="1095" height="30" fill="{REV}"/>
    <rect x="1160" y="96" width="3" height="30" fill="{SHADOW}"/><rect x="65" y="126" width="1098" height="3" fill="{SHADOW}"/>
    <text class="f t" x="82" y="116" fill="{INK}">TOOLS<tspan dx="14" opacity="0.45">. . . . . . . . . .</tspan><tspan dx="14">UNITY  ·  DOCKER  ·  XMAKE</tspan></text>
  </g>
  <g>
    <rect x="40" y="138" width="10" height="30" fill="{INK}"/><rect x="54" y="138" width="3" height="30" fill="{INK}"/>
    <rect x="65" y="138" width="1095" height="30" fill="{REV}"/>
    <rect x="1160" y="138" width="3" height="30" fill="{SHADOW}"/><rect x="65" y="168" width="1098" height="3" fill="{SHADOW}"/>
    <text class="f t" x="82" y="158" fill="{INK}">FIELD<tspan dx="14" opacity="0.45">. . . . . . . . . .</tspan><tspan dx="14">GAME ENGINES  ·  RENDERERS  ·  GAME PROTOCOLS</tspan></text>
  </g>
</svg>
"""

FILES = {
    "evangelion":     [("banner", EVA_BANNER), ("divider", EVA_DIVIDER)],
    "nier-automata":  [("banner", AUT_BANNER), ("divider", AUT_DIVIDER), ("pod", AUT_POD)],
    "nier-replicant": [("banner", REP_BANNER), ("rule", REP_RULE)],
}

for theme, items in FILES.items():
    for variant in ("light", "dark"):
        tokens = dict(PAL[theme][variant], NAME=NAME, REAL=REAL, SUB=SUB)
        for stem, tpl in items:
            out = ROOT / theme / f"{stem}-{variant}.svg"
            out.write_text(tpl.format(**tokens))
            print("wrote", out.relative_to(ROOT.parent))
