#!/bin/bash

# WaveLive Documents Converter
# This script converts HTML files to PDF and Word formats

echo "🚀 بدء تحويل ملفات WaveLive..."

# Check if required tools are installed
check_tool() {
    if ! command -v $1 &> /dev/null; then
        echo "❌ $1 غير مثبت. يرجى تثبيته أولاً."
        echo "لتثبيت $1:"
        if [[ "$1" == "wkhtmltopdf" ]]; then
            echo "  macOS: brew install wkhtmltopdf"
            echo "  Ubuntu: sudo apt-get install wkhtmltopdf"
        elif [[ "$1" == "pandoc" ]]; then
            echo "  macOS: brew install pandoc"
            echo "  Ubuntu: sudo apt-get install pandoc"
        fi
        return 1
    fi
    return 0
}

# Create output directories
mkdir -p pdf
mkdir -p word

echo "📁 إنشاء المجلدات..."

# Convert to PDF using wkhtmltopdf
if check_tool "wkhtmltopdf"; then
    echo "📄 تحويل الملفات إلى PDF..."
    
    # Agent Guide - Arabic
    wkhtmltopdf --page-size A4 --margin-top 0.75in --margin-right 0.75in --margin-bottom 0.75in --margin-left 0.75in --encoding UTF-8 agent-guide-ar.html pdf/agent-guide-ar.pdf
    echo "✅ تم تحويل دليل الوكيل (عربي) إلى PDF"
    
    # Agent Guide - English
    wkhtmltopdf --page-size A4 --margin-top 0.75in --margin-right 0.75in --margin-bottom 0.75in --margin-left 0.75in --encoding UTF-8 agent-guide-en.html pdf/agent-guide-en.pdf
    echo "✅ تم تحويل دليل الوكيل (إنجليزي) إلى PDF"
    
    # Agent Policy - Arabic
    wkhtmltopdf --page-size A4 --margin-top 0.75in --margin-right 0.75in --margin-bottom 0.75in --margin-left 0.75in --encoding UTF-8 agent-policy-ar.html pdf/agent-policy-ar.pdf
    echo "✅ تم تحويل سياسة الوكلاء (عربي) إلى PDF"
    
    # Agent Policy - English
    wkhtmltopdf --page-size A4 --margin-top 0.75in --margin-right 0.75in --margin-bottom 0.75in --margin-left 0.75in --encoding UTF-8 agent-policy-en.html pdf/agent-policy-en.pdf
    echo "✅ تم تحويل سياسة الوكلاء (إنجليزي) إلى PDF"
else
    echo "⚠️  تخطي تحويل PDF - wkhtmltopdf غير متوفر"
fi

# Convert to Word using pandoc
if check_tool "pandoc"; then
    echo "📝 تحويل الملفات إلى Word..."
    
    # Agent Guide - Arabic
    pandoc agent-guide-ar.html -o word/agent-guide-ar.docx --from html --to docx
    echo "✅ تم تحويل دليل الوكيل (عربي) إلى Word"
    
    # Agent Guide - English
    pandoc agent-guide-en.html -o word/agent-guide-en.docx --from html --to docx
    echo "✅ تم تحويل دليل الوكيل (إنجليزي) إلى Word"
    
    # Agent Policy - Arabic
    pandoc agent-policy-ar.html -o word/agent-policy-ar.docx --from html --to docx
    echo "✅ تم تحويل سياسة الوكلاء (عربي) إلى Word"
    
    # Agent Policy - English
    pandoc agent-policy-en.html -o word/agent-policy-en.docx --from html --to docx
    echo "✅ تم تحويل سياسة الوكلاء (إنجليزي) إلى Word"
else
    echo "⚠️  تخطي تحويل Word - pandoc غير متوفر"
fi

echo ""
echo "🎉 اكتمل التحويل!"
echo ""
echo "📋 الملفات المتوفرة:"
echo "├── 🌐 HTML Files:"
echo "│   ├── agent-guide-ar.html"
echo "│   ├── agent-guide-en.html"
echo "│   ├── agent-policy-ar.html"
echo "│   └── agent-policy-en.html"
echo "├── 📄 PDF Files (في مجلد pdf/):"
if [ -d "pdf" ] && [ "$(ls -A pdf/)" ]; then
    ls pdf/ | sed 's/^/│   ├── /'
fi
echo "└── 📝 Word Files (في مجلد word/):"
if [ -d "word" ] && [ "$(ls -A word/)" ]; then
    ls word/ | sed 's/^/    ├── /'
fi
echo ""
echo "💡 لفتح الموقع محلياً:"
echo "   python3 -m http.server 8000"
echo "   ثم افتح: http://localhost:8000"
echo ""
echo "📧 للدعم: support@wave-live.com"
