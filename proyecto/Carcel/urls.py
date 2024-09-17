
from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

app_name = "presos"

urlpatterns = [
    path("", login_required(views.index), name="index"),
    path("presos/",login_required(views.preso), name="preso"),
    path("presos/list", login_required(views.presos_list), name="agregar_preso"),
    path("prision",login_required(views.prision), name="prision"),
    path("prision/create", login_required(views.prision_create), name="prision_create" ),
    path("prision/list", login_required(views.prision_list), name="prision_list"),
    path("presos/create", login_required(views.presos_create), name="presos_create"),
    path("presos/list", login_required(views.presos_list), name="presos_list"),
    path("presos/detail/<int:pk>", login_required(views.presos_detail), name="presos_detail"),
    path("prision/detail/<int:pk>", login_required(views.prision_detail), name="prision_detail"),
    path("presos/update/<int:pk>", login_required(views.presos_update), name="presos_update"),
    path("prision/update/<int:pk>", login_required(views.prision_update), name="prision_update"),
    path("presos/confirm/delete/<int:pk>", login_required(views.presos_confirm_delete), name="presos_confirm_delete"),
    path("prision/confirm/delete/<int:pk>", login_required(views.prision_confirm_delete), name="prision_confirm_delete")
]
