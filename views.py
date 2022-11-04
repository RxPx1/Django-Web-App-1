from django.shortcuts import render

# Create your views here.
def home(request):
    import requests
    import json 
    
    if request.method == 'POST':
        ticker = request.POST['ticker']
        api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + ticker + "/quote?token=pk_bb64065f65954a3f9d06261971083a77")
         
        try:
            api=json.loads(api_request.content)
        except Exception as e:
            api = "Error..."
        return render(request, 'home.html', {'api': api })
            
             
    else:
        return render(request, 'home.html', {'ticker': "Enter a ticker symbol above."})
    
    
    


def about(request):
    return render(request, 'about.html', {})

def add_stock(request):
    return render(request, 'add_stock.html', {})

#pk_bb64065f65954a3f9d06261971083a77