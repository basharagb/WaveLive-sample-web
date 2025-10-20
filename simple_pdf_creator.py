#!/usr/bin/env python3
"""
إنشاء ملفات PDF بسيطة للوثائق المطلوبة
"""

import os
from datetime import datetime

def create_simple_pdf(filename, title, content):
    """إنشاء ملف PDF بسيط باستخدام HTML وطباعة المتصفح"""
    
    pdf_html = f"""
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <title>{title}</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@300;400;600;700&display=swap');
        
        body {{
            font-family: 'Cairo', Arial, sans-serif;
            line-height: 1.6;
            margin: 40px;
            color: #333;
            direction: rtl;
            text-align: right;
        }}
        
        .header {{
            text-align: center;
            border-bottom: 3px solid #8B5CF6;
            padding-bottom: 20px;
            margin-bottom: 30px;
        }}
        
        .logo {{
            font-size: 2em;
            font-weight: 700;
            color: #8B5CF6;
            margin-bottom: 10px;
        }}
        
        h1 {{
            color: #8B5CF6;
            font-size: 1.8em;
            margin-bottom: 10px;
        }}
        
        h2 {{
            color: #5B21B6;
            font-size: 1.3em;
            margin-top: 25px;
            margin-bottom: 15px;
            border-right: 4px solid #8B5CF6;
            padding-right: 15px;
        }}
        
        .content {{
            font-size: 14px;
            line-height: 1.8;
        }}
        
        .footer {{
            text-align: center;
            margin-top: 40px;
            padding-top: 20px;
            border-top: 2px solid #E2E8F0;
            color: #6B7280;
            font-size: 12px;
        }}
        
        @media print {{
            body {{ margin: 20px; }}
            .no-print {{ display: none; }}
        }}
    </style>
</head>
<body>
    <div class="header">
        <div class="logo">WaveLive</div>
        <h1>{title}</h1>
        <p>تاريخ الإصدار: {datetime.now().strftime('%Y-%m-%d')}</p>
    </div>
    
    <div class="content">
        {content}
    </div>
    
    <div class="footer">
        <p><strong>WaveLive Agents</strong> - {title}</p>
        <p>© 2025 WaveLive. جميع الحقوق محفوظة.</p>
        <p>للدعم والاستفسارات: support@wave-live.com</p>
    </div>
    
    <script>
        // Auto-print when opened
        window.onload = function() {{
            setTimeout(function() {{
                window.print();
            }}, 1000);
        }};
    </script>
</body>
</html>
"""
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(pdf_html)
    
    print(f"✅ تم إنشاء: {filename}")

def main():
    """إنشاء الملفات المطلوبة"""
    print("🚀 إنشاء ملفات PDF للطباعة...")
    
    # محتوى دليل الوكيل
    agent_guide_content = """
        <h2>مقدمة</h2>
        <p>مرحباً بك في عالم WaveLive! هذا الدليل سيساعدك على فهم كيفية التسجيل كوكيل في منصة WaveLive وبدء رحلتك في إدارة المضيفين وتحقيق الأرباح.</p>
        
        <h2>ما هو WaveLive؟</h2>
        <p>WaveLive هي منصة بث مباشر عالمية تجمع بين الوكالات والمضيفات للتواصل مع الجمهور في الوقت الفعلي. كوكيل، ستحصل على أدوات حصرية لتجنيد المضيفات وإدارة فريقك مع إمكانية كسب عمولة تصل إلى 20٪.</p>
        
        <h2>خطوات التسجيل</h2>
        <p><strong>1. تحميل التطبيق:</strong> قم بتحميل تطبيق WaveLive من متجر Google Play أو App Store.</p>
        <p><strong>2. إنشاء حساب:</strong> أنشئ حساب مستخدم جديد وأكمل إعداد ملفك الشخصي.</p>
        <p><strong>3. الحصول على المعرف:</strong> انسخ معرف WaveLive الخاص بك من ملفك الشخصي.</p>
        <p><strong>4. ملء النموذج:</strong> املأ نموذج تسجيل الوكيل بالمعلومات المطلوبة.</p>
        <p><strong>5. التحقق:</strong> احصل على رمز التحقق وأكمل عملية التسجيل.</p>
        
        <h2>نظام العمولات</h2>
        <p>يعتمد نظام العمولات على أداء فريقك خلال آخر 30 يوماً:</p>
        <p>• المستوى D (0 نقطة): 4% عمولة</p>
        <p>• المستوى C (2,000,000 نقطة): 8% عمولة</p>
        <p>• المستوى B (10,000,000 نقطة): 12% عمولة</p>
        <p>• المستوى A (50,000,000 نقطة): 16% عمولة</p>
        <p>• المستوى S (150,000,000 نقطة): 20% عمولة</p>
        
        <h2>مسؤوليات الوكيل</h2>
        <p>• تجنيد وإدارة المضيفين</p>
        <p>• تقديم الدعم والتدريب</p>
        <p>• مراقبة الأداء وتحسينه</p>
        <p>• الحفاظ على نشاط الوكالة</p>
        
        <h2>نصائح للنجاح</h2>
        <p>• ابنِ علاقات قوية مع مضيفيك</p>
        <p>• ركز على الجودة في اختيار المضيفين</p>
        <p>• قدم التدريب والدعم المستمر</p>
        <p>• راقب الأداء باستمرار</p>
        <p>• وسع شبكتك بدعوة وكلاء آخرين</p>
    """
    
    # محتوى سياسة الوكلاء
    privacy_policy_content = """
        <h2>المادة 1: التعريفات</h2>
        <p>في هذه السياسة، تحمل المصطلحات التالية المعاني المحددة:</p>
        <p>• <strong>المنصة:</strong> تطبيق وموقع WaveLive الإلكتروني</p>
        <p>• <strong>الوكيل:</strong> الشخص المسجل لإدارة المضيفين على المنصة</p>
        <p>• <strong>المضيف:</strong> الشخص الذي يقوم بالبث المباشر على المنصة</p>
        <p>• <strong>العمولة:</strong> النسبة المئوية من أرباح المضيفين التي يحصل عليها الوكيل</p>
        
        <h2>المادة 2: شروط التسجيل</h2>
        <p>للتسجيل كوكيل في WaveLive، يجب أن تستوفي الشروط التالية:</p>
        <p>• أن تكون بالغاً (18 سنة أو أكثر)</p>
        <p>• أن تمتلك حساباً نشطاً على منصة WaveLive</p>
        <p>• أن تقدم معلومات صحيحة ومحدثة</p>
        <p>• أن توافق على جميع شروط وأحكام المنصة</p>
        
        <h2>المادة 3: حقوق والتزامات الوكيل</h2>
        <p><strong>حقوق الوكيل:</strong></p>
        <p>• الحصول على عمولة وفقاً لنظام المستويات المحدد</p>
        <p>• الوصول إلى لوحة تحكم الوكيل</p>
        <p>• تجنيد وإدارة المضيفين</p>
        <p>• دعوة وكلاء فرعيين</p>
        
        <p><strong>التزامات الوكيل:</strong></p>
        <p>• الالتزام بجميع قوانين وأنظمة المنصة</p>
        <p>• تقديم الدعم والتوجيه للمضيفين</p>
        <p>• الحفاظ على سرية المعلومات</p>
        <p>• التصرف بمهنية وأخلاق عالية</p>
        
        <h2>المادة 4: شروط الحفاظ على النشاط</h2>
        <p>يجب على كل وكيل تحقيق أحد الشروط التالية كل 30 يوماً:</p>
        <p>• الحفاظ على 5 مضيفين نشطين على الأقل</p>
        <p>• دعوة 5 وكالات جديدة نشطة</p>
        <p>• بيع العملات بانتظام (للوكلاء المسجلين كبائعي عملات)</p>
        
        <h2>المادة 5: السلوك المحظور</h2>
        <p>يُمنع على الوكلاء القيام بالأنشطة التالية:</p>
        <p>• استخدام طرق غير مشروعة لزيادة النقاط أو الأرباح</p>
        <p>• انتهاك حقوق الطبع والنشر أو الملكية الفكرية</p>
        <p>• التلاعب في نظام العمولات</p>
        <p>• نشر محتوى مسيء أو غير لائق</p>
        
        <h2>المادة 6: حماية البيانات والخصوصية</h2>
        <p>• حماية البيانات الشخصية للمضيفين والمستخدمين</p>
        <p>• عدم مشاركة المعلومات السرية مع أطراف ثالثة</p>
        <p>• استخدام البيانات فقط للأغراض المصرح بها</p>
        <p>• استخدام كلمات مرور قوية وآمنة</p>
        
        <h2>المادة 7: تعديل السياسة</h2>
        <p>تحتفظ WaveLive بالحق في تعديل هذه السياسة في أي وقت. سيتم إشعار الوكلاء بأي تغييرات مهمة قبل 30 يوماً من سريانها.</p>
        
        <h2>معلومات الاتصال</h2>
        <p>للاستفسارات حول هذه السياسة:</p>
        <p>• البريد الإلكتروني: support@wave-live.com</p>
        <p>• الموقع الإلكتروني: wave-live.com</p>
        <p>• قسم دعم الوكلاء: agents@wave-live.com</p>
    """
    
    # إنشاء الملفات
    create_simple_pdf("agent-guide.html", "دليل التسجيل كوكيل في WaveLive", agent_guide_content)
    create_simple_pdf("privacy-policy.html", "سياسة الوكلاء - WaveLive", privacy_policy_content)
    
    print("\n📋 تم إنشاء ملفات HTML للطباعة كـ PDF:")
    print("├── agent-guide.html")
    print("└── privacy-policy.html")
    print("\n💡 لتحويلها إلى PDF:")
    print("1. افتح الملفات في المتصفح")
    print("2. اضغط Ctrl+P (أو Cmd+P على Mac)")
    print("3. اختر 'Save as PDF'")
    print("4. احفظ باسم agent-guide.pdf و privacy-policy.pdf")

if __name__ == "__main__":
    main()
