import hashlib
import os
import shutil

BOT = os.environ.get("MAKEFUN_BOT_DIR", "/bot")
OUT = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
src = os.path.join(BOT, "entry.png")
dst = os.path.join(OUT, "entry.png")

os.makedirs(OUT, exist_ok=True)
shutil.copyfile(src, dst)

with open(dst, "rb") as f:
    data = f.read()

if data[:8] != b"\x89PNG\r\n\x1a\n":
    raise SystemExit("entry.png is not a PNG")
if len(data) > 1048576:
    raise SystemExit("entry.png is over 1 MiB")

print("wrote", dst, len(data), "bytes", hashlib.sha256(data).hexdigest()[:16])
