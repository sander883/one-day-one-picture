import os
import shutil

BOT = os.environ.get("MAKEFUN_BOT_DIR", "/bot")
OUT = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
src = os.path.join(BOT, "entry.png")
dst = os.path.join(OUT, "entry.png")

shutil.copyfile(src, dst)
print("wrote", dst, os.path.getsize(dst), "bytes")
