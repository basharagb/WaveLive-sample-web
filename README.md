# WaveLive Agents Website

موقع وكلاء WaveLive - نسخة مطابقة لموقع Poppo Live Agents مع تخصيص العلامة التجارية لـ WaveLive

## الملفات المتوفرة

### الموقع الرئيسي
- `index.html` - الصفحة الرئيسية للموقع (عربي)
- `index-en.html` - الصفحة الرئيسية للموقع (إنجليزي)
- `styles.css` - ملف التصميم المخصص
- `script.js` - ملف JavaScript للتفاعل وتبديل اللغات
- `404.html` - صفحة الخطأ 404 (ثنائية اللغة)
- `.htaccess` - تكوين الخادم وإعادة التوجيه

### الوثائق
#### دليل التسجيل كوكيل
- `agent-guide-ar.html` - النسخة العربية
- `agent-guide-en.html` - النسخة الإنجليزية

#### سياسة الوكلاء
- `agent-policy-ar.html` - النسخة العربية
- `agent-policy-en.html` - النسخة الإنجليزية

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
