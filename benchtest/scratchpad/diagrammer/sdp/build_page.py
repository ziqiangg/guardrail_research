#!/usr/bin/env python
"""Builds benchtest/diagrams/sdp-explained.html (gr-diagrammer, sdp P10).

Base CSS (sentinel-explained.html lines 6-109) is copied byte for byte; everything else is generated here
so fork and linear diagrams share the README coordinates exactly.
"""
import io
import os
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
SENTINEL = os.path.join(ROOT, "benchtest", "diagrams", "sentinel-explained.html")
OUT = os.path.join(ROOT, "benchtest", "diagrams", "sdp-explained.html")

with io.open(SENTINEL, encoding="utf-8", newline="") as f:
    lines = f.read().split("\n")
base_css = "\n".join(lines[5:109])  # lines 6..109, 1-based
fonts_line = lines[2]
preconnect = lines[1]


def marker(mid, cls):
    return ('<marker id="%s" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" '
            'orient="auto"><path d="M0,0 L10,5 L0,10 z" class="%s"/></marker>' % (mid, cls))


def fork(n, aria, in_t, in_s, gcls, g_t, g_1, g_2, lo, hi, ok_t, ok_s, no_t, no_s):
    return """<svg viewBox="0 0 760 250" role="img" aria-label="%(aria)s">
            <defs>
              %(m1)s
              %(m2)s
              %(m3)s
            </defs>
            <rect class="box" x="10" y="90" width="160" height="70" rx="8"/>
            <text class="tb" x="90" y="120" text-anchor="middle">%(in_t)s</text>
            <text class="ts" x="90" y="140" text-anchor="middle">%(in_s)s</text>
            <line class="ln" x1="170" y1="125" x2="226" y2="125" marker-end="url(#a%(n)s)"/>
            <rect class="%(gcls)s" x="230" y="75" width="200" height="100" rx="8"/>
            <text class="tb" x="330" y="112" text-anchor="middle">%(g_t)s</text>
            <text class="ts" x="330" y="132" text-anchor="middle">%(g_1)s</text>
            <text class="ts" x="330" y="150" text-anchor="middle">%(g_2)s</text>
            <path class="lok" d="M430,105 C470,105 470,55 506,55" marker-end="url(#a%(n)so)"/>
            <path class="lno" d="M430,145 C470,145 470,195 506,195" marker-end="url(#a%(n)sn)"/>
            <text class="tok" x="455" y="72" text-anchor="middle">%(lo)s</text>
            <text class="tno" x="460" y="185" text-anchor="end">%(hi)s</text>
            <rect class="ok" x="510" y="25" width="240" height="60" rx="8"/>
            <text class="tb" x="630" y="52" text-anchor="middle">%(ok_t)s</text>
            <text class="ts" x="630" y="71" text-anchor="middle">%(ok_s)s</text>
            <rect class="no dev" x="510" y="165" width="240" height="60" rx="8"/>
            <text class="tb" x="630" y="192" text-anchor="middle">%(no_t)s</text>
            <text class="ts" x="630" y="211" text-anchor="middle">%(no_s)s</text>
          </svg>""" % dict(
        n=n, aria=aria, in_t=in_t, in_s=in_s, gcls=gcls, g_t=g_t, g_1=g_1, g_2=g_2, lo=lo, hi=hi,
        ok_t=ok_t, ok_s=ok_s, no_t=no_t, no_s=no_s,
        m1=marker("a%s" % n, "ah"), m2=marker("a%so" % n, "ahok"), m3=marker("a%sn" % n, "ahno"))


def linear(n, aria, in_t, in_s, gcls, g_t, g_1, g_2, out_cls, out_t, out_s, edit_label=None):
    edge_cls, head_cls, mk = ("led", "ahed", "a%se" % n) if edit_label else ("ln", "ah", "a%s" % n)
    defs = marker("a%s" % n, "ah")
    if edit_label:
        defs += "\n              " + marker(mk, head_cls)
    label = ('\n            <text class="ted" x="468" y="90" text-anchor="middle">%s</text>' % edit_label) if edit_label else ""
    return """<svg viewBox="0 0 760 200" role="img" aria-label="%(aria)s">
            <defs>
              %(defs)s
            </defs>
            <rect class="box" x="10" y="65" width="160" height="70" rx="8"/>
            <text class="tb" x="90" y="95" text-anchor="middle">%(in_t)s</text>
            <text class="ts" x="90" y="115" text-anchor="middle">%(in_s)s</text>
            <line class="ln" x1="170" y1="100" x2="226" y2="100" marker-end="url(#a%(n)s)"/>
            <rect class="%(gcls)s" x="230" y="50" width="200" height="100" rx="8"/>
            <text class="tb" x="330" y="87" text-anchor="middle">%(g_t)s</text>
            <text class="ts" x="330" y="107" text-anchor="middle">%(g_1)s</text>
            <text class="ts" x="330" y="125" text-anchor="middle">%(g_2)s</text>
            <line class="%(edge)s" x1="430" y1="100" x2="506" y2="100" marker-end="url(#%(mk)s)"/>%(label)s
            <rect class="%(out_cls)s" x="510" y="65" width="240" height="70" rx="8"/>
            <text class="tb" x="630" y="95" text-anchor="middle">%(out_t)s</text>
            <text class="ts" x="630" y="115" text-anchor="middle">%(out_s)s</text>
          </svg>""" % dict(
        n=n, aria=aria, in_t=in_t, in_s=in_s, gcls=gcls, g_t=g_t, g_1=g_1, g_2=g_2, out_cls=out_cls,
        out_t=out_t, out_s=out_s, defs=defs, edge=edge_cls, mk=mk, label=label)


def rail(num, title, tag, svg, caption, dl, know, indent="    "):
    dl_html = ""
    if dl:
        dl_html = "\n      <dl class=\"example\">\n" + "\n".join("        <dt>%s</dt><dd>%s</dd>" % (k, v) for k, v in dl) + "\n      </dl>"
    return """    <article class="rail">
      <div class="rail-head">
        <h3>%s%s</h3>
        <span class="tag">%s</span>
      </div>
      <figure>
        %s
        <figcaption>%s</figcaption>
      </figure>%s
      <p class="know"><b>Good to know:</b> %s</p>
    </article>""" % ("%s. " % num if num else "", title, tag, svg, caption, dl_html, know)


YES = '<span class="pill yes">Yes</span>'
PARTLY = '<span class="pill partly">Partly</span>'
NO = '<span class="pill no">No</span>'

# ----------------------------------------------------------------------------------------------
# Overview map
# ----------------------------------------------------------------------------------------------
overview = """<section class="overview">
  <figure>
    <svg viewBox="0 0 900 400" role="img" aria-label="A user's message goes through Sensitive Data Protection's input checks for personal data, secrets and your own detectors before it reaches the AI model, and pictures the user sends go through picture checks. The AI model's answer goes through output checks before the user sees it, and pictures the AI makes go through picture checks. In both cases SDP returns findings or a cleaned copy, and your app decides whether to refuse, discard or mask. Documents fetched for the AI model can be checked for personal data and keys but not for hidden instructions, and actions the AI takes have no SDP check.">
      <defs>
        %(o)s
      </defs>
      <rect class="box" x="10" y="170" width="100" height="60" rx="8"/>
      <text class="tb" x="60" y="197" text-anchor="middle">User</text>
      <text class="ts" x="60" y="216" text-anchor="middle">asks a question</text>

      <rect class="gate" x="150" y="155" width="170" height="90" rx="8"/>
      <text class="tb" x="235" y="188" text-anchor="middle">Input checks</text>
      <text class="ts" x="235" y="208" text-anchor="middle">personal data · secrets</text>
      <text class="ts" x="235" y="225" text-anchor="middle">· your own detectors</text>

      <rect class="box" x="370" y="160" width="130" height="80" rx="8"/>
      <text class="tb" x="435" y="192" text-anchor="middle">AI model</text>
      <text class="ts" x="435" y="212" text-anchor="middle">writes the answer</text>

      <rect class="gate" x="550" y="155" width="170" height="90" rx="8"/>
      <text class="tb" x="635" y="188" text-anchor="middle">Output checks</text>
      <text class="ts" x="635" y="208" text-anchor="middle">personal data · secrets</text>
      <text class="ts" x="635" y="225" text-anchor="middle">· your own detectors</text>

      <rect class="box" x="770" y="170" width="100" height="60" rx="8"/>
      <text class="tb" x="820" y="205" text-anchor="middle">User</text>

      <line class="ln" x1="110" y1="200" x2="146" y2="200" marker-end="url(#o-a)"/>
      <line class="ln" x1="320" y1="200" x2="366" y2="200" marker-end="url(#o-a)"/>
      <line class="ln" x1="500" y1="200" x2="546" y2="200" marker-end="url(#o-a)"/>
      <line class="ln" x1="720" y1="200" x2="766" y2="200" marker-end="url(#o-a)"/>
      <text class="ts" x="343" y="147" text-anchor="middle">if allowed</text>
      <text class="ts" x="523" y="147" text-anchor="middle">draft</text>
      <text class="ts" x="743" y="147" text-anchor="middle">if allowed</text>

      <!-- pictures the user sends -->
      <rect class="gate" x="150" y="30" width="170" height="80" rx="8"/>
      <text class="tb" x="235" y="62" text-anchor="middle">Picture checks</text>
      <text class="ts" x="235" y="82" text-anchor="middle">text · IDs · safety</text>
      <path class="ln" d="M235,110 V151" marker-end="url(#o-a)"/>

      <!-- documents: personal data and keys -->
      <rect class="part" x="350" y="30" width="170" height="80" rx="8"/>
      <text class="tb" x="435" y="62" text-anchor="middle">Your documents</text>
      <text class="ts" x="435" y="82" text-anchor="middle">personal data and keys</text>
      <path class="ln" d="M435,110 V156" marker-end="url(#o-a)"/>

      <!-- pictures the AI makes -->
      <rect class="gate" x="550" y="30" width="170" height="80" rx="8"/>
      <text class="tb" x="635" y="62" text-anchor="middle">Picture checks</text>
      <text class="ts" x="635" y="82" text-anchor="middle">AI-made images too</text>
      <path class="ln" d="M635,110 V151" marker-end="url(#o-a)"/>

      <!-- bottom row -->
      <path class="ln" d="M235,245 V306" marker-end="url(#o-a)"/>
      <text class="ts" x="245" y="280">findings</text>
      <rect class="gate dev" x="150" y="310" width="170" height="70" rx="8"/>
      <text class="tb" x="235" y="340" text-anchor="middle">Your app</text>
      <text class="ts" x="235" y="360" text-anchor="middle">refuses or masks</text>

      <path class="lna" d="M435,240 V306" marker-end="url(#o-a)"/>
      <text class="ts" x="445" y="280">wants to act</text>
      <rect class="na" x="360" y="310" width="150" height="70" rx="8"/>
      <text class="tb" x="435" y="340" text-anchor="middle">Actions, tools</text>
      <text class="ts" x="435" y="360" text-anchor="middle">no SDP check</text>

      <path class="ln" d="M635,245 V306" marker-end="url(#o-a)"/>
      <text class="ts" x="645" y="280">findings</text>
      <rect class="gate dev" x="550" y="310" width="170" height="70" rx="8"/>
      <text class="tb" x="635" y="340" text-anchor="middle">Your app</text>
      <text class="ts" x="635" y="360" text-anchor="middle">discards or masks</text>
    </svg>
    <figcaption>SDP can check text and pictures going to the AI model and coming back, and can check passages from your documents for personal data and keys, but not for hidden instructions. It has no check for actions the AI takes. At every point it returns findings or a cleaned copy; your app decides whether to continue, refuse, discard or use the masked version.</figcaption>
  </figure>
</section>""" % dict(o=marker("o-a", "ah"))

# ----------------------------------------------------------------------------------------------
# Positioning
# ----------------------------------------------------------------------------------------------
positioning = """<section class="stage">
  <div class="stage-head">
    <div class="eyebrow">SDP, NeMo, Llama Guard and Sentinel</div>
    <h2>A finder and a cleaner, not a judge</h2>
    <p>The four tools sit at different levels. NeMo is a framework you run that decides where checks go. Llama Guard is one model you run that gives a verdict. Sentinel is a web service run by GovTech that gives a score for each check. Sensitive Data Protection (SDP) is a Google Cloud service that finds specific kinds of data in text and pictures, and can change them.</p>
  </div>

  <article class="rail">
    <div class="rail-head">
      <h3>1. Four different kinds of tool</h3>
      <span class="tag">What each one is, and what it hands back to your app</span>
    </div>
    <figure>
      <svg viewBox="0 0 760 300" role="img" aria-label="Four columns. NeMo Guardrails is a framework you run: it places the checks, runs your rules and calls safety models, and it gives allow or block. Llama Guard is one model you run, and it gives a safe or unsafe verdict. GovTech Sentinel is a hosted menu of checks that gives a score from 0 to 1 for each check. Google Sensitive Data Protection is a hosted service that finds sensitive data, masks or tokenises it and reads pictures, and it gives back findings or a cleaned copy.">
        <rect class="zone" x="10" y="20" width="170" height="260" rx="10"/>
        <text class="zl" x="26" y="44">NeMo Guardrails</text>
        <text class="ts" x="26" y="64">a framework you run</text>
        <rect class="box" x="22" y="80" width="146" height="44" rx="8"/>
        <text class="ts" x="95" y="107" text-anchor="middle">Places the checks</text>
        <rect class="box" x="22" y="134" width="146" height="44" rx="8"/>
        <text class="ts" x="95" y="161" text-anchor="middle">Runs your rules</text>
        <rect class="box" x="22" y="188" width="146" height="44" rx="8"/>
        <text class="ts" x="95" y="215" text-anchor="middle">Calls safety models</text>
        <text class="ts" x="95" y="262" text-anchor="middle">gives: allow or block</text>

        <rect class="gate" x="200" y="95" width="170" height="110" rx="8"/>
        <text class="tb" x="285" y="135" text-anchor="middle">Llama Guard</text>
        <text class="ts" x="285" y="157" text-anchor="middle">one model you run</text>
        <text class="ts" x="285" y="177" text-anchor="middle">reads text, judges it</text>
        <text class="ts" x="285" y="262" text-anchor="middle">gives: safe or unsafe</text>

        <rect class="zone" x="390" y="20" width="170" height="260" rx="10"/>
        <text class="zl" x="406" y="44">GovTech Sentinel</text>
        <text class="ts" x="406" y="64">a hosted menu of checks</text>
        <rect class="gate" x="402" y="80" width="146" height="44" rx="8"/>
        <text class="ts" x="475" y="107" text-anchor="middle">Harm and attack</text>
        <rect class="gate" x="402" y="134" width="146" height="44" rx="8"/>
        <text class="ts" x="475" y="161" text-anchor="middle">Off-topic, leakage</text>
        <rect class="gate" x="402" y="188" width="146" height="44" rx="8"/>
        <text class="ts" x="475" y="215" text-anchor="middle">Refusal, AWS checks</text>
        <text class="ts" x="475" y="262" text-anchor="middle">gives: a 0 to 1 score</text>

        <rect class="zone" x="580" y="20" width="170" height="260" rx="10"/>
        <text class="zl" x="596" y="44">Google SDP</text>
        <text class="ts" x="596" y="64">finds and cleans data</text>
        <rect class="gate" x="592" y="80" width="146" height="44" rx="8"/>
        <text class="ts" x="665" y="107" text-anchor="middle">Finds sensitive data</text>
        <rect class="gate" x="592" y="134" width="146" height="44" rx="8"/>
        <text class="ts" x="665" y="161" text-anchor="middle">Masks or tokenises</text>
        <rect class="gate" x="592" y="188" width="146" height="44" rx="8"/>
        <text class="ts" x="665" y="215" text-anchor="middle">Reads pictures too</text>
        <text class="ts" x="665" y="254" text-anchor="middle">gives: findings, or</text>
        <text class="ts" x="665" y="270" text-anchor="middle">a cleaned copy</text>
      </svg>
      <figcaption>Only NeMo acts on a result. Llama Guard, Sentinel and SDP all report, and your app (or a framework such as NeMo) does the refusing. SDP's main job is finding and editing specific values, such as an ID number, rather than judging whether a message is harmful. This page claims no link between SDP and NeMo, Llama Guard or Sentinel.</figcaption>
    </figure>
    <div class="tablewrap">
      <table class="cats">
        <thead><tr><th></th><th>NeMo Guardrails</th><th>Llama Guard</th><th>GovTech Sentinel</th><th>Google SDP</th></tr></thead>
        <tbody>
          <tr><td>What it is</td><td>A framework around your chatbot</td><td>One AI model</td><td>A web service with a menu of checks</td><td>A Google Cloud web service that finds and edits sensitive data</td></tr>
          <tr><td>Who runs it</td><td>You</td><td>You</td><td>GovTech (hosted); some models can be self-hosted</td><td>Google (hosted); you call it</td></tr>
          <tr><td>What it hands back</td><td>Allow or block</td><td>Safe or unsafe, plus a category</td><td>A score from 0 to 1 per check</td><td>Findings (kind of data, likelihood level, position) or a cleaned copy of the text</td></tr>
          <tr><td>Decides where checks run</td><td>Yes</td><td>No</td><td>No, your app chooses what text to send</td><td>No, your app chooses what to send</td></tr>
          <tr><td>Your own rules and fixed replies</td><td>Yes</td><td>No</td><td>No</td><td>Your own word lists and patterns for what to find; no fixed replies</td></tr>
          <tr><td>Edits text</td><td>Masks personal data</td><td>No</td><td>Returns a masked copy (personal data, via AWS)</td><td>Yes: deletes, masks, replaces or swaps for reversible tokens</td></tr>
          <tr><td>Singapore languages</td><td>Depends on the model it calls</td><td>Listed languages do not include Chinese, Malay or Tamil</td><td>LionGuard: Singlish, Chinese, Malay, partial Tamil</td><td>Not stated for Chinese, Malay, Tamil or Singlish; country-specific detectors support English and the country's languages</td></tr>
          <tr><td>Who can use it</td><td>Anyone (open source)</td><td>Anyone who accepts Meta's licence</td><td>Singapore Government public officers, closed beta</td><td>Anyone with a Google Cloud project that has billing and the service switched on</td></tr>
        </tbody>
      </table>
    </div>
    <p class="know"><b>Good to know:</b> SDP still carries its old name in places: the web address, the role name and the Python package all say DLP. Google's <a href="modelarmor-explained.html">Model Armor</a>, a separate product, can call SDP on prompts and answers; how it does so is covered on its own page, and this page is about SDP itself.</p>
  </article>
</section>"""

# ----------------------------------------------------------------------------------------------
# How it works
# ----------------------------------------------------------------------------------------------
how = """<section class="stage">
  <div class="stage-head">
    <div class="eyebrow">How it works</div>
    <h2>Send text or a picture, get back findings or a cleaned copy</h2>
    <p>Every function works the same way from the outside. Your app makes one web request to Google's API and reads what comes back. The next two diagrams show the request, and how SDP rates a match.</p>
  </div>

  <article class="rail">
    <div class="rail-head">
      <h3>2. One request, findings or a cleaned copy back</h3>
      <span class="tag">Sensitive Data Protection's API (still named the Cloud DLP API), with Google Cloud sign-in</span>
    </div>
    <figure>
      <svg viewBox="0 0 760 270" role="img" aria-label="The request carries the text or picture to check, the kinds of data to look for, and options such as a minimum likelihood, your own detectors and masking steps. SDP returns findings, each with the kind of data, a likelihood level and a position, or a cleaned copy of the text with a summary of changes. It never returns an allow or block verdict, and its results are not stored in Google Cloud.">
        <defs>
          %(a2)s
        </defs>
        <rect class="box" x="10" y="20" width="290" height="230" rx="8"/>
        <text class="tb" x="26" y="48">Your app sends</text>
        <text class="t" x="26" y="80">① the text or picture</text>
        <text class="ts" x="44" y="99">a message, answer, table, chat or file</text>
        <text class="t" x="26" y="130">② what to look for</text>
        <text class="ts" x="44" y="149">name each kind; do not leave it empty</text>
        <text class="t" x="26" y="180">③ options</text>
        <text class="ts" x="44" y="199">minimum likelihood, own detectors</text>
        <text class="ts" x="44" y="218">masking steps, if it should edit</text>

        <line class="ln" x1="300" y1="135" x2="346" y2="135" marker-end="url(#a2)"/>
        <rect class="gate" x="350" y="90" width="150" height="90" rx="8"/>
        <text class="tb" x="425" y="128" text-anchor="middle">SDP</text>
        <text class="ts" x="425" y="148" text-anchor="middle">finds or cleans</text>
        <line class="ln" x1="500" y1="135" x2="536" y2="135" marker-end="url(#a2)"/>

        <rect class="box" x="540" y="20" width="210" height="230" rx="8"/>
        <text class="tb" x="556" y="48">SDP returns</text>
        <text class="t" x="556" y="80">findings</text>
        <text class="ts" x="574" y="99">kind, likelihood, position</text>
        <text class="t" x="556" y="130">or a cleaned copy</text>
        <text class="ts" x="574" y="149">plus a summary of changes</text>
        <text class="ts" x="574" y="168">quote of match: off by default</text>
        <text class="ts" x="574" y="187">no allow or block verdict</text>
        <text class="ts" x="556" y="224">results are not stored</text>
      </svg>
      <figcaption>There is no 'this is input' or 'this is output' switch. Your app chooses which text to send, so the same request can be used before or after the AI model. One request is capped at 0.5 MB, and Google says to name the kinds of data to look for rather than leave the list empty.</figcaption>
    </figure>
    <figure>
      <svg viewBox="0 0 760 110" role="img" aria-label="A scale of five likelihood levels, from less sure to more sure that a match is real. Very unlikely and unlikely are left out of the results by default. Possible, likely and very likely are returned by default, and Possible is the default minimum.">
        <text class="ts" x="40" y="18" text-anchor="start">less sure it is a match</text>
        <text class="ts" x="720" y="18" text-anchor="end">more sure</text>
        <rect class="box" x="40" y="30" width="136" height="26" rx="4"/>
        <rect class="box" x="176" y="30" width="136" height="26"/>
        <rect class="gate" x="312" y="30" width="136" height="26"/>
        <rect class="gate" x="448" y="30" width="136" height="26"/>
        <rect class="gate" x="584" y="30" width="136" height="26" rx="4"/>
        <text class="ts" x="108" y="48" text-anchor="middle">Very unlikely</text>
        <text class="ts" x="244" y="48" text-anchor="middle">Unlikely</text>
        <text class="ts" x="380" y="48" text-anchor="middle">Possible</text>
        <text class="ts" x="516" y="48" text-anchor="middle">Likely</text>
        <text class="ts" x="652" y="48" text-anchor="middle">Very likely</text>
        <line class="ln" x1="44" y1="72" x2="308" y2="72"/>
        <line class="ln" x1="316" y1="72" x2="716" y2="72"/>
        <text class="ts" x="176" y="92" text-anchor="middle">left out by default</text>
        <text class="ts" x="516" y="92" text-anchor="middle">returned by default; the default minimum is Possible</text>
      </svg>
      <figcaption>SDP rates each finding in one of five buckets, not with a number. Google says a Very likely finding has 'many strong signals'. It gives no recommended minimum for screening chat text, so the cut-off is yours to choose and test.</figcaption>
    </figure>
  </article>

  <article class="rail">
    <div class="rail-head">
      <h3>What the built-in detectors cover</h3>
      <span class="tag">About 261 detectors by our count of Google's reference table; Google gives no total and says the list changes</span>
    </div>
    <div class="tablewrap">
      <table class="cats">
        <thead><tr><th>Group</th><th>What it covers</th><th>How many</th><th>One detector name</th></tr></thead>
        <tbody>
          <tr><td>Person details</td><td>Names, email, phone, user names, dates of birth</td><td>9</td><td class="code">PERSON_NAME</td></tr>
          <tr><td>Places and organisations</td><td>Street addresses, locations, organisation names</td><td>5</td><td class="code">STREET_ADDRESS</td></tr>
          <tr><td>Network and device IDs</td><td>IP and MAC addresses, device IDs, web addresses</td><td>12</td><td class="code">IP_ADDRESS</td></tr>
          <tr><td>Dates and times</td><td>Dates and times of day</td><td>2</td><td class="code">DATE</td></tr>
          <tr><td>Sensitive attributes</td><td>Age, gender, religion, politics, trade union, immigration status and similar terms</td><td>13</td><td class="code">RELIGIOUS_TERM</td></tr>
          <tr><td>Money</td><td>Card, bank, IBAN and SWIFT numbers</td><td>10</td><td class="code">CREDIT_CARD_NUMBER</td></tr>
          <tr><td>Health</td><td>Medical codes, record numbers and terms, blood type</td><td>8</td><td class="code">MEDICAL_RECORD_NUMBER</td></tr>
          <tr><td>Secrets</td><td>Cloud and AI-provider keys (Anthropic, OpenAI, Gemini), tokens, passwords</td><td>21</td><td class="code">ANTHROPIC_API_KEY</td></tr>
          <tr><td>Worldwide IDs</td><td>Passport (the list of countries includes Singapore), government ID, driver's licence, VAT, vehicle identification number (VIN)</td><td>6</td><td class="code">PASSPORT</td></tr>
          <tr><td>Singapore</td><td>NRIC number, passport number</td><td>2</td><td class="code">SINGAPORE_NATIONAL_REGISTRATION_ID_NUMBER</td></tr>
          <tr><td>Other countries</td><td>National IDs, tax and health numbers, listed by country in Google's reference</td><td>125</td><td class="code">US_SOCIAL_SECURITY_NUMBER</td></tr>
          <tr><td>Documents and source code</td><td>Document kinds (legal, finance, HR, medical), topic labels (offensive, politics, religion), 15 programming languages</td><td>37</td><td class="code">DOCUMENT_TYPE/CONTEXT/POLITICS</td></tr>
          <tr><td>Pictures</td><td>Objects in an image (person, passport, photo ID, face, signature, licence plate, barcode, whiteboard) and three whole-image safety labels</td><td>11</td><td class="code">OBJECT_TYPE/PERSON/PASSPORT</td></tr>
        </tbody>
      </table>
    </div>
    <p class="know"><b>Good to know:</b> the counts are ours, from the rows of Google's reference page. No Singapore FIN, UEN, +65 phone or address detector is named there. The document-category detectors are listed as limited-availability, and it is not stated whether they run on a plain text string.</p>
  </article>
</section>""" % dict(a2=marker("a2", "ah"))

# ----------------------------------------------------------------------------------------------
# Stage 1 Input
# ----------------------------------------------------------------------------------------------
r3 = rail(
    3, "Finding personal data and secrets",
    'Built-in detectors ("inspect") · input and output · ' + YES,
    fork(3,
         "The user's message is checked by SDP's built-in detectors, which return each kind of data found, a likelihood level and a position. If nothing is found, the message continues to the AI model. If something is found, your app decides whether to route or refuse, because SDP only reports.",
         "User's message", "any text, table or chat", "gate",
         "Sensitive-data check", "built-in detectors", "kind + likelihood + place",
         "clear", "found",
         "Continues to the AI model", "nothing changed",
         "Your app routes or refuses", "SDP only reports findings"),
    "SDP reports what it finds: the kind of data, a likelihood level (diagram 2) and where it sits in the text. It has built-in detectors for Singapore NRIC and passport numbers, and for AI-provider keys such as Anthropic, OpenAI and Gemini. Whether the message goes on is your app's call.",
    [("In", "My NRIC is S1234567D, email tan@example.com. (illustrative)"),
     ("Result", "Expected: two findings, a Singapore NRIC number and an email address, each with a likelihood level and a position (illustrative)")],
    "Google calls its detectors 'not a perfectly accurate detection method' and publishes no accuracy figure for any of them, including the Singapore NRIC one. Whether Singapore FIN numbers or +65 phone numbers are found is not stated. If you list no kinds of data, SDP picks a default list that Google says is for testing only.")

r4 = rail(
    4, "Masking before the AI model sees it",
    'Masking ("de-identify") · input and output · ' + YES,
    linear(4,
           "The user's message goes to SDP's de-identify step, which finds each sensitive value and then deletes, masks or replaces it. SDP returns a cleaned copy and a summary of changes, and your app decides whether to pass the cleaned copy to the AI model.",
           "User's message", "holds personal data", "gate",
           "De-identify", "finds each value,", "then changes it", "ed",
           "Cleaned copy returned", "plus a summary of changes", edit_label="replaces"),
    "SDP finds each value first, then changes it the way you chose: delete it, replace it with fixed text or with its type name, mask some characters, or hash it (a one-way scramble). Only the kinds of data you list are changed. Your app decides whether to pass the cleaned copy on.",
    [("Rule", "Mask email addresses with # (Google's docs)"),
     ("Masked", "My name is Alicia Abernathy, and my email address is <mark>##########@#######.###</mark>.")],
    "A value the detectors miss stays in the text, and Google publishes no figure for how much is missed. Bucketing and time extraction are offered, but Google's samples show them on tables only, so use on free text is to be verified; one sample does shift a date in a plain string. More than 3,000 findings in one request returns an error message.")

stage1 = """<section class="stage">
  <div class="stage-head">
    <div class="eyebrow">Stage 1 · Input</div>
    <h2>Finding and masking personal data in what the user typed</h2>
    <p>These checks look at the user's message before the AI model sees it. SDP either reports what it found or hands back a copy with the sensitive values replaced. Your app decides what happens next.</p>
  </div>

  <div class="grid2">
%s

%s
  </div>
</section>""" % (r3, r4)

# ----------------------------------------------------------------------------------------------
# Stage 2 Output
# ----------------------------------------------------------------------------------------------
r5 = rail(
    5, "Personal data in the AI's answer",
    'Same detectors, run on the answer · output · ' + YES,
    fork(5,
         "The AI's draft answer is checked by SDP's detectors, which return what they find. If nothing is found, the answer is shown to the user unchanged. If something is found, your app discards the draft or uses a cleaned copy from SDP.",
         "AI's draft answer", "may repeat personal data", "gate",
         "Sensitive-data check", "same detectors as input", "kind + likelihood + place",
         "clear", "found",
         "Answer shown to the user", "unchanged",
         "Your app discards the draft", "or uses a cleaned copy"),
    "There is no input or output setting, so the draft answer goes in the same kind of request as the user's message. NeMo's diagram 4 masks personal data on the answer in the same spirit; this page claims no link between NeMo and SDP.",
    [("Draft", "You can reach Jane Tan at jane.tan@example.com."),
     ("Result", "Two findings, a person name and an email address; your app discards or masks (illustrative)")],
    "Google's own examples describe prompts going to outside AI models; sending the answer through the same calls is our reading of the request format. <a href=\"modelarmor-explained.html\">Model Armor</a>, a separate Google product, can call SDP on prompts and answers, but its docs say its streaming methods and file-based prompts do not support SDP's masking.")

stage2 = """<section class="stage">
  <div class="stage-head">
    <div class="eyebrow">Stage 2 · Output</div>
    <h2>Checking the AI's answer</h2>
    <p>The same two calls can run on the AI's draft answer before the user sees it. SDP reports what it found or returns a cleaned copy; your app decides whether to show, discard or replace the answer. Diagrams 3 and 4 work the same way here.</p>
  </div>

%s
</section>""" % r5

# ----------------------------------------------------------------------------------------------
# Custom detectors and tokens
# ----------------------------------------------------------------------------------------------
r6 = rail(
    6, "Your own detectors and rules",
    'Custom detectors and rules ("custom infoTypes") · input and output · ' + YES,
    linear(6,
           "The text to check goes to SDP together with your own word lists, patterns and rules. SDP runs your detectors alongside the built-in ones and returns each match under the name you gave it, at a likelihood you set.",
           "Text to check", "+ your list or pattern", "gate",
           "Custom detectors", "your list or pattern,", "then your rules", "box",
           "Findings under your name", "at a likelihood you set"),
    "Custom detectors are your own word lists, patterns and rules, added to the built-in ones in the same request. A pattern is a regular expression, a compact code for a text shape such as ###-#-#####. A rule can drop a finding, or raise or lower its likelihood when a nearby word (a 'hotword') or another finding is present.",
    [("Rule", "Find ###-#-##### (medical record numbers); raise the likelihood if the word MRN is nearby"),
     ("In", "123-4-56789"), ("Result", "Possible (Google's docs)"),
     ("In", "MRN 123-4-56789"), ("Result", "Very likely (Google's docs)")],
    "The built-in list names no Singapore FIN, UEN or address detector, so a pattern you write could fill the gap, but nothing says Google tests such patterns. Its docs disagree on rule order: one page says rules run as written, another says exclusion rules run last. How word boundaries work on Chinese, Malay or Tamil text is not stated.")

def tokens_svg():
    return """<svg viewBox="0 0 760 270" role="img" aria-label="The user's message holds a real value such as an email address. SDP swaps it for a coded token using your key, and the AI model sees only the token. The AI's answer still holds the token. Your app sends the answer back to SDP, which swaps the token for the original value using the same key, and the user sees the real value.">
            <defs>
              %s
              %s
            </defs>
            <rect class="box" x="10" y="20" width="200" height="80" rx="8"/>
            <text class="tb" x="110" y="50" text-anchor="middle">User's message</text>
            <text class="ts" x="110" y="70" text-anchor="middle">holds a real value</text>
            <line class="ln" x1="210" y1="60" x2="270" y2="60" marker-end="url(#a7)"/>
            <rect class="gate" x="275" y="20" width="200" height="80" rx="8"/>
            <text class="tb" x="375" y="50" text-anchor="middle">SDP swaps in a token</text>
            <text class="ts" x="375" y="70" text-anchor="middle">encrypted with your key</text>
            <line class="led" x1="475" y1="60" x2="535" y2="60" marker-end="url(#a7e)"/>
            <rect class="ed" x="540" y="20" width="210" height="80" rx="8"/>
            <text class="tb" x="645" y="50" text-anchor="middle">AI model sees a token</text>
            <text class="ts" x="645" y="70" text-anchor="middle">never the real value</text>
            <path class="ln" d="M645,100 V166" marker-end="url(#a7)"/>
            <text class="ts" x="375" y="140" text-anchor="middle">your app makes both requests and keeps the key</text>
            <rect class="box" x="540" y="170" width="210" height="80" rx="8"/>
            <text class="tb" x="645" y="200" text-anchor="middle">AI's answer</text>
            <text class="ts" x="645" y="220" text-anchor="middle">still holds the token</text>
            <line class="ln" x1="540" y1="210" x2="480" y2="210" marker-end="url(#a7)"/>
            <rect class="gate" x="275" y="170" width="200" height="80" rx="8"/>
            <text class="tb" x="375" y="200" text-anchor="middle">SDP swaps it back</text>
            <text class="ts" x="375" y="220" text-anchor="middle">same key, whole token</text>
            <line class="ln" x1="275" y1="210" x2="215" y2="210" marker-end="url(#a7)"/>
            <rect class="box" x="10" y="170" width="200" height="80" rx="8"/>
            <text class="tb" x="110" y="200" text-anchor="middle">User sees the real value</text>
            <text class="ts" x="110" y="220" text-anchor="middle">your app shows it</text>
          </svg>""" % (marker("a7", "ah"), marker("a7e", "ahed"))

r7 = rail(
    7, "Reversible stand-in tokens",
    'Reversible tokens (AES-SIV and format-preserving encryption) · input and output · ' + YES,
    tokens_svg(),
    "Two reversible methods exist: AES-SIV, a standard encryption mode that Google recommends, and format-preserving encryption, which keeps a value's length and character set but 'can run very slowly'. The key can be kept wrapped by Cloud KMS, Google's key-storage service. To swap back, your app sends the whole token and the same key.",
    [("Rule", "Token form: name, then the length of the coded part in brackets, then the coded part (Google's docs)"),
     ("Masked", "An email address becomes <mark>EMAIL_ADDRESS_TOKEN(52):AVAx2eIEnIQP5jbNEr2j9wLOAd5m4kpSBR/0jjjGdAOmryzZbE/q.</mark>")],
    "None of the Google pages we read describes a round trip through an AI model, so it only works if the model repeats the token unchanged. Google's docs disagree on whether an AES-SIV token keeps the length of the original value. The client docs warn that re-identifying text can restore a stand-in that matches no real value, or fail, so the token name must not occur naturally in your data.")

stage_custom = """<section class="stage">
  <div class="stage-head">
    <div class="eyebrow">Input and output · Custom detectors and tokens</div>
    <h2>Your own list of things to find, and reversible stand-ins</h2>
    <p>Two extras sit on the same requests. Custom detectors add your own word lists and patterns to the built-in ones. Reversible tokens swap a value for a coded stand-in that your app can swap back later.</p>
  </div>

  <div class="grid2">
%s

%s
  </div>
</section>""" % (r6, r7)

# ----------------------------------------------------------------------------------------------
# Stage 2b Images
# ----------------------------------------------------------------------------------------------
r8 = rail(
    8, "Finding and covering details in a picture",
    'Image detection and redaction · input and output · ' + YES,
    linear(8,
           "A picture goes to SDP, which reads any text in it with optical character recognition and looks for objects such as passports and photo ID cards. SDP returns boxes around the matches, or the same picture with opaque rectangles drawn over them, and your app decides what to do with the result.",
           "Picture", "screenshot, scan or photo", "gate",
           "Read and find", "text read by OCR,", "objects found in pixels", "ed",
           "Picture with boxes drawn", "opaque rectangles on matches", edit_label="covers"),
    "SDP reads text in the picture with optical character recognition (OCR, software that turns pictures of text into text), then runs the text detectors on it. Separate detectors look at the pixels for passports, photo ID cards, signatures, licence plates, barcodes, whiteboards and faces (faces are in Preview, Google's pre-release stage). 'Inspect' returns pixel boxes; 'redact' returns the picture with rectangles, black by default.",
    [("In", "A user-submitted screenshot showing an account number and contact details (Google's documented use case)"),
     ("Out", "The same screenshot with opaque rectangles over those details")],
    "Google names no OCR languages and publishes no accuracy for text or object detection. Six statements in its docs disagree on which image formats work (PNG, JPEG and BMP are named most often), and its pages differ on whether box coordinates start at the upper left or the bottom left. Whether the passport and ID-card detectors recognise Singapore documents is not stated.")

r9 = rail(
    9, "Judging the whole picture",
    'Image safety classification · input and output · ' + PARTLY,
    fork(9,
         "A picture is checked by SDP's image safety check, which looks at the whole picture for three categories: sexually explicit, sexually suggestive and violent. If nothing is found, the picture continues. If a category is found, SDP returns a finding with a likelihood level and your app blocks the picture.",
         "Picture", "upload or AI-made", "part",
         "Image safety check", "whole picture, 3 categories", "explicit · suggestive · violent",
         "clear", "found",
         "Picture continues", "nothing changed",
         "Your app blocks the picture", "SDP gives a finding only"),
    "Unlike the object detectors in diagram 8, this check judges the picture's overall subject. Only three categories are listed. If you ask SDP to blank a picture on these findings, it covers the entire picture.",
    [("In", "An uploaded photo that shows violence (illustrative)"),
     ("Result", "A finding for the violence category with a likelihood level; Google shows no worked example (illustrative)")],
    "Google says the models are 'primarily trained and evaluated on real-world images', results on AI-generated images 'can vary', and 'Don't rely solely on these classifiers for safety assurances in high-risk generative AI applications.' No accuracy is published and the model is not named.")

stage_images = """<section class="stage">
  <div class="stage-head">
    <div class="eyebrow">Stage 2b · Images</div>
    <h2>Looking inside pictures</h2>
    <p>Text printed in a picture and objects such as ID cards can be found and covered. A separate check judges the whole picture for sexual or violent content. Pictures work only in listed regions, which include Singapore.</p>
  </div>

  <div class="grid2">
%s

%s
  </div>
</section>""" % (r8, r9)

# ----------------------------------------------------------------------------------------------
# Stage 3 Retrieval
# ----------------------------------------------------------------------------------------------
r10 = rail(
    10, "Personal data in passages and files",
    'Same detectors, run on passages and files · retrieval · ' + PARTLY,
    fork(10,
         "A passage or file fetched for the AI model is checked by SDP for personal data and keys, but not for hidden instructions. If nothing is found, the passage goes to the AI model unchanged. If something is found, your app drops or masks the passage, because SDP only reports.",
         "Passage or file", "text, or a PDF file", "part",
         "Sensitive-data check", "personal data and keys", "not hidden instructions",
         "clear", "found",
         "Continues to the AI model", "nothing changed",
         "Your app drops or masks it", "you choose; SDP only reports"),
    "NeMo's diagram 5 masks personal data on retrieved passages in the same spirit. SDP's request has no document or retrieval setting: your app sends the passage as ordinary text, or the file's bytes, and reads the findings.",
    [("Passage", "Ticket raised by Ahmad Rahim, phone 9123 4567. (illustrative)"),
     ("Result", "A person name is likely to be found; whether a Singapore phone number is found is not stated (illustrative)")],
    "None of the Google pages we read describes checking retrieved passages, so this is our reading of the request format. Masking is shown for plain text and CSV or TSV files only: the docs list no masking for PDF, Word, Excel or PowerPoint files, although PDF bytes can be inspected.")

stage_retrieval = """<section class="stage">
  <div class="stage-head">
    <div class="eyebrow">Stage 3 · Retrieval</div>
    <h2>Checking passages and files pulled from your documents</h2>
    <p>SDP has no retrieval-specific check. It can look for personal data and secrets in any text or file your app sends, so a passage can be checked before it goes to the AI model. The docs name no detector for instructions hidden in a passage, so that risk is not covered.</p>
  </div>

%s
</section>""" % r10

# ----------------------------------------------------------------------------------------------
# Scorecard
# ----------------------------------------------------------------------------------------------
scorecard = """<section class="stage">
  <div class="stage-head">
    <div class="eyebrow">At a glance</div>
    <h2>SDP at NeMo's five checkpoints</h2>
    <p>The same five places NeMo can check, plus pictures and monitoring, with an honest answer for each.</p>
  </div>
  <div class="tablewrap">
    <table class="cats">
      <thead><tr><th>Checkpoint</th><th>SDP?</th><th>Why</th></tr></thead>
      <tbody>
        <tr><td>Input</td><td>%(yes)s</td><td>Personal data and secrets in text, from built-in detectors and your own, with masking or reversible tokens (diagrams 3, 4, 6 and 7). It does not check for attacks, jailbreaks or harmful wording; the docs name no such detector.</td></tr>
        <tr><td>Output</td><td>%(yes)s</td><td>The same calls can run on the AI's draft answer (diagram 5). That is our reading of the request, which has no input or output setting; Google's examples describe prompts.</td></tr>
        <tr><td>Retrieval (your documents)</td><td>%(partly)s</td><td>Personal data and secrets in any passage or file your app sends (diagram 10), but nothing checks for instructions hidden in a document, and none of the Google pages we read describes retrieval use.</td></tr>
        <tr><td>Dialog (topics, fixed replies)</td><td>%(no)s</td><td>No topic rules and no fixed replies. Document-category detectors for politics, religion or offensive topics are listed, but whether they run on a plain text string is not stated.</td></tr>
        <tr><td>Execution (actions, tools)</td><td>%(no)s</td><td>No check for tool requests or actions. Text going into or out of a tool could be sent through the same calls, but nothing official describes this, and business limits like NeMo's diagram 8 still need a written rule.</td></tr>
        <tr><td>Images</td><td>%(yes)s</td><td>Text and ID-type objects in pictures can be found and covered (diagram 8). The whole-picture safety check covers three categories only (diagram 9), which is why it is marked Partly there.</td></tr>
        <tr><td>Monitoring</td><td>%(no)s</td><td>Scheduled scans and data profiles look at stored data, such as Cloud Storage and BigQuery, not at chat traffic. A hybrid scan can take data from other sources, but it returns findings later, not to your app.</td></tr>
      </tbody>
    </table>
  </div>
</section>""" % dict(yes=YES, partly=PARTLY, no=NO)

# ----------------------------------------------------------------------------------------------
# Limitations
# ----------------------------------------------------------------------------------------------
limits = """<section class="stage">
  <div class="stage-head">
    <div class="eyebrow">Limitations</div>
    <h2>What SDP does not do, or does not tell us</h2>
  </div>
  <article class="rail">
    <ul class="limits">
      <li><b>It never acts.</b> You get findings or a cleaned copy, not decisions, and Google gives no recommended cut-off for chat text. Your app refuses, discards, masks and replies. A separate content-policy feature does return allow or block, but no documented call lets your own app send it text, so it is left out of this page.</li>
      <li><b>It does not judge what is said.</b> The docs name no detector for prompt attacks, jailbreaks, harmful text or off-topic questions. The only harm check is the three picture categories in diagram 9.</li>
      <li><b>No published accuracy.</b> Google publishes no precision, recall or speed figure for any detector, including the Singapore NRIC one, and says detectors are 'not a perfectly accurate detection method'. It promises 99.5% monthly uptime for the inspect and de-identify calls in most regions; no uptime figure is stated for re-identify or picture redaction.</li>
      <li><b>Singapore coverage is thin and partly unknown.</b> NRIC and passport numbers have detectors. No FIN, UEN, +65 phone or address detector is named, and support for Chinese, Malay, Tamil and Singlish is not stated.</li>
      <li><b>Models are not named, and they change.</b> The person-name detector's backing model, the OCR and the picture classifiers are not disclosed. A new person-name version was announced on 2026-10-03 and is due to become the standard about 30 days later, so the same test can give different results over time.</li>
      <li><b>Its docs disagree in places.</b> They differ on which detectors run when you list none, which image formats work, where picture box coordinates start, whether AES-SIV tokens keep the original length, the output format of the one-way hash, and the order rules run in.</li>
      <li><b>Your text goes to Google's API.</b> No offline mode was found. Google says request data is encrypted in transit and not stored, and that regional addresses (one exists for Singapore) keep data in the chosen place, while the global address makes no such promise for data in transit. What the web demo does with text is not described.</li>
      <li><b>Caps, cost and test terms apply.</b> A request is capped at 0.5 MB (4 MB for picture redaction), and the first gibibyte (a little over a billion bytes) a month is free, then $3.00 per gibibyte inspected. The face detector is in Preview, so Google's terms say it has no SLA. Published test results need all the information to replicate them, and Google's Acceptable Use Policy bars illegal content; which explicit or violent test pictures are acceptable is for the bench design to decide.</li>
    </ul>
  </article>
</section>"""

footer = """<footer>
  <p>Sources: Google Cloud's Sensitive Data Protection documentation (overview, detector reference, likelihood, de-identification, transformations, pseudonymisation, custom detectors and rules, image guides, locations, endpoints, limits and release notes), its pricing and uptime pages, Google's Model Armor and Gemini Enterprise pages (for the links to SDP only), the Google Cloud terms and Acceptable Use Policy, and the google-cloud-dlp Python client source at release 3.40.0. All pages were read on 2026-10-09. Google publishes no accuracy figures for SDP, so none appear here. Limits, prices and dates are from Google's pages. Examples marked illustrative are invented; the others are quoted from Google's docs.</p>
  <p><a href="https://docs.cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview">SDP overview</a> · <a href="https://docs.cloud.google.com/sensitive-data-protection/docs/infotypes-reference">Detector reference</a> · <a href="https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-infotypes">Detector concepts</a> · <a href="https://docs.cloud.google.com/sensitive-data-protection/docs/likelihood">Likelihood</a> · <a href="https://docs.cloud.google.com/sensitive-data-protection/docs/inspecting-text">Inspecting text</a> · <a href="https://docs.cloud.google.com/sensitive-data-protection/docs/deidentify-sensitive-data">De-identifying text</a> · <a href="https://docs.cloud.google.com/sensitive-data-protection/docs/transformations-reference">Transformations</a> · <a href="https://docs.cloud.google.com/sensitive-data-protection/docs/pseudonymization">Pseudonymisation</a> · <a href="https://docs.cloud.google.com/sensitive-data-protection/docs/inspect-sensitive-text-de-identify">Quickstart: tokens</a> · <a href="https://docs.cloud.google.com/sensitive-data-protection/docs/creating-custom-infotypes">Custom detectors</a> · <a href="https://docs.cloud.google.com/sensitive-data-protection/docs/creating-custom-infotypes-rules">Inspection rules</a> · <a href="https://docs.cloud.google.com/sensitive-data-protection/docs/creating-custom-infotypes-likelihood">Match likelihood</a> · <a href="https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-image-redaction">Images</a> · <a href="https://docs.cloud.google.com/sensitive-data-protection/docs/inspecting-images">Inspecting images</a> · <a href="https://docs.cloud.google.com/sensitive-data-protection/docs/redacting-sensitive-data-images">Redacting images</a> · <a href="https://docs.cloud.google.com/sensitive-data-protection/docs/supported-file-types">File types</a> · <a href="https://docs.cloud.google.com/sensitive-data-protection/docs/locations">Locations</a> · <a href="https://docs.cloud.google.com/sensitive-data-protection/docs/api-endpoints">API endpoints</a> · <a href="https://docs.cloud.google.com/sensitive-data-protection/docs/release-notes">Release notes</a> · <a href="https://docs.cloud.google.com/sensitive-data-protection/docs/content-policy">Content policies</a> · <a href="https://docs.cloud.google.com/sensitive-data-protection/limits">Limits</a> · <a href="https://cloud.google.com/sensitive-data-protection/pricing">Pricing</a> · <a href="https://cloud.google.com/sensitive-data-protection/sla">Uptime (SLA)</a> · <a href="https://docs.cloud.google.com/model-armor/overview">Model Armor overview</a> · <a href="https://docs.cloud.google.com/model-armor/sanitize-prompts-responses">Model Armor: sanitising</a> · <a href="https://docs.cloud.google.com/gemini/enterprise/docs/protect-sensitive-data">Gemini Enterprise: protect data</a> · <a href="https://cloud.google.com/terms">Google Cloud terms</a> · <a href="https://cloud.google.com/terms/data-processing-addendum">Data Processing Addendum</a> · <a href="https://cloud.google.com/terms/service-terms">Service Specific Terms</a> · <a href="https://cloud.google.com/terms/aup">Acceptable Use Policy</a> · <a href="https://github.com/googleapis/google-cloud-python/blob/google-cloud-dlp-v3.40.0/packages/google-cloud-dlp/google/cloud/dlp_v2/types/dlp.py">Python client source (3.40.0)</a></p>
</footer>"""

header = """<header>
  <div class="eyebrow">Google Cloud Sensitive Data Protection · formerly Cloud DLP</div>
  <h1>How Google Cloud Sensitive Data Protection screens a conversation</h1>
  <p class="lede">Sensitive Data Protection (SDP) is a Google Cloud service, formerly called Cloud DLP (data loss prevention), that finds sensitive data such as names, ID numbers and secret keys in text and pictures. Your app sends it text or an image in one web request and gets back a list of what it found, or a copy with those values masked or swapped for tokens. It never blocks anything itself. This page shows what it can find, where it fits in a chat, and what it does not cover.</p>
  <div class="legend" aria-label="Colour key">
    <span><i class="sw gate"></i>Check done by SDP</span>
    <span><i class="sw dev"></i>Your app's job (not SDP)</span>
    <span><i class="sw pass"></i>Allowed through</span>
    <span><i class="sw stop"></i>Stopped</span>
    <span><i class="sw edit"></i>Changed, then allowed</span>
    <span><i class="sw part"></i>Partly supported</span>
    <span><i class="sw na"></i>Not supported</span>
  </div>
</header>"""

layout_comment = ("/* Layout: one reading column; overview map, four-way comparison, how it works, then checkpoints "
                  "(input, output, custom detectors and tokens, images, retrieval), a scorecard and limits */")

page = "\n".join([
    "<title>How Google Cloud Sensitive Data Protection Screens a Conversation</title>",
    preconnect,
    fonts_line,
    "<style>",
    layout_comment,
    base_css,
    "/* Additions for this page: links to sibling pages inside body text */",
    ".stage-head a, .know a { color: var(--accent); }",
    "</style>",
    "",
    '<div class="wrap">',
    "",
    header,
    "",
    "<!-- OVERVIEW -->",
    overview,
    "",
    "<!-- FOUR-WAY -->",
    positioning,
    "",
    "<!-- HOW IT WORKS -->",
    how,
    "",
    "<!-- INPUT -->",
    stage1,
    "",
    "<!-- OUTPUT -->",
    stage2,
    "",
    "<!-- CUSTOM DETECTORS AND TOKENS -->",
    stage_custom,
    "",
    "<!-- IMAGES -->",
    stage_images,
    "",
    "<!-- RETRIEVAL -->",
    stage_retrieval,
    "",
    "<!-- SCORECARD -->",
    scorecard,
    "",
    "<!-- LIMITATIONS -->",
    limits,
    "",
    footer,
    "",
    "</div>",
    "",
])

with io.open(OUT, "w", encoding="utf-8", newline="\n") as f:
    f.write(page)
print("wrote", OUT, len(page))
