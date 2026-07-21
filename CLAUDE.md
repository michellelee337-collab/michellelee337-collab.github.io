# Michelle's personal website (LIVE)

**Live:** https://michellelee337-collab.github.io/
**Repo:** github.com/michellelee337-collab/michellelee337-collab.github.io (public)
**Deployed:** July 21, 2026 via GitHub Pages from `main`.

Static HTML + one `styles.css`. No build step, no npm.

## Editing and publishing

1. Edit files here.
2. If any photo, video, or caption changed: `python3 tools/build_gallery.py`
3. Preview: serve a copy from `~/.claude/preview/michelle-website/`
   (macOS blocks preview servers reading ~/Desktop), then
   `rsync -a --delete ./ ~/.claude/preview/michelle-website/`
4. Publish:
   `git add -A && git commit -m "..." && git push`
   Pages redeploys in about a minute. Nothing else to do.

Every published version is in git history, so any change can be reverted:
`git log --oneline` then `git revert <hash>`.

## Rules that still apply

Read `~/.claude/context/website-state.md` before edits; facts go through
`~/.claude/context/facts-verified.md`. Style counts before "done": 0 em/en-dashes,
0 exclamation marks in site copy, no cross-page duplicate images.

## Assets

- `images/` holds every file the site uses. The site is self-contained:
  nothing references the Desktop, so Desktop originals can be deleted safely.
- `images/_archive/` holds 245 unused originals (75 MB). Kept on disk,
  excluded from git by `.gitignore`, so they never reach the public site.
- Large images are capped at 1400px; photo PNGs were converted to JPEG.

## Custom domain

`michellelee.com` is registered to someone else (since 1998). To use a domain
you own: buy it, add a `CNAME` file containing the domain, then point DNS
(A records to GitHub Pages IPs, or CNAME to michellelee337-collab.github.io).
