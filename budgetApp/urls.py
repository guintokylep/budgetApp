
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),

    # display transaction
    path("display/<int:id>", views.display, name="display"),
    path("display/<int:id>/delete", views.deleteTransaction, name="deleteTransaction"),
    path("display/unread/<int:id>", views.unread, name="unread"),
    path("display/transaction/<int:id>/<int:pageNo>", views.transaction, name="transaction"),

    path("addTransaction/<int:id>", views.addTransaction, name="addTransaction"),
    path("display/editTransaction/<int:id>", views.editTransaction, name="editTransaction"),
    
    # add or edit transaction page
    path("editTransaction/creditEdit/<int:id>", views.creditEdit, name="creditEdit"),
    path("editTransaction/debitEdit/<int:id>", views.debitEdit, name="debitEdit"),
    path("editTransaction/transferEdit/<int:id>", views.transferEdit, name="transferEdit"),
    path("addTransaction/<int:id>/creditAdd", views.creditAdd, name="creditAdd"),
    path("addTransaction/<int:id>/debitAdd", views.debitAdd, name="debitAdd"),
    path("addTransaction/<int:id>/transferAdd", views.transferAdd, name="transferAdd"),

    #settings
    path("settings", views.settings, name="settings"),

    #budget
    path("budget", views.budget, name="budget"),
    path("budget/delete", views.deleteBudget, name="deleteBudget"),
    path("addBudget", views.addBudget, name="addBudget"),
    path("budgetAdd", views.budgetAdd, name="budgetAdd"),
    path("budget/budgetTransaction", views.budgetTransaction, name="budgetTransaction"),
    path("budget/budgetDisplay", views.budgetDisplay, name="budgetDisplay"),
    path("editBudget/<int:id>", views.editBudget, name="editBudget"),
    path("budgetEdit/<int:id>", views.budgetEdit, name="editBudget"),

    #report
    path("report", views.report, name="report"),
    path("expensesIncome", views.expensesIncome, name="expensesIncome"),
    path("expensesIncome/expensesIncomeDisplay", views.expensesIncomeDisplay, name="expensesIncomeDisplay"),
    path("expensesIncome/expensesIncomeDetail", views.expensesIncomeDetail, name="expensesIncomeDetail"),
    path("accountReport", views.expensesIncome, name="accountReport"),
    path("accountReport/accountReportDisplay", views.expensesIncomeDisplay, name="accountReportDisplay"),

    #schedule
    path("schedule", views.schedule, name="schedule"),
    path("schedule/delete", views.deleteSchedule, name="deleteSchedule"),
    path("addSchedule", views.addSchedule, name="addSchedule"),
    path("addSchedule/creditAddSched", views.creditAddSched, name="creditAddSched"),
    path("addSchedule/debitAddSched", views.debitAddSched, name="debitAddSched"),
    path("addSchedule/transferAddSched", views.transferAddSched, name="transferAddSched"),
    path("editSchedule/<int:id>", views.editSchedule, name="editSchedule"),
    path("editSchedule/creditEditSched/<int:id>", views.creditEditSched, name="creditEditSched"),
    path("editSchedule/debitEditSched/<int:id>", views.debitEditSched, name="debitEditSched"),
    path("editSchedule/transferEditSched/<int:id>", views.transferEditSched, name="transferEditSched"),
    path("schedule/scheduleDisplay", views.scheduleDisplay, name="scheduleDisplay"),

    #accounts
    path("accounts",views.accounts, name="accounts"),
    path("accounts/delete",views.deleteAccount, name="deleteAccount"),
    path("addAccount",views.addAccount, name="addAccount"),
    path("editAccount/<int:id>",views.editAccount, name="editAccount"),

    #categories/subcategories
    path("categories",views.categories, name="categories"),
    path("categories/deleteCategory",views.deleteCategory, name="deleteCategory"),
    path("categories/deleteSubcategory",views.deleteSubcategory, name="deleteSubcategory"),
    path("editCategory/<int:id>",views.editCategory, name="editCategory"),
    path("editSubCategory/<int:id>",views.editSubCategory, name="editSubCategory"),
    path("addCategory",views.addCategory, name="addCategory"),
]