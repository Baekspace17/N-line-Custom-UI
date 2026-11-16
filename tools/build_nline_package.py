#!/usr/bin/env python3
from pathlib import Path
import shutil,zipfile
root=Path(__file__).resolve().parents[1]
apk=root/'app/build/outputs/apk/debug/app-debug.apk'
if not apk.exists(): raise SystemExit('Build :app:assembleDebug first')
stage=root/'build/nline-package'
if stage.exists():shutil.rmtree(stage)
shutil.copytree(root/'nemesis-package',stage)
(stage/'app').mkdir()
shutil.copy2(apk,stage/'app/NLineCustomUI.apk')
dist=root/'dist';dist.mkdir(exist_ok=True)
with zipfile.ZipFile(dist/'nlinecustomui.zip','w',zipfile.ZIP_DEFLATED) as z:
 for p in sorted(stage.rglob('*')):
  if p.is_file():z.write(p,p.relative_to(stage))
print(dist/'nlinecustomui.zip')
