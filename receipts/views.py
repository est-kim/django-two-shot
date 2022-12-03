from django.shortcuts import render, get_object_or_404, redirect
from receipts.models import Account, ExpenseCategory, Receipt
from receipts.forms import ReceiptForm, ExpenseCategoryForm, AccountForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def receipt_list(request):
    receipts = Receipt.objects.filter(purchaser=request.user)
    context = {
        "receipts" : receipts,
    }
    return render(request, "receipts/list.html", context)

@login_required
def create_receipt(request):
    if request.method == "POST":
        form = ReceiptForm(request.POST)
        if form.is_valid():
            receipt = form.save(False)
            receipt.purchaser = request.user
            receipt.save()
            return redirect("home")
    else:
        form = ReceiptForm()
    context = {
        "form": form,
    }
    return render(request, "receipts/create.html", context)

@login_required
def category_list(request):
    categories = ExpenseCategory.objects.filter(owner=request.user)
    context = {
        "categories": categories,
    }
    return render(request, "receipts/categories.html", context)

@login_required
def account_list(request):
    accounts = Account.objects.filter(owner=request.user)
    context = {
        "accounts": accounts,
    }
    return render(request,"receipts/accounts.html", context)

@login_required
def create_category(request):
    if request.method == "POST":
        form = ExpenseCategoryForm(request.POST)
        if form.is_valid():
            expense = form.save(False)
            expense.owner = request.user
            expense.save()
            return redirect("category_list")
    else:
        form = ExpenseCategoryForm()
    context = {
        "form": form,
    }
    return render(request, "receipts/create_cat.html", context)

@login_required
def create_account(request):
    if request.method == "POST":
        form = AccountForm(request.POST)
        if form.is_valid():
            account = form.save(False)
            account.owner = request.user
            account.save()
            return redirect("account_list")
    else:
        form = AccountForm()
    context = {
        "form": form,
    }
    return render(request, "receipts/create_acc.html", context)
