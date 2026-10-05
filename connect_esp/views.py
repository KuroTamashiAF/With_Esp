from django.http import JsonResponse
from django.shortcuts import render
from connect_esp.models import LedCommand


# Create your views here.
def connect_esp_view(request, cmd):
    "hkhdkhvkgv"
    if cmd in ("on", "off"):
        command = LedCommand(command_esp=cmd)
        command.save()
    last_command_on_DB = LedCommand.objects.all().last()
    if last_command_on_DB:
        last = last_command_on_DB.command_esp
        time = last_command_on_DB.date

    context = {
        "title": "Управление",
        # "kkk": "какаха",
        "cmd": f"{cmd}",
        "last": f"{last}",
        "time": f"{time}",
    }

    return render(request, "connect_esp/connect_esp.html", context)



def status_view(request):
    last_command  = LedCommand.objects.all().last()
    if last_command:
        data = {
            "command": f"{last_command.command_esp}"
        }
    else:
        data = {
                    "command": "off"
                }
    return JsonResponse(data)
