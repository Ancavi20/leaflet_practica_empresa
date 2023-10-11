from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.views.decorators.http import require_POST
from django.shortcuts import render, get_object_or_404, redirect
from .models import Location
from .forms import EditLocationForm, UserRegisterForm, LoginForm
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse
from django.conf import settings
from django.core.files.storage import FileSystemStorage

import logging
console = logging.getLogger('django')

# Esta vista es el main de la aplicación
def mapa(request):
    locations = Location.objects.all()
    return render(request, 'map/main.html', {'locations': locations})

# Esta vista se encarga de guardar las nuevas localizaciones creadas en la BD
@require_POST
def create_location(request):
    try:
        name = request.POST.get('name')
        latitude = float(request.POST.get('latitude'))
        longitude = float(request.POST.get('longitude'))

        new_location = Location.objects.create(
            name=name,
            latitude=latitude,
            longitude=longitude
        )

        return JsonResponse({'success': True, 'id': new_location.id, 'name': new_location.name})
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)})

# Esta vista se encarga de cargar todas las localizaciones existentes al cargar la página
def get_locations(request):
    if request.method == 'GET':
        locations = Location.objects.all()
        data = [{'name': location.name, 'latitude': location.latitude, 'longitude': location.longitude} for location in locations] # Se crea un diccionario que será devuelto como JSON a la petición
        return JsonResponse(data, safe=False)
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)

#Esta vista se encarga de cargar de la edición de las localizaciones
def edit_location(request, location_id):
    location = get_object_or_404(Location, id=location_id)

    if request.method == 'POST':
        form = EditLocationForm(request.POST, instance=location)
        if form.is_valid():
            form.save()  # Guardar los cambios en la base de datos
            return HttpResponseRedirect('/')  # Redirigir a la página principal o a donde desees
    else:
        location.latitude = str(location.latitude).replace(',', '.')    # Django no detecta las coordenadas con , como números tipo float
        location.longitude = str(location.longitude).replace(',', '.')
        form = EditLocationForm(instance=location)

    return render(request, 'map/edit_location.html', {'location': location, 'form': form})

# Esta vista borra la ubicación
def delete_location(request, location_id):
    location = get_object_or_404(Location, id=location_id)
    location.delete()
    return redirect('map:mapa')

# Vista encargada del registro de usuarios
def register_user(request):
    if request.method == 'POST':
        console.info(request.POST)
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            console.info('Usuario registrado')
            login(request, user)
            return redirect('map:mapa')
    else:
        form = UserRegisterForm()

    return render(request, 'map/register_user.html', {'form': form})

# Vista envargada del inicio de sesión de usuarios
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirigir a la página deseada después del inicio de sesión
                return redirect('map:mapa')
    else:
        form = LoginForm()

    return render(request, 'map/login.html', {'form': form})

# Vista para cerrar sesión del usuario
def logout_view(request):
    logout(request)
    return redirect('map:mapa')