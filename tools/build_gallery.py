#!/usr/bin/env python3
"""Regenerate the homepage gallery from every activity page.

Run after adding, removing, or recaptioning any photo or video anywhere:
    python3 tools/build_gallery.py

Scans each page in PAGES, collects its photos (.ph-item figures) and YouTube
embeds, and rewrites index.html's gallery grid + filter buttons so the gallery
always matches the pages, grouped per activity in GALLERY_ORDER. Captions carry
over. YouTube thumbnails are cached once into images/tiles/yt-<id>.jpg.
"""
import os, re, subprocess, sys, urllib.request

SITE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(SITE)

# category -> (page file, filter label)
PAGES = {
    'research':     ('research.html',     'Labor-Rights Research'),
    'jurio':        ('jurio.html',        'Jurio'),
    'lumen':        ('lumen.html',        'Lumen Education'),
    'welltain':     ('welltain.html',     'Welltain'),
    'puac':         ('puac.html',         'Peaceful Unification Advisory Council'),
    'soldiers':     ('soldiers.html',     "Soldiers' Angels"),
    'unmck':        ('unmck.html',        'UN Memorial Cemetery'),
    'mission':      ('mission.html',      'Mission Center for Migrants'),
    'mediawatch':   ('mediawatch.html',   'Media Watch'),
    'leaderstimes': ('leaderstimes.html', 'Leaders Times'),
    'kang':         ('kang.html',         'Undergraduate Research'),
    'lawgic':       ('lawgic.html',       'LAWGIC & A.C.E.'),
    'angels':       ('angels.html',       'Angels for the Journey'),
    'asianhub':     ('asianhub.html',     'AsianHub'),
    'isc':          ('isc.html',          'ISC Global'),
}

# gallery display order: newest work first
GALLERY_ORDER = ['research', 'jurio', 'lumen', 'welltain', 'puac', 'soldiers',
                 'unmck', 'mission', 'mediawatch', 'leaderstimes', 'kang',
                 'lawgic', 'angels', 'asianhub', 'isc']

# page images that should stay out of the gallery
SKIP_PREFIX = ('images/sites/',)

# site screenshots shown in the gallery for activities whose page embeds the live
# site instead of a screenshot (category -> image path)
EXTRA_IMAGES = {
    'lumen':  ('images/sites/site-lumen.jpg',  'https://lumen-education.squarespace.com/'),
    'angels': ('images/sites/site-angels.jpg', 'https://angels-journey.squarespace.com/'),
    'jurio':  ('images/sites/site-jurio.png',  'https://jurio-gamma.vercel.app/'),
    'unmck':  ('images/sites/site-unmck.jpg',  'https://busan-koreanwar-project.netlify.app/'),
}

FIG = re.compile(
    r'<figure class="(?:ph-item|hs-item)[^"]*"[^>]*>\s*<img[^>]*src="([^"]+)"[^>]*>'
    r'(?:<figcaption>(.*?)</figcaption>)?\s*</figure>', re.S)
VID = re.compile(r'youtube\.com/embed/([\w-]+)')


def yt_thumb(vid):
    path = f'images/tiles/yt-{vid}.jpg'
    if os.path.exists(path):
        return path
    os.makedirs('images/tiles', exist_ok=True)
    for name in ('maxresdefault', 'hqdefault'):
        try:
            req = urllib.request.Request(
                f'https://img.youtube.com/vi/{vid}/{name}.jpg',
                headers={'User-Agent': 'Mozilla/5.0'})
            data = urllib.request.urlopen(req, timeout=30).read()
            if len(data) > 5000:
                open(path, 'wb').write(data)
                subprocess.run(['sips', '-Z', '800', path], capture_output=True)
                return path
        except Exception:
            continue
    return None


def collect():
    groups, seen = {}, set()
    for cat in GALLERY_ORDER:
        page = PAGES[cat][0]
        if not os.path.exists(page):
            continue
        html = open(page, encoding='utf-8').read()
        cards = []
        extra = EXTRA_IMAGES.get(cat)
        if extra and os.path.exists(extra[0]) and extra[0] not in seen:
            seen.add(extra[0])
            cards.append(f'<a class="g-item" data-cat="{cat}" href="{extra[1]}" '
                         f'target="_blank" rel="noopener">'
                         f'<img loading="lazy" decoding="async" src="{extra[0]}" alt="">'
                         f'<figcaption>Visit site &#8599;</figcaption></a>')
        for src, cap in FIG.findall(html):
            if src in seen or src.startswith(SKIP_PREFIX):
                continue
            seen.add(src)
            cls = ' has-cap' if cap else ''
            capel = f'<figcaption>{cap}</figcaption>' if cap else ''
            cards.append(f'<figure class="g-item{cls}" data-cat="{cat}">'
                         f'<img loading="lazy" decoding="async" src="{src}" alt="">'
                         f'{capel}</figure>')
        for vid in dict.fromkeys(VID.findall(html)):
            if 'yt:' + vid in seen:
                continue
            seen.add('yt:' + vid)
            thumb = yt_thumb(vid)
            if thumb:
                cards.append(
                    f'<figure class="g-item g-vid" data-cat="{cat}" data-video="{vid}">'
                    f'<img loading="lazy" decoding="async" src="{thumb}" alt=""></figure>')
        if cards:
            groups[cat] = cards
    return groups


def main():
    groups = collect()
    items = ''.join(c for cat in GALLERY_ORDER for c in groups.get(cat, []))
    buttons = '<button class="g-fil is-on" data-f="all">All</button>' + ''.join(
        f'<button class="g-fil" data-f="{cat}">{PAGES[cat][1]}</button>'
        for cat in GALLERY_ORDER if cat in groups)

    s = open('index.html', encoding='utf-8').read()
    out, n_fil = re.subn(r'(<div class="g-fils">).*?(</div>)',
                         lambda m: m.group(1) + buttons + m.group(2), s, count=1, flags=re.S)
    out, n_grid = re.subn(r'(<div class="g-grid"[^>]*>).*?(</div>\s*</div>\s*</section>)',
                          lambda m: m.group(1) + items + m.group(2), out, count=1, flags=re.S)
    if not (n_fil and n_grid):
        print(f'gallery markup not found in index.html (filters={n_fil}, grid={n_grid}); nothing written')
        return 1
    if out == s:
        print('gallery already up to date; no change written')
    else:
        open('index.html', 'w', encoding='utf-8').write(out)

    total = sum(len(v) for v in groups.values())
    print(f'gallery rebuilt: {total} items across {len(groups)} activities')
    for cat in GALLERY_ORDER:
        if cat in groups:
            vids = sum(1 for c in groups[cat] if 'g-vid' in c)
            note = f' ({vids} video)' if vids else ''
            print(f'  {cat:13s} {len(groups[cat]):3d}{note}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
