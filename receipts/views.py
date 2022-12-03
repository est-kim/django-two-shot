from django.shortcuts import render, get_object_or_404, redirect
from receipts.models import Account, ExpenseCategory, Receipt
from receipts.forms import ReceiptForm
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
