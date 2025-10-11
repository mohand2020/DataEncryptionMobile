[app]

# (str) Title of your application
title = DataEncryptionMobile

# (str) Package name
package.name = dataencryptionmobile

# (str) Package domain (needed for android/ios packaging)
package.domain = org.mohand

# (str) Source code where the main.py live
source.dir = .

# (str) Main .py file to use as the main entry point
source.main = main.py

# (list) List of inclusions using pattern matching
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning
version = 1.0.0

# (str) Requirements
requirements = python3,kivy

# (list) Permissions
android.permissions = WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# (str) Supported orientation (one of landscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

# ✅ إصدار SDK و build-tools لتجنب مشاكل الرخص
android.sdk = 34
android.build_tools_version = 34.0.0
android.ndk = 25b

# (str) Android entry point
android.entrypoint = org.kivy.android.PythonActivity

# (bool) Hide the statusbar
android.hide_statusbar = 1

# (str) Icon of the application
icon.filename = %(source.dir)s/icon.png

# (str) Presplash of the application (اختياري)
# presplash.filename = %(source.dir)s/presplash.png

# (bool) Indicate if the application should be built in release mode
# android.release = 0

# (str) The format used to package the app for release mode (aab or apk)
# android.release_artifact = apk

# (str) Path to keystore (اختياري للتوقيع)
# android.keystore = 
# android.keystore_pass = 
# android.keyalias = 
# android.keyalias_pass = 
