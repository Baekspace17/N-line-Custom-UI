# N-line Custom UI

Android 4.4 (Gen5W / NEMESIS) custom tile application derived from **KramerTech/gen5-Tilepad**.

## Source and copyright
Original project: https://github.com/KramerTech/gen5-Tilepad
Original authors and contributors: KramerTech/gen5-Tilepad project contributors.
Original license: **GNU General Public License v3.0**. See the included `LICENSE`. This project modifies the original code for personal use. The license remains applicable to derivative code.

## Names and install isolation
- Android package / namespace: `com.baekspace.nline`
- Tweaks app: excluded (not built or installed)
- NEMESIS ID: `nlinecustomui`
- App path: `/data/nemesis/apps/nlinecustomui`
- System APK: `/system/app/NLineCustomUI.apk`
- Tilepad's own APK and package ID are not replaced.

## Features
- Original-source Wi-Fi Client UI, initial client provisioning shell code, and network status.
- Original-source optional ADB over TCP controls. Keep ADB disabled when not needed.
- Tile-based main UI and future custom feature extension.
- EV preconditioning and tweaks tiles are hidden; shared source classes remain for compilation.

## Build and upload
Upload the **contents** of this ZIP into a clean GitHub repository root. Remove older files before upload, since GitHub does not delete absent files.
Run GitHub Actions → `N-line Build`. The workflow compiles the debug APK and creates `dist/nlinecustomui.zip`.

## Caution
This is a source-level namespace and path migration. The Android build and vehicle execution have not been verified here. Do not run uninstall hooks of either application while both coexist: Wi-Fi provisioning may have shared system-level state.
