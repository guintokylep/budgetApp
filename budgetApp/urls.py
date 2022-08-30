
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),


    path("display/<int:id>", views.display, name="display"),
    path("display/<int:id>/delete", views.deleteTransaction, name="deleteTransaction"),
    path("display/unread/<int:id>", views.unread, name="unread"),
    path("display/transaction/<int:id>/<int:pageNo>", views.transaction, name="transaction"),

    path("addTransaction/<int:id>", views.addTransaction, name="addTransaction"),
    path("display/editTransaction/<int:id>", views.editTransaction, name="editTransaction"),
    
    path("editTransaction/creditEdit/<int:id>", views.creditEdit, name="creditEdit"),
    path("editTransaction/debitEdit/<int:id>", views.debitEdit, name="debitEdit"),
    path("editTransaction/transferEdit/<int:id>", views.transferEdit, name="transferEdit"),
    path("addTransaction/<int:id>/creditAdd", views.creditAdd, name="creditAdd"),
    path("addTransaction/<int:id>/debitAdd", views.debitAdd, name="debitAdd"),
    path("addTransaction/<int:id>/transferAdd", views.transferAdd, name="transferAdd"),

    path("settings", views.settings, name="settings"),

    path("accounts",views.accounts, name="accounts"),
    path("accounts/delete",views.deleteAccount, name="deleteAccount"),
    path("addAccount",views.addAccount, name="addAccount"),
    path("editAccount/<int:id>",views.editAccount, name="editAccount"),

    path("categories",views.categories, name="categories"),
    path("categories/deleteCategory",views.deleteCategory, name="deleteCategory"),
    path("categories/deleteSubcategory",views.deleteSubcategory, name="deleteSubcategory"),
    path("editCategory/<int:id>",views.editCategory, name="editCategory"),
    path("editSubCategory/<int:id>",views.editSubCategory, name="editSubCategory"),
    path("addCategory",views.addCategory, name="addCategory"),
]