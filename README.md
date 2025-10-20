# 🌊 WaveLive Agents Website

**Professional bilingual website for WaveLive agent registration and management**

A complete, modern, and responsive website inspired by Poppo Live Agents, customized for WaveLive brand with comprehensive documentation system.

## 🚀 Project Overview

WaveLive Agents is a comprehensive platform that provides:
- **Bilingual Support** (Arabic & English)
- **Agent Registration System**
- **Host Policy Management** 
- **Complete Documentation Suite**
- **Professional Brand Identity**

## 📁 Project Structure

```
wave-live/
├── 🌐 Main Website
│   ├── index.html              # Arabic homepage
│   ├── index-en.html           # English homepage
│   ├── styles.css              # Custom styling
│   ├── script.js               # Interactive features
│   ├── 404.html                # Custom error page
│   └── .htaccess               # Server configuration
│
├── 🎨 Brand Assets
│   └── assets/
│       ├── wavelive-logo.svg   # Main logo (200×60)
│       └── wavelive-icon.svg   # Icon version (48×48)
│
├── 📄 Documentation (HTML)
│   ├── agent-guide-ar.html     # Agent guide (Arabic)
│   ├── agent-guide-en.html     # Agent guide (English)
│   ├── agent-policy-ar.html    # Agent policy (Arabic)
│   ├── agent-policy-en.html    # Agent policy (English)
│   ├── host-policy-ar.html     # Host policy (Arabic)
│   └── host-policy-en.html     # Host policy (English)
│
├── 📄 PDF Documents
│   ├── agent-guide.pdf         # Agent guide
│   ├── agent-guide-ar.pdf      # Agent guide (Arabic)
│   ├── privacy-policy.pdf      # Privacy policy
│   ├── agent-policy-ar.pdf     # Agent policy (Arabic)
│   ├── host-policy-ar.pdf      # Host policy (Arabic)
│   └── host-policy-en.pdf      # Host policy (English)
│
├── 📝 Word Documents
│   ├── agent-guide.docx        # Agent guide
│   ├── agent-guide-ar.docx     # Agent guide (Arabic)
│   ├── agent-guide-en.docx     # Agent guide (English)
│   ├── privacy-policy.docx     # Privacy policy
│   ├── agent-policy-ar.docx    # Agent policy (Arabic)
│   ├── agent-policy-en.docx    # Agent policy (English)
│   ├── host-policy-ar.docx     # Host policy (Arabic)
│   └── host-policy-en.docx     # Host policy (English)
│
└── 📂 Organized Documents
    ├── documents/
    │   ├── pdf/                # All PDF files
    │   ├── word/               # All Word files
    │   └── host-policy/        # Host policy specific files
    │       ├── pdf/
    │       └── word/
    │
    └── 📋 Project Documentation
        ├── README.md           # This file
        ├── DEPLOYMENT_GUIDE.md # Deployment instructions
        ├── FINAL_STATUS.md     # Project completion status
        ├── HOST_POLICY_SUMMARY.md # Host policy details
        └── LOGO_UPDATE_SUMMARY.md # Logo implementation details
```

## ✨ Features

### 🌐 Website Features
- **Bilingual Support** - Complete Arabic & English versions
- **Responsive Design** - Works on all devices
- **Interactive Elements** - Commission calculator, animations
- **Language Switching** - Seamless language toggle
- **Modern UI/UX** - Professional design with Tailwind CSS
- **SEO Optimized** - Meta tags and structured data
- **Performance Optimized** - Fast loading and compressed assets

### 📋 Documentation System
- **3 Document Types**: Agent Guide, Agent Policy, Host Policy
- **2 Languages**: Arabic and English for each document
- **3 Formats**: HTML, PDF, and Word for maximum compatibility
- **Professional Layout** - Print-ready with proper formatting
- **Comprehensive Content** - Detailed policies and procedures

### 🎨 Brand Identity
- **Custom Logo** - Professional SVG logo with animations
- **Consistent Branding** - Unified color scheme and typography
- **Modern Design** - Gradient backgrounds and smooth transitions
- **Animated Elements** - Live indicator and interactive components

## 🛠️ Technology Stack

### Frontend
- **HTML5** - Semantic markup
- **CSS3** - Modern styling with Tailwind CSS
- **JavaScript ES6+** - Interactive features
- **SVG** - Scalable vector graphics for logos

### Build Tools
- **Pandoc** - Document conversion (HTML → Word)
- **Python** - PDF generation scripts
- **Node.js** - Development server (optional)

### Server Configuration
- **Apache** - .htaccess configuration
- **PHP** - Not required (static site)
- **SSL** - HTTPS ready

## 🚀 Quick Start

### Local Development
```bash
# Clone the repository
git clone <repository-url>
cd wave-live

# Start local server (Python)
python3 -m http.server 8080

# Or using Node.js
npm start

# Or using serve
npx serve .
```

### Access Points
- **Arabic Site**: http://localhost:8080/
- **English Site**: http://localhost:8080/index-en.html
- **Documents**: http://localhost:8080/agent-guide.pdf

## 📦 Deployment

### cPanel Deployment
1. **Upload Files**: Upload `wave-live-website-with-logo.zip`
2. **Extract**: Unzip in `public_html` directory
3. **Permissions**: Set proper file permissions (644 for files, 755 for directories)
4. **Test**: Verify all links and documents work

### Requirements
- **Web Server**: Apache/Nginx
- **PHP**: Not required
- **Database**: Not required
- **SSL**: Recommended

## 📊 Project Statistics

| Category | Count | Size | Languages |
|----------|-------|------|-----------|
| **HTML Files** | 12 files | ~240 KB | Arabic + English |
| **PDF Files** | 16 files | ~96 KB | Arabic + English |
| **Word Files** | 16 files | ~240 KB | Arabic + English |
| **Assets** | 6 files | ~15 KB | SVG + CSS + JS |
| **Total** | **50 files** | **~591 KB** | **Bilingual** |

## 🎯 Document Types

### 1. Agent Guide
- **Purpose**: Complete registration guide for agents
- **Content**: Step-by-step registration, commission system, requirements
- **Formats**: HTML, PDF, Word
- **Languages**: Arabic, English

### 2. Agent Policy
- **Purpose**: Terms and conditions for agents
- **Content**: Rights, obligations, commission structure, penalties
- **Formats**: HTML, PDF, Word
- **Languages**: Arabic, English

### 3. Host Policy
- **Purpose**: Terms and conditions for hosts/streamers
- **Content**: Registration requirements, content standards, earnings system
- **Formats**: HTML, PDF, Word
- **Languages**: Arabic, English

## 🌟 Key Highlights

### Commission System
- **Level D**: 4% (0 points)
- **Level C**: 8% (2M points)
- **Level B**: 12% (10M points)
- **Level A**: 16% (50M points)
- **Level S**: 20% (150M points)

### Host Earnings
- **New Hosts**: 50% share
- **Distinguished Hosts**: 60% share
- **Star Hosts**: 70% share

### Activity Requirements
- **Option 1**: Maintain 5+ active hosts
- **Option 2**: Invite 5+ new agencies
- **Option 3**: Regular coin selling activity

## 🔧 Customization

### Colors
```css
:root {
  --primary: #8b5cf6;    /* Purple */
  --secondary: #667eea;  /* Blue */
  --accent: #f093fb;     /* Pink */
  --success: #10b981;    /* Green */
  --warning: #f59e0b;    /* Orange */
  --danger: #ef4444;     /* Red */
}
```

### Logo Usage
```html
<!-- Main Logo -->
<img src="assets/wavelive-logo.svg" alt="WaveLive" class="h-8 w-auto">

<!-- Icon Version -->
<img src="assets/wavelive-icon.svg" alt="WaveLive" class="h-6 w-6">
```

## 📞 Support & Contact

- **Website**: wave-live.com
- **Support Email**: support@wave-live.com
- **Agent Support**: agents@wave-live.com
- **Host Support**: hosts@wave-live.com
- **Legal Inquiries**: legal@wave-live.com

## 📄 License

© 2025 WaveLive. All rights reserved.

This project contains proprietary and confidential information. Unauthorized reproduction or distribution is prohibited.

## 🏆 Project Completion

**Status**: ✅ **COMPLETED**
- **Start Date**: October 20, 2025
- **Completion Date**: October 20, 2025
- **Total Development Time**: ~6 hours
- **Files Created**: 50+ files
- **Languages Supported**: 2 (Arabic, English)
- **Document Formats**: 3 (HTML, PDF, Word)

---

**Built with ❤️ by Jarvis AI Assistant**

## كيفية تحويل الملفات إلى PDF و Word

### تحويل إلى PDF

#### الطريقة الأولى: باستخدام المتصفح
1. افتح الملف HTML في المتصفح
2. اضغط Ctrl+P (أو Cmd+P على Mac)
3. اختر "Save as PDF"
4. احفظ الملف

#### الطريقة الثانية: باستخدام wkhtmltopdf
```bash
# تثبيت wkhtmltopdf
brew install wkhtmltopdf  # على Mac
sudo apt-get install wkhtmltopdf  # على Ubuntu

# تحويل الملفات
wkhtmltopdf agent-guide-ar.html agent-guide-ar.pdf
wkhtmltopdf agent-guide-en.html agent-guide-en.pdf
wkhtmltopdf agent-policy-ar.html agent-policy-ar.pdf
wkhtmltopdf agent-policy-en.html agent-policy-en.pdf
```

### تحويل إلى Word

#### الطريقة الأولى: باستخدام Pandoc
```bash
# تثبيت Pandoc
brew install pandoc  # على Mac
sudo apt-get install pandoc  # على Ubuntu

# تحويل الملفات
pandoc agent-guide-ar.html -o agent-guide-ar.docx
pandoc agent-guide-en.html -o agent-guide-en.docx
pandoc agent-policy-ar.html -o agent-policy-ar.docx
pandoc agent-policy-en.html -o agent-policy-en.docx
```

#### الطريقة الثانية: باستخدام Microsoft Word
1. افتح Microsoft Word
2. File > Open > اختر الملف HTML
3. File > Save As > اختر تنسيق Word Document (.docx)

## تشغيل الموقع محلياً

### خيار 1: خادم Python البسيط
```bash
cd /Users/macbookair/Downloads/wave-live
python3 -m http.server 8000
# افتح http://localhost:8000 في المتصفح
```

### خيار 2: خادم Node.js
```bash
npx serve .
```

### خيار 3: فتح مباشر
افتح ملف `index.html` مباشرة في المتصفح

## الميزات المتوفرة

### الموقع الرئيسي
- ✅ **دعم لغتين كامل** (عربي وإنجليزي)
- ✅ **تبديل اللغات** مع حفظ التفضيل
- ✅ تصميم متجاوب (Responsive Design)
- ✅ دعم اللغة العربية مع RTL
- ✅ نظام العمولات التفاعلي
- ✅ **حاسبة العمولة** التفاعلية
- ✅ جدول المحتويات
- ✅ قسم الأسئلة الشائعة
- ✅ تصميم حديث باستخدام Tailwind CSS
- ✅ لوغو WaveLive مدمج
- ✅ **رسوم متحركة** وتأثيرات بصرية
- ✅ **زر العودة للأعلى**
- ✅ **كشف اللغة التلقائي**

### الوثائق
- ✅ تصميم احترافي للطباعة
- ✅ دعم كامل للغتين العربية والإنجليزية
- ✅ تنسيق قانوني مناسب للسياسات
- ✅ أرقام المواد والأقسام
- ✅ صناديق تحذير وملاحظات ملونة

## التخصيص

### تغيير الألوان
في ملف `styles.css`، يمكنك تعديل المتغيرات التالية:
```css
/* الألوان الرئيسية */
--primary-color: #8B5CF6;
--secondary-color: #A855F7;
--accent-color: #7C3AED;
```

### تغيير المحتوى
- عدّل النصوص في ملفات HTML
- استبدل الروابط بروابط موقع WaveLive الفعلية
- أضف معرف الدعوة الخاص بك

### إضافة صور
1. ضع الصور في مجلد `images/`
2. أضف المراجع في ملفات HTML:
```html
<img src="images/logo.png" alt="WaveLive Logo">
```

## الروابط المطلوب تحديثها

في الملفات، استبدل الروابط التالية بروابط WaveLive الفعلية:
- `https://wave-live.com` - الموقع الرئيسي
- `https://wave-live.com/wave/admincp/login.php` - لوحة الوكلاء
- `support@wave-live.com` - بريد الدعم
- `agents@wave-live.com` - بريد دعم الوكلاء

## الدعم الفني

للحصول على المساعدة في التخصيص أو التطوير:
- راجع التوثيق في ملفات HTML
- تحقق من التعليقات في ملف CSS
- استخدم أدوات المطور في المتصفح للتصحيح

## الترخيص

هذا المشروع مخصص لاستخدام WaveLive ويحتوي على تصميم مستوحى من Poppo Live Agents مع التخصيص الكامل للعلامة التجارية.

---

**ملاحظة:** تأكد من تحديث جميع الروابط والمعلومات لتتطابق مع بيانات WaveLive الفعلية قبل النشر.
