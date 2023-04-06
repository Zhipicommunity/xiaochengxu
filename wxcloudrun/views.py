from django.shortcuts import render
from rest_framework import generics
from .models import Pet
from .serializers import PetSerializer
from django.views import View

class UserLoginView(View):
    def user_login(request):
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                return render(request, 'login.html', {'error_message': 'Invalid login'})
        else:
            return render(request, 'login.html')



class PetListCreateView(generics.ListCreateAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer

    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')

    def post(self, request, *args, **kwargs):
        # 处理 POST 请求
        return HttpResponse(request,'api.html')
