"""SVG and HTML helpers for the Purple Llama explainer (scratch tool, not committed)."""


def marker(mid, cls):
    return ('<marker id="%s" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" '
            'orient="auto"><path d="M0,0 L10,5 L0,10 z" class="%s"/></marker>' % (mid, cls))


def fork(n, aria, in_tb, in_ts, gate_cls, gate_tb, gate_ts1, gate_ts2, lab_ok, lab_no,
         ok_tb, ok_ts, no_tb, no_ts, no_cls="no dev", ok_cls="ok"):
    """Reference fork, coordinates copied from Sentinel diagram 5 (README section 6)."""
    return f'''<svg viewBox="0 0 760 250" role="img" aria-label="{aria}">
          <defs>
            {marker("a%d" % n, "ah")}
            {marker("a%do" % n, "ahok")}
            {marker("a%dn" % n, "ahno")}
          </defs>
          <rect class="box" x="10" y="90" width="160" height="70" rx="8"/>
          <text class="tb" x="90" y="120" text-anchor="middle">{in_tb}</text>
          <text class="ts" x="90" y="140" text-anchor="middle">{in_ts}</text>
          <line class="ln" x1="170" y1="125" x2="226" y2="125" marker-end="url(#a{n})"/>
          <rect class="{gate_cls}" x="230" y="75" width="200" height="100" rx="8"/>
          <text class="tb" x="330" y="112" text-anchor="middle">{gate_tb}</text>
          <text class="ts" x="330" y="132" text-anchor="middle">{gate_ts1}</text>
          <text class="ts" x="330" y="150" text-anchor="middle">{gate_ts2}</text>
          <path class="lok" d="M430,105 C470,105 470,55 506,55" marker-end="url(#a{n}o)"/>
          <path class="lno" d="M430,145 C470,145 470,195 506,195" marker-end="url(#a{n}n)"/>
          <text class="tok" x="455" y="72" text-anchor="middle">{lab_ok}</text>
          <text class="tno" x="460" y="185" text-anchor="end">{lab_no}</text>
          <rect class="{ok_cls}" x="510" y="25" width="240" height="60" rx="8"/>
          <text class="tb" x="630" y="52" text-anchor="middle">{ok_tb}</text>
          <text class="ts" x="630" y="71" text-anchor="middle">{ok_ts}</text>
          <rect class="{no_cls}" x="510" y="165" width="240" height="60" rx="8"/>
          <text class="tb" x="630" y="192" text-anchor="middle">{no_tb}</text>
          <text class="ts" x="630" y="211" text-anchor="middle">{no_ts}</text>
        </svg>'''


def linear(n, aria, in_tb, in_ts, gate_cls, gate_tb, gate_ts1, gate_ts2, out_tb, out_ts, out_cls="box"):
    """Linear layout (README section 6): input 10,65 160x70; gate 230,50 200x100; output 510,65 240x70."""
    return f'''<svg viewBox="0 0 760 200" role="img" aria-label="{aria}">
          <defs>
            {marker("a%d" % n, "ah")}
          </defs>
          <rect class="box" x="10" y="65" width="160" height="70" rx="8"/>
          <text class="tb" x="90" y="95" text-anchor="middle">{in_tb}</text>
          <text class="ts" x="90" y="115" text-anchor="middle">{in_ts}</text>
          <line class="ln" x1="170" y1="100" x2="226" y2="100" marker-end="url(#a{n})"/>
          <rect class="{gate_cls}" x="230" y="50" width="200" height="100" rx="8"/>
          <text class="tb" x="330" y="87" text-anchor="middle">{gate_tb}</text>
          <text class="ts" x="330" y="107" text-anchor="middle">{gate_ts1}</text>
          <text class="ts" x="330" y="125" text-anchor="middle">{gate_ts2}</text>
          <line class="ln" x1="430" y1="100" x2="506" y2="100" marker-end="url(#a{n})"/>
          <rect class="{out_cls}" x="510" y="65" width="240" height="70" rx="8"/>
          <text class="tb" x="630" y="95" text-anchor="middle">{out_tb}</text>
          <text class="ts" x="630" y="115" text-anchor="middle">{out_ts}</text>
        </svg>'''


def rail(h3, tag, svg, caption, example=None, know=None):
    out = ['<article class="rail">',
           '      <div class="rail-head">',
           '        <h3>%s</h3>' % h3,
           '        <span class="tag">%s</span>' % tag,
           '      </div>']
    if svg is not None:
        out.append('      <figure>')
        out.append('        ' + svg)
        out.append('        <figcaption>%s</figcaption>' % caption)
        out.append('      </figure>')
    if example:
        out.append('      <dl class="example">')
        for dt, dd in example:
            out.append('        <dt>%s</dt><dd>%s</dd>' % (dt, dd))
        out.append('      </dl>')
    if know:
        out.append('      <p class="know"><b>Good to know:</b> %s</p>' % know)
    out.append('    </article>')
    return "\n    ".join(out) if False else "\n".join("    " + l if i else l for i, l in enumerate(out))


def pill(kind):
    txt = {"yes": "Yes", "partly": "Partly", "no": "No"}[kind]
    return '<span class="pill %s">%s</span>' % (kind, txt)
