[app]
title = Super AI Automation
package.name = superai
package.domain = org.shubham
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# Sabse important permissions[span_1](start_span)[span_1](end_span)
android.permissions = INTERNET, REQUEST_INSTALL_PACKAGES, BIND_ACCESSIBILITY_SERVICE, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

requirements = python3,kivy,requests

orientation = portrait
fullscreen = 0
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True

# Accessibility Service Configuration (Future use ke liye)[span_2](start_span)[span_2](end_span)
# android.services = MyAIService:service.py
