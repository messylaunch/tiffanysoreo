#!/usr/bin/env python3
"""Generates oreo-lady-game-plan.pdf — the actionable field guide for Tiffany."""
import os
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor, white
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph,
                                Spacer, PageBreak, Table, TableStyle,
                                NextPageTemplate)

NAVY = HexColor("#0A1045")
NAVY_DEEP = HexColor("#060B2E")
PINK = HexColor("#FF2E9A")
PINK_SOFT = HexColor("#FFE6F3")
CYAN = HexColor("#0FA8C9")
CREAM = HexColor("#FFF8EE")
INK = HexColor("#221F2E")
GRAY = HexColor("#5E5A6E")
LINE = HexColor("#E7E3EF")

OUT = os.path.join(os.path.dirname(__file__), "..", "oreo-lady-game-plan.pdf")
W, H = letter

# ---------------- styles ----------------
def st(name, **kw):
    base = dict(fontName="Helvetica", fontSize=10.5, leading=15, textColor=INK)
    base.update(kw)
    return ParagraphStyle(name, **base)

S = {
    "kicker":   st("kicker", fontName="Helvetica-Bold", fontSize=9, leading=12,
                   textColor=PINK, spaceAfter=4, spaceBefore=0),
    "h1":       st("h1", fontName="Helvetica-Bold", fontSize=21, leading=25,
                   textColor=NAVY, spaceAfter=10),
    "h2":       st("h2", fontName="Helvetica-Bold", fontSize=13, leading=17,
                   textColor=NAVY, spaceBefore=12, spaceAfter=5),
    "body":     st("body", spaceAfter=7),
    "small":    st("small", fontSize=9, leading=13, textColor=GRAY),
    "check":    st("check", fontSize=10.5, leading=15, leftIndent=24,
                   firstLineIndent=-24, spaceAfter=7),
    "tmplhead": st("tmplhead", fontName="Helvetica-Bold", fontSize=9,
                   textColor=CYAN, spaceAfter=2),
    "tmpl":     st("tmpl", fontName="Helvetica-Oblique", fontSize=10, leading=14,
                   textColor=INK),
}

def check(text):
    return Paragraph(
        '<font face="ZapfDingbats" color="#FF2E9A">o</font>&nbsp;&nbsp;' + text,
        S["check"])

def box(flowables, bg=CREAM, border=PINK):
    t = Table([[flowables]], colWidths=[6.6 * inch])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), bg),
        ("BOX", (0, 0), (-1, -1), 1.2, border),
        ("LEFTPADDING", (0, 0), (-1, -1), 14),
        ("RIGHTPADDING", (0, 0), (-1, -1), 14),
        ("TOPPADDING", (0, 0), (-1, -1), 10),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
        ("ROUNDEDCORNERS", [6, 6, 6, 6]),
    ]))
    return t

def tmpl_box(label, text):
    return box([Paragraph(label, S["tmplhead"]), Paragraph(text, S["tmpl"])],
               bg=PINK_SOFT, border=PINK)

# ---------------- page furniture ----------------
def cover(canv, doc):
    canv.saveState()
    canv.setFillColor(NAVY_DEEP)
    canv.rect(0, 0, W, H, fill=1, stroke=0)
    # star field
    import random
    random.seed(7)
    for _ in range(120):
        x, y = random.uniform(0, W), random.uniform(0, H)
        r = random.uniform(0.4, 1.6)
        canv.setFillColor(white if random.random() > .2 else PINK)
        canv.circle(x, y, r, fill=1, stroke=0)
    # pink band
    canv.setFillColor(PINK)
    canv.rect(0, H - 3.1 * inch, W, 0.16 * inch, fill=1, stroke=0)
    canv.setFillColor(white)
    canv.setFont("Helvetica-Bold", 13)
    canv.drawCentredString(W / 2, H - 2.35 * inch, "T H E   O R E O   L A D Y")
    canv.setFont("Helvetica-Bold", 40)
    canv.drawCentredString(W / 2, H - 4.1 * inch, "THE GAME PLAN")
    canv.setFillColor(HexColor("#29D8FF"))
    canv.setFont("Helvetica-Bold", 14)
    canv.drawCentredString(W / 2, H - 4.75 * inch,
                           "From flyer to machine — your first 30 days")
    canv.setFillColor(white)
    canv.setFont("Helvetica", 11)
    for i, line in enumerate([
        "How to use the website while you're out serving.",
        "What to do this week with what you already have.",
        "Your first text campaign, word for word.",
        "The simple tech build — and what waits for later.",
    ]):
        canv.drawCentredString(W / 2, H - 5.7 * inch - i * 0.3 * inch, line)
    canv.setFillColor(PINK)
    canv.setFont("Helvetica-Bold", 12)
    canv.drawCentredString(W / 2, 1.5 * inch,
                           "Start on page 2. Do the checkboxes in order. Come hungry.")
    canv.setFillColor(HexColor("#8A86A0"))
    canv.setFont("Helvetica", 8.5)
    canv.drawCentredString(W / 2, 0.9 * inch,
                           "Prepared July 2026  ·  TikTok @theoreolady863  ·  facebook.com/theoreolady863")
    canv.restoreState()

def later(canv, doc):
    canv.saveState()
    canv.setFillColor(NAVY)
    canv.rect(0, H - 0.42 * inch, W, 0.42 * inch, fill=1, stroke=0)
    canv.setFillColor(white)
    canv.setFont("Helvetica-Bold", 8.5)
    canv.drawString(0.85 * inch, H - 0.28 * inch, "THE OREO LADY — GAME PLAN")
    canv.setFillColor(PINK)
    canv.drawRightString(W - 0.85 * inch, H - 0.28 * inch, "PAGE %d" % doc.page)
    canv.setFillColor(PINK)
    canv.rect(0, 0.5 * inch, W, 0.045 * inch, fill=1, stroke=0)
    canv.restoreState()

doc = BaseDocTemplate(OUT, pagesize=letter,
                      leftMargin=0.85 * inch, rightMargin=0.85 * inch,
                      topMargin=0.85 * inch, bottomMargin=0.85 * inch,
                      title="The Oreo Lady — Game Plan",
                      author="Prepared for The Oreo Lady")
frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="f")
doc.addPageTemplates([
    PageTemplate(id="cover", frames=[frame], onPage=cover),
    PageTemplate(id="page", frames=[frame], onPage=later),
])

E = []  # story
E.append(Paragraph("", S["body"]))  # cover has no flowables
E.append(NextPageTemplate("page"))  # everything after the cover uses the content template
E.append(PageBreak())

# ---------------- p2: this week ----------------
E.append(Paragraph("STEP 1 · THIS WEEK — NO NEW TOOLS, NO NEW COSTS", S["kicker"]))
E.append(Paragraph("Start with what you already have", S["h1"]))
E.append(Paragraph(
    "You don't need to wait on any tech to start. These five moves cost nothing "
    "and build the asset everything else runs on: <b>a list of people who want to "
    "know where you are.</b>", S["body"]))
E.append(check("<b>Put the website link everywhere.</b> TikTok bio, Facebook page, "
               "and one pinned post that says: “Menu + this week's schedule + "
               "book me — all right here.”"))
E.append(check("<b>Start collecting numbers TODAY.</b> A notes app or a paper sheet "
               "on the table is fine. The line is one sentence: “Want a text "
               "when I'm in your area?” Say it to every single customer."))
E.append(check("<b>Pick ONE schedule day and never miss it.</b> Every Sunday: post "
               "the week's spots on TikTok + Facebook. Same day, every week — "
               "people learn to look for it."))
E.append(check("<b>Post a story the moment you set up.</b> Every stop, every time: "
               "where you are, until when, what's fresh. 15 seconds."))
E.append(check("<b>Ask for the follow at the table.</b> Hand them the box, then: "
               "“Follow the TikTok — that's where I drop where I'll be.”"))
E.append(Spacer(1, 10))
E.append(box([
    Paragraph("MICHAEL HANDLES THIS PART", S["tmplhead"]),
    Paragraph("Put the website live on a real domain (Vercel). Print two things: "
              "a QR table-tent that opens the site, and small QR cards to drop in "
              "every box. File the A2P texting registration the day the GHL "
              "account opens — it takes 1–2 weeks to approve, so it starts "
              "first.", S["body"]),
], bg=CREAM, border=CYAN))

E.append(PageBreak())

# ---------------- p3: using the site ----------------
E.append(Paragraph("STEP 2 · YOUR WEBSITE, WORKING WHILE YOU FRY", S["kicker"]))
E.append(Paragraph("How to use the site in the field & online", S["h1"]))
E.append(Paragraph("The site has three jobs. Point people at the right one and it "
                   "answers questions so you don't have to stop frying.", S["body"]))
t = Table([
    [Paragraph("<b>MENU</b>", S["body"]),
     Paragraph("Answers “how much?” — 6 for $10 regular, 4 for $10 Dubai, "
               "3+3 for $10 half/half. Point the QR at anyone in line deciding.", S["body"])],
    [Paragraph("<b>FIND ME</b>", S["body"]),
     Paragraph("Where the schedule lives. Your Sunday post should say: “full "
               "week on the site.” One link instead of 30 DMs.", S["body"])],
    [Paragraph("<b>BOOK ME</b>", S["body"]),
     Paragraph("Events, parties, business pop-ups. When someone says “come to "
               "my job!” — “Hit Book Me on my site, I'll get you "
               "scheduled.”", S["body"])],
], colWidths=[1.1 * inch, 5.5 * inch])
t.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (0, -1), PINK_SOFT),
    ("GRID", (0, 0), (-1, -1), 0.8, LINE),
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ("LEFTPADDING", (0, 0), (-1, -1), 10),
    ("RIGHTPADDING", (0, 0), (-1, -1), 10),
    ("TOPPADDING", (0, 0), (-1, -1), 8),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
]))
E.append(t)
E.append(Paragraph("In person", S["h2"]))
E.append(check("QR tent faces the line. Your line: “Scan that — menu, my "
               "schedule, and how to book me.”"))
E.append(check("QR card in every box — the box travels to offices and parties; "
               "that's free advertising to people who already tasted it."))
E.append(Paragraph("Online", S["h2"]))
E.append(check("Sunday schedule post links the site. Share it into 2–3 local "
               "community Facebook groups (where allowed)."))
E.append(check("Anyone who DMs “where are you?” gets the link — one tap, "
               "done, back to frying."))
E.append(check("Every viral-ish TikTok comment section: pin “schedule's on the "
               "site, link in bio.”"))

E.append(PageBreak())

# ---------------- p4: phase-1 GHL ----------------
E.append(Paragraph("STEP 3 · THE SIMPLE TECH BUILD (PHASE 1)", S["kicker"]))
E.append(Paragraph("Four pieces of GoHighLevel. Only four.", S["h1"]))
E.append(Paragraph(
    "Michael sets all of this up — your job is just to use it. The rule for "
    "phase 1: <b>if it isn't one of these four pieces, it waits.</b>", S["body"]))
E.append(check("<b>1. The account + a real business phone number.</b> One number for "
               "calls and texts that isn't your personal cell. A2P registration is "
               "filed on day one (1–2 week government-ish wait — this is why "
               "we start now)."))
E.append(check("<b>2. One list + one join form.</b> The QR cards and a keyword "
               "point here. Every number you collected on paper gets typed in too. "
               "This list is the business."))
E.append(check("<b>3. A booking calendar with a small deposit.</b> “Book Me” "
               "on the site points here. A $25 deposit ends no-show parties "
               "forever."))
E.append(check("<b>4. Missed-call text-back.</b> You're frying, a call comes in, "
               "you miss it — they instantly get: “Frying right now! "
               "Book me or find today's spot here.” A missed call stops being "
               "a lost customer."))
E.append(Spacer(1, 8))
E.append(box([
    Paragraph("DO NOT BUILD MORE YET", S["tmplhead"]),
    Paragraph("No funnels, no AI bots, no 12-step automations in month one. "
              "Every fancy thing added before the basics work is a thing that "
              "breaks while you're busy. The list, the calendar, and the "
              "text-back earn money first.", S["body"]),
]))
E.append(Spacer(1, 8))
E.append(Paragraph(
    "<b>Cost reality:</b> the software runs roughly $97/mo at the base plan plus "
    "pennies per text (a 200-person blast is a couple of dollars) — Michael will "
    "confirm current pricing. One extra $10 box per stop covers it.", S["small"]))

E.append(PageBreak())

# ---------------- p5: first campaign ----------------
E.append(Paragraph("STEP 4 · YOUR FIRST CAMPAIGN", S["kicker"]))
E.append(Paragraph("“The Drop List” — 100 numbers in 30 days", S["h1"]))
E.append(Paragraph(
    "One goal: 100 people on the text list in your first month. At your prices, "
    "a 100-person list that shows up even 10% of the time is an extra 10 boxes "
    "every single stop.", S["body"]))
E.append(check("<b>The hook:</b> joining gets a treat — e.g. a free extra Oreo with "
               "their next box, or first dibs when Dubai sells out. (Pick one, "
               "keep it cheap, honor it every time.)"))
E.append(check("<b>The ask, at every table:</b> “Join my text list — I'll ping "
               "you when I'm in your area, and you get [the perk].”"))
E.append(check("<b>The rhythm:</b> exactly two texts a week. Sunday = the week's "
               "schedule. Day-of = “I'm posted up.” Never more — the list "
               "stays golden because you don't spam it."))
E.append(Paragraph("Copy-paste texts (fill the [brackets], add your emojis when "
                   "you send — cookie, sparkle, heart)", S["h2"]))
E.append(tmpl_box("TEXT 1 — WHEN SOMEONE JOINS",
    "It's the Oreo Lady! You're on the list — you'll get a text when "
    "I'm setting up near you. Show this text next visit for [your perk]. "
    "Reply STOP anytime."))
E.append(Spacer(1, 6))
E.append(tmpl_box("TEXT 2 — SUNDAY SCHEDULE",
    "This week's fry-up: [Day] — [spot], [Day] — [spot], [Day] — [spot]. "
    "Full schedule + menu: [site link]. Come hungry!"))
E.append(Spacer(1, 6))
E.append(tmpl_box("TEXT 3 — DAY-OF DROP",
    "Fresh batch! I'm at [location] until [time] — regular, Dubai "
    "chocolate pistachio, and half/half boxes ready. First come, first served!"))
E.append(Paragraph("Track three numbers weekly", S["h2"]))
E.append(Paragraph("List size &nbsp;•&nbsp; perk redemptions &nbsp;•&nbsp; "
                   "sell-out time. If sell-out time keeps shrinking, the list is "
                   "working — raise the batch size, not the prices.", S["body"]))

E.append(PageBreak())

# ---------------- p6: later / AI builder ----------------
E.append(Paragraph("STEP 5 · LATER — ONLY AFTER THE LIST WORKS", S["kicker"]))
E.append(Paragraph("Phase 2: what the AI builder adds", S["h1"]))
E.append(Paragraph(
    "Once the list is past ~100 and the weekly rhythm is habit, GHL's AI tools "
    "start earning their keep. Each one is a single afternoon for Michael to "
    "switch on:", S["body"]))
E.append(check("<b>AI booking funnel</b> — a one-page event-booking funnel (built "
               "with the AI page builder) that upsells party platters when someone "
               "books a date."))
E.append(check("<b>Conversation AI</b> — answers the same five DM questions "
               "(where are you / how much / do you deliver / can you do my event / "
               "what's Dubai chocolate) instantly, 24/7, in your voice."))
E.append(check("<b>Auto review requests</b> — the day after every event: "
               "“Leave a review + tag a photo” text while the sugar's "
               "still on their fingers."))
E.append(check("<b>30-day win-back</b> — anyone who hasn't opened/visited in 30 "
               "days gets one “we miss you — I'm near you Thursday” text."))
E.append(check("<b>Card-on-file payments</b> — invoices and tap-to-pay for event "
               "bookings so deposits and balances collect themselves."))
E.append(Spacer(1, 8))
E.append(box([
    Paragraph("THE ORDER MATTERS", S["tmplhead"]),
    Paragraph("List → rhythm → bookings → automation. Skipping ahead "
              "builds robots with nobody to talk to. The paper sheet of phone "
              "numbers in week one is worth more than any AI feature in month "
              "one.", S["body"]),
]))

E.append(PageBreak())

# ---------------- p7: checklist ----------------
E.append(Paragraph("THE BACK PAGE — TEAR-OFF", S["kicker"]))
E.append(Paragraph("First steps, in order", S["h1"]))
E.append(Paragraph("If this is the only page you keep, keep this one.", S["body"]))
for i, item in enumerate([
    "Site link in TikTok + Facebook bios, one pinned post. <i>(today)</i>",
    "Numbers sheet on the table — ask every customer. <i>(today)</i>",
    "Pick your schedule day (Sunday) — post this week's spots. <i>(this week)</i>",
    "Story at every setup: where + until when. <i>(every stop)</i>",
    "Michael: site on the real domain + QR tent & box cards printed. <i>(this week)</i>",
    "Michael: GHL account + number + A2P filed. <i>(day one — it has a wait)</i>",
    "Type the paper numbers into the list the day texting is approved. <i>(week 2–3)</i>",
    "Send Text 1 to everyone + start the Sunday/day-of rhythm. <i>(week 2–3)</i>",
    "Booking calendar with deposit live behind “Book Me.” <i>(week 3)</i>",
    "Day 30: count the list, the redemptions, the sell-outs — then unlock Phase 2. <i>(day 30)</i>",
], start=1):
    E.append(check("<b>%d.</b> %s" % (i, item)))
E.append(Spacer(1, 14))
E.append(box([
    Paragraph("REMEMBER", S["tmplhead"]),
    Paragraph("The product already sells itself — the whole plan is just making "
              "sure more people know where the fryer is. Two texts a week. One "
              "schedule day. Ask every customer. <b>Come hungry.</b>", S["body"]),
], bg=PINK_SOFT, border=PINK),)

doc.build(E)
print("wrote", os.path.abspath(OUT))
