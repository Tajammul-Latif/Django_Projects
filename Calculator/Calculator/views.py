from django.shortcuts import render
from django.http import HttpResponse
from service.models import Services
from django.core.paginator import Paginator
from savedata.models import saveFormData


def showCalculator(request):
    
    data = {
                'output': '',
                'num1': '',
                'num2': '',
                'error': False
            }
    try:
        if request.method == 'POST':
            if request.POST.get('num1') == '':
                return render(request, 'index.html', {'error': True}) 
            else:
                num1 = eval(request.POST.get('num1'))
                num2 = eval(request.POST.get('num2'))
                opr = request.POST.get('opr')
                
                if opr == '+':
                    output = num1 + num2
                elif opr == '-':
                    output = num1 - num2
                elif opr == '*':
                    output = num1 * num2
                elif opr == '/':
                    output = num1 / num2
                    
                data = {
                    'output': output,
                    'num1': num1,
                    'num2': num2
                }

    except Exception as e:
        data['output'] = "Invalid Calculation"
        data['error'] = True 
    return render(request, 'index.html', data)



def showServices(request):
    servicesData = Services.objects.all()
    # for a in servicesData:
    #     print(a)
    
    
    paginator = Paginator(servicesData, 2)
    page_number = request.GET.get('page')
    servicesDataFinal = paginator.get_page(page_number)
    total_pages = servicesDataFinal.paginator.num_pages
    
    
    
    
    data = {
                'serviceData': servicesDataFinal,
                'last_page': total_pages,
                'totalPageList': [n+1 for n in range(total_pages)]
            }
    
    return render(request, 'services.html', data)

def showForm(request):
    return render(request, 'form_data.html')

def saveForm(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        website = request.POST.get('website')
        message = request.POST.get('message')
        
        data = {
            'name': name,
            'email': email,
            'phone': phone,
            'website': website,
            'message': message
        }
        
        send_Data = saveFormData(name = name, email = email, phone = phone, websiteLink = website, message = message)
        send_Data.save()
    return render(request, 'form_data.html')
    
    