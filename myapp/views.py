from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Resource
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'index.html')

def signup_user(request):
    if request.method != 'POST':
        return redirect('index')

    name = request.POST.get('signupName', '').strip()
    email = request.POST.get('signupEmail', '').strip().lower()
    password = request.POST.get('signupPassword', '')
    password_confirm = request.POST.get('signupPasswordConfirm', '')

    # Basic validation
    if not email or not password:
        return render(request, 'index.html', {
            'signup_error': 'Email and password are required.',
            'show_signup': True
        })

    if password != password_confirm:
        return render(request, 'index.html', {
            'signup_error': 'Passwords do not match.',
            'show_signup': True
        })

    if User.objects.filter(username=email).exists() or User.objects.filter(email__iexact=email).exists():
        return render(request, 'index.html', {
            'signup_error': 'An account with that email already exists.',
            'show_signup': True
        })

    # Create account (username == email to keep it simple)
    user = User.objects.create_user(username=email, email=email, password=password, first_name=name)
    user.save()
    # Try to authenticate + login immediately
    user = authenticate(request, username=email, password=password)
    if user is None:
        # unexpected, add a debug print to console for investigation
        print('DEBUG: created user but authenticate() returned None for', email)
        return render(request, 'index.html', {
            'signup_error': 'Account created but auto-login failed — please sign in.',
            'show_signup': False
        })

    login(request, user)
    return redirect('dashboard')


def login_user(request):
    if request.method != 'POST':
        return redirect('index')

    email = request.POST.get('loginEmail', '').strip().lower()
    password = request.POST.get('loginPassword', '')

    # Debug: print POST keys/values to server console (remove in production)
    print('DEBUG login POST:', dict(request.POST))

    if not email or not password:
        return render(request, 'index.html', {
            'login_error': 'Please enter email and password.',
            'show_signup': False
        })

    # Try authenticate using username==email
    user = authenticate(request, username=email, password=password)

    # Fallback: maybe username != email in DB — try to find user by email and authenticate with its username
    if user is None:
        try:
            found = User.objects.get(email__iexact=email)
            # try authenticate with actual username
            user = authenticate(request, username=found.username, password=password)
            print('DEBUG: fallback found user by email, tried authenticate with username=', found.username, 'result=', bool(user))
        except User.DoesNotExist:
            user = None

    if user is None:
        # Provide a helpful inline error and show appropriate tab
        if User.objects.filter(email__iexact=email).exists():
            return render(request, 'index.html', {
                'login_error': 'Invalid password. Please try again.',
                'show_signup': False
            })
        else:
            return render(request, 'index.html', {
                'login_error': 'No account found for that email — please sign up.',
                'show_signup': True
            })

    if not user.is_active:
        return render(request, 'index.html', {
            'login_error': 'Account disabled. Contact admin.',
            'show_signup': False
        })

    login(request, user)
    return redirect('dashboard')

# Logout View
def logout_user(request):
    auth.logout(request)
    return redirect('index')


@login_required(login_url='index')
def dashboard(request):
    resources = Resource.objects.filter(user=request.user).order_by('-updated_at')

    total = resources.count()
    completed = resources.filter(progress=100).count()
    in_progress = resources.filter(progress__gt=0, progress__lt=100).count()
    avg = int(round(sum(r.progress for r in resources) / total)) if total else 0

    context = {
        "resources": resources,
        "stats": {
            "totalResources": total,
            "completedResources": completed,
            "inProgressResources": in_progress,
            "averageProgress": avg,
        },
    }
    return render(request, "dashboard.html", context)


def add_resource_view(request):
    if request.method == "POST":
        title = request.POST.get("title", "").strip()
        category = request.POST.get("category")
        try:
            progress = int(request.POST.get("progress", 0))
        except (TypeError, ValueError):
            progress = 0

        if not title:
            messages.error(request, "Title is required.")
            return redirect('add_resource')

        resource = Resource.objects.create(
            user=request.user,
            title=title,
            category=category,
            progress=max(0, min(100, progress))
        )
        messages.success(request, "Resource added successfully.")
        return redirect('dashboard')

    return render(request, "add-resource.html")


@login_required(login_url='index')
def resource_detail_view(request, resource_id):
    resource = get_object_or_404(Resource, id=resource_id, user=request.user)

    if request.method == "POST":
        if 'update_progress' in request.POST:
            try:
                progress = int(request.POST.get('progress', resource.progress))
                resource.progress = max(0, min(100, progress))
                resource.save()
                messages.success(request, "Progress updated.")
            except (TypeError, ValueError):
                messages.error(request, "Invalid progress value.")
            return redirect('resource_detail', resource_id=resource.id)

        elif 'mark_completed' in request.POST:
            resource.progress = 100
            resource.completed = True
            resource.save()
            messages.success(request, "Marked as completed.")
            return redirect('resource_detail', resource_id=resource.id)

    context = {"resource": resource}
    return render(request, "resource-detail.html", context)