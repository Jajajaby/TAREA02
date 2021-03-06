from django.shortcuts import render
from basket.models import Player
from basket.forms import PlayerForm
from django.http import HttpResponse
from django.shortcuts import redirect


def index(request):
    data = {}

    data['saludar'] = 'Hola dsfs'

    # SELECT * FROM player
    data['object_list'] = Player.objects.all().order_by('-id')

    template_name = 'player/list_player.html'
    return render(request, template_name, data)


def detail(request, player_id):

    data = {}
    template_name = 'player/detail_player.html'

    # SELECT * FROM player WHERE id = player_id
    data['player'] = Player.objects.get(pk=player_id)
    # import pdb;pdb.set_trace()

    return render(request, template_name, data)

def delete(request,player_rut):
    p = Player.objects.get(rut=player_rut)
    p.delete()
    return redirect("player_list2")


def add(request):
    data = {}
    if request.method == "POST":
        data['form'] = PlayerForm(request.POST, request.FILES)

        if data['form'].is_valid():
            # aca el formulario valido
            data['form'].save()

            return redirect('player_list')

    else:
        data['form'] = PlayerForm()


    template_name = 'player/agregar.html'
    return render(request, template_name,data)

def update(request,player_rut):
    data = {}
    player = Player.objects.get(rut=player_rut)
    if request.method == "GET":
        data['form'] = PlayerForm(instance=player)
    else:
        data['form']= PlayerForm(request.POST,request.FILES, instance=player)
        p = data['form']
        if p.is_valid():
            p.save()
        return redirect("player_list2")
    template_name = 'player/agregar.html'
    return render(request,template_name,data)

    
def list2(request):
    data = {}
    template_name = 'player/listar.html'
    data['list_player'] = Player.objects.all()
    # import pdb;pdb.set_trace()

    return render(request, template_name,data)
