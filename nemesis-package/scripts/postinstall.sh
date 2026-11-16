#!/system/bin/sh
. /data/nemesis/apps/nlinecustomui/scripts/common.sh
[ -s "$DEX" ] || { log "missing app APK"; exit 1; }
# Independent app; never touch /system/app/NLineCustomUI.apk.
NEW=/system/app/NLineCustomUI.apk.nline-new
system_rw || { log "cannot remount system"; exit 1; }
cat "$DEX" > "$NEW" && chmod 0644 "$NEW" && chown 0:0 "$NEW" && same_file "$DEX" "$NEW" && mv "$NEW" "$SYSAPK"
RESULT=$?
[ "$RESULT" = 0 ] || rm -f "$NEW"
sync
system_restore
[ "$RESULT" = 0 ] || { log "APK install failed"; exit 1; }
log "installed NLineCustomUI; reboot to register APK"
exit 0
