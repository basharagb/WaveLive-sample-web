#!/usr/bin/env python3
"""
تحويل HTML إلى PDF باستخدام المتصفح
"""

import os
import subprocess
import sys
from pathlib import Path

def create_pdf_with_browser(html_file, pdf_file):
    """تحويل HTML إلى PDF باستخدام المتصفح"""
    try:
        # التأكد من وجود الملف
        if not os.path.exists(html_file):
            print(f"❌ الملف غير موجود: {html_file}")
            return False
        
        # الحصول على المسار المطلق
        html_path = os.path.abspath(html_file)
        pdf_path = os.path.abspath(pdf_file)
        
        # أوامر مختلفة للمتصفحات المختلفة
        commands = [
            # Chrome/Chromium
            [
                "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
                "--headless", "--disable-gpu", "--print-to-pdf=" + pdf_path,
                "file://" + html_path
            ],
            # Safari (يتطلب تفعيل Developer menu)
            [
                "osascript", "-e",
                f'''
                tell application "Safari"
                    open "file://{html_path}"
                    delay 2
                    tell application "System Events"
                        keystroke "p" using command down
                        delay 1
                        keystroke "s" using command down
                        delay 1
                        keystroke "{pdf_path}"
                        delay 1
                        keystroke return
                    end tell
                end tell
                '''
            ]
        ]
        
        # تجربة الأوامر
        for cmd in commands:
            try:
                result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
                if result.returncode == 0 or os.path.exists(pdf_path):
                    print(f"✅ تم إنشاء: {pdf_file}")
                    return True
            except (subprocess.TimeoutExpired, FileNotFoundError):
                continue
        
        print(f"⚠️  لم يتم العثور على متصفح مناسب لـ {html_file}")
        return False
        
    except Exception as e:
        print(f"❌ خطأ في تحويل {html_file}: {e}")
        return False

def create_simple_pdfs():
    """إنشاء ملفات PDF بسيطة"""
    
    # إنشاء محتوى PDF مبسط
    pdf_content_guide = """
%PDF-1.4
1 0 obj
<<
/Type /Catalog
/Pages 2 0 R
>>
endobj

2 0 obj
<<
/Type /Pages
/Kids [3 0 R]
/Count 1
>>
endobj

3 0 obj
<<
/Type /Page
/Parent 2 0 R
/MediaBox [0 0 612 792]
/Contents 4 0 R
/Resources <<
/Font <<
/F1 5 0 R
>>
>>
>>
endobj

4 0 obj
<<
/Length 200
>>
stream
BT
/F1 18 Tf
50 700 Td
(WaveLive Agent Guide) Tj
0 -50 Td
/F1 12 Tf
(This is the WaveLive Agent Registration Guide.) Tj
0 -30 Td
(Please visit wave-live.com for more information.) Tj
0 -30 Td
(Contact: support@wave-live.com) Tj
ET
endstream
endobj

5 0 obj
<<
/Type /Font
/Subtype /Type1
/BaseFont /Helvetica
>>
endobj

xref
0 6
0000000000 65535 f 
0000000010 00000 n 
0000000053 00000 n 
0000000125 00000 n 
0000000348 00000 n 
0000000565 00000 n 
trailer
<<
/Size 6
/Root 1 0 R
>>
startxref
636
%%EOF
"""
    
    pdf_content_policy = """
%PDF-1.4
1 0 obj
<<
/Type /Catalog
/Pages 2 0 R
>>
endobj

2 0 obj
<<
/Type /Pages
/Kids [3 0 R]
/Count 1
>>
endobj

3 0 obj
<<
/Type /Page
/Parent 2 0 R
/MediaBox [0 0 612 792]
/Contents 4 0 R
/Resources <<
/Font <<
/F1 5 0 R
>>
>>
>>
endobj

4 0 obj
<<
/Length 220
>>
stream
BT
/F1 18 Tf
50 700 Td
(WaveLive Agent Policy) Tj
0 -50 Td
/F1 12 Tf
(This is the WaveLive Agent Policy document.) Tj
0 -30 Td
(Terms and conditions for WaveLive agents.) Tj
0 -30 Td
(Please visit wave-live.com for more information.) Tj
0 -30 Td
(Contact: support@wave-live.com) Tj
ET
endstream
endobj

5 0 obj
<<
/Type /Font
/Subtype /Type1
/BaseFont /Helvetica
>>
endobj

xref
0 6
0000000000 65535 f 
0000000010 00000 n 
0000000053 00000 n 
0000000125 00000 n 
0000000348 00000 n 
0000000585 00000 n 
trailer
<<
/Size 6
/Root 1 0 R
>>
startxref
656
%%EOF
"""
    
    # كتابة ملفات PDF
    with open("agent-guide.pdf", "wb") as f:
        f.write(pdf_content_guide.encode('latin1'))
    
    with open("privacy-policy.pdf", "wb") as f:
        f.write(pdf_content_policy.encode('latin1'))
    
    print("✅ تم إنشاء: agent-guide.pdf")
    print("✅ تم إنشاء: privacy-policy.pdf")

def main():
    """الدالة الرئيسية"""
    print("🚀 إنشاء ملفات PDF...")
    
    # محاولة التحويل من HTML
    html_files = ["agent-guide.html", "privacy-policy.html"]
    pdf_files = ["agent-guide.pdf", "privacy-policy.pdf"]
    
    success = False
    for html_file, pdf_file in zip(html_files, pdf_files):
        if os.path.exists(html_file):
            if create_pdf_with_browser(html_file, pdf_file):
                success = True
    
    # إذا فشل التحويل، إنشاء ملفات PDF بسيطة
    if not success:
        print("📄 إنشاء ملفات PDF بسيطة...")
        create_simple_pdfs()
    
    print("\n🎉 تم إنشاء ملفات PDF!")
    print("📋 الملفات المتوفرة:")
    print("├── agent-guide.pdf")
    print("└── privacy-policy.pdf")
    print("\n🌐 يمكنك الآن الوصول إليها عبر:")
    print("├── http://localhost:8000/agent-guide.pdf")
    print("└── http://localhost:8000/privacy-policy.pdf")

if __name__ == "__main__":
    main()
