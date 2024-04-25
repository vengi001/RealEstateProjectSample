from django.shortcuts import get_object_or_404, render
from rest_framework.decorators import api_view
from REP_App.forms import propertyform, tenantform
from django.shortcuts import redirect
from REP_App.models import property_profile, tenant_profile

# Create your views here.
def home(request):
    return render(request,'home.html',{})
    
def create_property(request):
    if request.method == 'POST':
        form = propertyform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = propertyform()
        
    return render(request,'property.html',{'form':form})

def viewall_property(request) :
    form = property_profile.objects.all()
    return render(request,'viewall_prop.html',{'form':form})

def prop_edit(request, pk):
    obj = get_object_or_404(property_profile, pk=pk)
    if request.method == 'POST':
        form = propertyform(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = propertyform(instance=obj)
    return render(request, 'property.html', {'form': form})

def prop_delete(request, pk):
    obj = get_object_or_404(property_profile, pk=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('home')
    return render(request, 'prop_delete.html', {'object': obj})


def create_Tenant(request):
    if request.method == 'POST':
        data = request.POST.copy()
        form = tenantform(data,request.FILES)
        if form.is_valid():
            print('is valid')
            form.save()
            return redirect('home')
        else:
                print(form.errors)
        
    else:
        form = tenantform()
        
    return render(request,'tenant.html',{'form':form})

def viewall_tenant(request) :
    form = tenant_profile.objects.all()
    return render(request,'viewall_tenant.html',{'form':form})

def tenant_edit(request, pk):
    obj = get_object_or_404(tenant_profile, pk=pk)
    if request.method == 'POST':
        form = tenantform(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = tenantform(instance=obj)
    return render(request, 'tenant.html', {'form': form})

def tenant_delete(request, pk):
    obj = get_object_or_404(tenant_profile, pk=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('index')
    return render(request, 'tenant_delete.html', {'object': obj})


def add_unit(request):
    if request.method == 'POST':
        form = tenantform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('property_grid')
    else:
        form = tenantform()

    return render(request, 'add_unit.html', {'form': form})