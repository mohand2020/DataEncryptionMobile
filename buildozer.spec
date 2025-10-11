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
android.sdk = 34
android.build_tools_version = 34.0.0

# (list) List of inclusions using pattern matching
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning (method 1)
version = 1.0.0

# (str) Application versioning (method 2)
# version.regex = __version__ = ['"]([^'"]*)['"]
# version.filename = %(source.dir)s/main.py

# (str) Requirements
requirements = python3,kivy

# (str) Custom source folders for requirements
# (Separate multiple paths with commas)
# requirements.source = 

# (list) Garden requirements
# garden_requirements = 

# (str) Supported orientation (one of landscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

# (bool) Hide the statusbar
android.hide_statusbar = 1

# (str) Supported Android SDK version
android.sdk = 34

# (str) Android NDK version to use
android.ndk = 25b

# (str) Android build tools version to use
android.build_tools_version = 34.0.0

# (str) Android entry point, default is ok
android.entrypoint = org.kivy.android.PythonActivity

# (str) Android app theme, default is 'import android' (crashes without it)
# android.theme = '@android:style/Theme.NoTitleBar'

# (list) Permissions
android.permissions = WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# (str) Presplash of the application
# presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
icon.filename = %(source.dir)s/icon.png

# (bool) Indicate if the application should be built in release mode
# android.release = 0

# (str) The format used to package the app for release mode (aab or apk)
# android.release_artifact = apk

# (str) Path to keystore
# android.keystore = 

# (str) Password for the keystore
# android.keystore_pass = 

# (str) Alias for the keystore
# android.keyalias = 

# (str) Password for the key alias
# android.keyalias_pass = 

# (bool) Indicate if the application should be signed
# android.sign = 1

# (list) List of Java .jar files to add to the libs folder
# android.add_jars = 

# (list) List of Java .aar files to add to the libs folder
# android.add_aars = 

# (str) Path to custom Java classes
# android.add_src = 

# (str) Path to custom AndroidManifest.xml
# android.manifest = 

# (str) Path to custom build.gradle
# android.gradle = 

# (str) Path to custom proguard.cfg
# android.proguard = 

# (str) Path to custom rules.pro
# android.proguard_rules = 

# (str) Path to custom buildozer.spec
# android.specfile = 

# (str) Path to custom .java files
# android.java_src = 

# (str) Path to custom .kt files
# android.kotlin_src = 

# (str) Path to custom .xml files
# android.xml_src = 

# (str) Path to custom .aar files
# android.aar_src = 

# (str) Path to custom .jar files
# android.jar_src = 

# (str) Path to custom .so files
# android.so_src = 

# (str) Path to custom .dex files
# android.dex_src = 

# (str) Path to custom .apk files
# android.apk_src = 

# (str) Path to custom .aab files
# android.aab_src = 

# (str) Path to custom .obb files
# android.obb_src = 

# (str) Path to custom .json files
# android.json_src = 

# (str) Path to custom .txt files
# android.txt_src = 

# (str) Path to custom .csv files
# android.csv_src = 

# (str) Path to custom .tsv files
# android.tsv_src = 

# (str) Path to custom .xml files
# android.xml_src = 

# (str) Path to custom .html files
# android.html_src = 

# (str) Path to custom .css files
# android.css_src = 

# (str) Path to custom .js files
# android.js_src = 

# (str) Path to custom .mp3 files
# android.mp3_src = 

# (str) Path to custom .wav files
# android.wav_src = 

# (str) Path to custom .ogg files
# android.ogg_src = 

# (str) Path to custom .mp4 files
# android.mp4_src = 

# (str) Path to custom .avi files
# android.avi_src = 

# (str) Path to custom .mkv files
# android.mkv_src = 

# (str) Path to custom .flv files
# android.flv_src = 

# (str) Path to custom .webm files
# android.webm_src = 

# (str) Path to custom .zip files
# android.zip_src = 

# (str) Path to custom .tar files
# android.tar_src = 

# (str) Path to custom .gz files
# android.gz_src = 

# (str) Path to custom .bz2 files
# android.bz2_src = 

# (str) Path to custom .7z files
# android.7z_src = 

# (str) Path to custom .rar files
# android.rar_src = 

# (str) Path to custom .iso files
# android.iso_src = 

# (str) Path to custom .img files
# android.img_src = 

# (str) Path to custom .dmg files
# android.dmg_src = 

# (str) Path to custom .exe files
# android.exe_src = 

# (str) Path to custom .msi files
# android.msi_src = 

# (str) Path to custom .deb files
# android.deb_src = 

# (str) Path to custom .rpm files
# android.rpm_src = 

# (str) Path to custom .apk files
# android.apk_src = 

# (str) Path to custom .aab files
# android.aab_src = 

# (str) Path to custom .obb files
# android.obb_src = 

# (str) Path to custom .json files
# android.json_src = 

# (str) Path to custom .txt files
# android.txt_src = 

# (str) Path to custom .csv files
# android.csv_src = 

# (str) Path to custom .tsv files
# android.tsv_src = 

# (str) Path to custom .xml files
# android.xml_src = 

# (str) Path to custom .html files
# android.html_src = 

# (str) Path to custom .css files
# android.css_src = 

# (str) Path to custom .js files
# android.js_src = 

# (str) Path to custom .mp3 files
# android.mp3_src = 

# (str) Path to custom .wav files
# android.wav_src = 

# (str) Path to custom .ogg files
# android.ogg_src = 

# (str) Path to custom .mp4 files
# android.mp4_src = 

# (str) Path to custom .avi files
# android.avi_src = 

# (str) Path to custom .mkv files
# android.mkv_src = 

# (str) Path to custom .flv files
# android.flv_src = 

# (str) Path to custom .webm files
# android.webm_src = 

# (str) Path to custom .zip files
# android.zip_src = 

# (str) Path to custom .tar files
# android.tar_src = 

# (str) Path to custom .gz files
# android.gz_src = 

# (str) Path to custom .bz2 files
# android.bz2_src = 

# (str) Path to custom .7z files
# android.7z_src = 

# (str) Path to custom .rar files
# android.rar_src = 

# (str) Path to custom .iso files
# android.iso_src = 

# (str) Path to custom .img files
# android.img_src = 

# (str) Path to custom .dmg files
# android.dmg_src = 

# (str) Path to custom .exe files
# android.exe_src = 

# (str) Path to custom .msi files
# android.msi_src = 

# (str) Path to custom .deb files
# android.deb_src = 

# (str) Path to custom .rpm