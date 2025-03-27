from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.apps import apps  # ✅ Import apps module
from .forms import ServiceRequestForm

# ✅ Replace direct model imports with apps.get_model()
ServiceRequest = apps.get_model('customer_service', 'ServiceRequest')
ServiceRequestType = apps.get_model('customer_service', 'ServiceRequestType')

# User view: Submit a service request
@login_required
def submit_service_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.user = request.user
            service_request.save()
            return redirect('request_status', request_id=service_request.id)
    else:
        form = ServiceRequestForm()
    return render(request, 'customer_service/submit_request.html', {'form': form})

# User view: Check the status of a specific service request
@login_required
def request_status(request, request_id):
    service_request = get_object_or_404(ServiceRequest, id=request_id, user=request.user)
    return render(request, 'customer_service/request_status.html', {'request': service_request})

# User view: List all requests submitted by the logged-in user
@login_required
def request_list(request):
    service_requests = ServiceRequest.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'customer_service/request_list.html', {'requests': service_requests})

# Check if a user is a staff member
def is_staff(user):
    return user.is_staff

# Staff view: View and manage all service requests
@user_passes_test(is_staff)
def support_dashboard(request):
    requests = ServiceRequest.objects.all().order_by('-created_at')
    return render(request, 'customer_service/support_dashboard.html', {'requests': requests})

# Staff view: Update the status of a service request
@user_passes_test(is_staff)
def update_request_status(request, request_id):
    service_request = get_object_or_404(ServiceRequest, id=request_id)
    if request.method == 'POST':
        new_status = request.POST.get('status')
        if new_status in dict(ServiceRequest.STATUS_CHOICES):
            service_request.status = new_status
            service_request.save()
    return redirect('support_dashboard')

