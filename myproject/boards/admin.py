from django.contrib import admin
from .models import קטגוריה, מוצר, ספק, הזמנה
class orderInline(admin.TabularInline):
    model = הזמנה
    extra = 1

# מודל שמיועד לתצוגה בדף ה-admin
@admin.register(קטגוריה)
class categoryAdmin(admin.ModelAdmin):
    list_display = ('שם',)

@admin.register(מוצר)
class itemAdmin(admin.ModelAdmin):
    list_display = ('שם', 'קטגוריה', 'cal_sum_in_stock')  # נוסיף עמודה מחושבת
    inlines = [orderInline]  # הצג נתוני הזמנה בעמודת המוצר

    def cal_sum_in_stock(self, obj):
        הזמנות = הזמנה.objects.filter(מוצר=obj)
        sum_in_stock = sum(הזמנה.כמות for הזמנה in הזמנות)
        return sum_in_stock

    cal_sum_in_stock.short_description = 'כמות במלאי'

@admin.register(ספק)
class ספקAdmin(admin.ModelAdmin):
    list_display = ('שם',)

@admin.register(הזמנה)
class הזמנהAdmin(admin.ModelAdmin):
    list_display = ('מוצר', 'ספק', 'כמות', 'תאריך')