#!/usr/bin/env python3
"""src/*.html の {{head}} {{header}} {{footer}} を partials/ で置き換えて public/ に出力する。"""
import pathlib, shutil
R = pathlib.Path(__file__).parent
P = R / "public"
if P.exists(): shutil.rmtree(P)
P.mkdir()
parts = {k: (R / "partials" / f"{k}.html").read_text() for k in ("head", "header", "footer")}
for f in sorted((R / "src").glob("*.html")):
    s = f.read_text()
    for k, v in parts.items(): s = s.replace("{{" + k + "}}", v)
    (P / f.name).write_text(s)
for x in ("style.css", "site.js", "CNAME"):
    if (R / x).exists(): shutil.copy(R / x, P / x)
for d in ("img", "video"):
    if (R / d).exists(): shutil.copytree(R / d, P / d)
(P / ".nojekyll").write_text("")
print("built:", ", ".join(p.name for p in sorted(P.glob("*.html"))))
