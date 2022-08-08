from django.contrib import admin

from .models import User, Categories, SubCategories, Account, Transaction

class AccountAdmin(admin.ModelAdmin):
    list_display = ("id","userAccount", "accountName", "description","balance","ins_date")

class CategoriesAdmin(admin.ModelAdmin):
    list_display = ("id","userCategory", "category", "ins_date")

class SubCategoriesAdmin(admin.ModelAdmin):
    list_display = ("id","userSubCategory", "parentCategory", "subCategory" ,"ins_date" )
    
class TransactionAdmin(admin.ModelAdmin):
    list_display = ("id","userTransaction", "accountNameTransaction", "accountNameTransferFrom", "accountNameTransferTo", "transactionType", "amount","descriptionTransaction","categoryTransaction", "subCategoryTransaction", "transactionDate", "ins_date")

admin.site.register(User)
admin.site.register(Account, AccountAdmin)
admin.site.register(Categories, CategoriesAdmin)
admin.site.register(SubCategories, SubCategoriesAdmin)
admin.site.register(Transaction, TransactionAdmin)