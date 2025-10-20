#!/usr/bin/env python3
"""
إنشاء ملفات PDF من ملفات HTML باستخدام weasyprint
"""

import os
import sys
from pathlib import Path

def install_weasyprint():
    """تثبيت weasyprint إذا لم يكن مثبتاً"""
    try:
        import weasyprint
        return True
    except ImportError:
        print("📦 تثبيت weasyprint...")
        os.system("pip3 install weasyprint")
        try:
            import weasyprint
            return True
        except ImportError:
            print("❌ فشل في تثبيت weasyprint")
            return False

def html_to_pdf(html_file, pdf_file):
    """تحويل ملف HTML إلى PDF"""
    try:
        import weasyprint
        
        # قراءة ملف HTML
        with open(html_file, 'r', encoding='utf-8') as f:
            html_content = f.read()
        
        # إنشاء PDF
        html_doc = weasyprint.HTML(string=html_content, base_url='.')
        html_doc.write_pdf(pdf_file)
        
        print(f"✅ تم إنشاء: {pdf_file}")
        return True
    except Exception as e:
        print(f"❌ خطأ في إنشاء {pdf_file}: {e}")
        return False

def main():
    """الدالة الرئيسية"""
    print("🚀 بدء إنشاء ملفات PDF...")
    
    # التأكد من تثبيت weasyprint
    if not install_weasyprint():
        print("❌ لا يمكن المتابعة بدون weasyprint")
        return
    
    # إنشاء مجلد PDF
    pdf_dir = Path("pdf")
    pdf_dir.mkdir(exist_ok=True)
    
    # قائمة الملفات للتحويل
    files_to_convert = [
        ("agent-guide-ar.html", "pdf/agent-guide-ar.pdf"),
        ("agent-guide-en.html", "pdf/agent-guide-en.pdf"),
        ("agent-policy-ar.html", "pdf/agent-policy-ar.pdf"),
        ("agent-policy-en.html", "pdf/agent-policy-en.pdf"),
    ]
    
    # تحويل الملفات
    success_count = 0
    for html_file, pdf_file in files_to_convert:
        if os.path.exists(html_file):
            if html_to_pdf(html_file, pdf_file):
                success_count += 1
        else:
            print(f"⚠️  الملف غير موجود: {html_file}")
    
    # إنشاء روابط مباشرة في المجلد الرئيسي
    print("\n📋 إنشاء روابط مباشرة...")
    
    # نسخ الملفات للمجلد الرئيسي بأسماء مبسطة
    import shutil
    
    links = [
        ("pdf/agent-guide-ar.pdf", "agent-guide.pdf"),
        ("pdf/agent-policy-ar.pdf", "privacy-policy.pdf"),
        ("pdf/agent-guide-en.pdf", "agent-guide-en.pdf"),
        ("pdf/agent-policy-en.pdf", "agent-policy-en.pdf"),
    ]
    
    for src, dst in links:
        if os.path.exists(src):
            shutil.copy2(src, dst)
            print(f"✅ تم إنشاء: {dst}")
    
    print(f"\n🎉 تم إنشاء {success_count} ملف PDF بنجاح!")
    print("\n📋 الملفات المتوفرة:")
    print("├── agent-guide.pdf (عربي)")
    print("├── privacy-policy.pdf (سياسة الوكلاء عربي)")
    print("├── agent-guide-en.pdf (إنجليزي)")
    print("└── agent-policy-en.pdf (سياسة الوكلاء إنجليزي)")

if __name__ == "__main__":
    main()
