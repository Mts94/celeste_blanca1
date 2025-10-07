from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Afiliado
from .forms import AfiliadoForm, UploadFileForm
import pandas as pd
from django.http import HttpResponse
from django.db.models import Q
import openpyxl
from django.db import IntegrityError
from django.contrib import messages


@login_required
def lista_afiliados(request):
    afiliados = Afiliado.objects.all()

    # filtros
    q = request.GET.get("q", "")
    numero_afiliado = request.GET.get("numero_afiliado", "")
    sector = request.GET.get("sector", "")
    ocultar_hechos = request.GET.get("ocultar_hechos", "")
    localidad = request.GET.get("localidad", "")  # 🔹 nuevo filtro
    
    if q:
        afiliados = afiliados.filter(nombre__icontains=q)
    if numero_afiliado:
        afiliados = afiliados.filter(numero_afiliado__icontains=numero_afiliado)
    if zona:
        afiliados = afiliados.filter(zona__icontains=zona)
    if localidad:
        afiliados = afiliados.filter(localidad__icontains=localidad)  # 🔹 filtra por localidad

    

    # exportar solo lo filtrado
    if "exportar" in request.GET:
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.title = "Afiliados"

        # encabezados
        ws.append(["Nombre", "DNI", "Número Afiliado", "Zona", "Hecho","localidad"])

        # solo los registros filtrados
        for a in afiliados:
            ws.append(
                [
                    a.apellido_nombre,
                    a.dni,
                    a.numero_afiliado,
                    a.sector,
                    "Sí" if a.hecho else "No",
                    a.localidad,
                ]
            )

        response = HttpResponse(content_type="application/ms-excel")
        response["Content-Disposition"] = (
            'attachment; filename="afiliados_filtrados.xlsx"'
        )
        wb.save(response)
        return response

    return render(request, "afiliados/lista.html", {"afiliados": afiliados})


@login_required
def crear_afiliado(request):
    if request.method == "POST":
        form = AfiliadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("lista_afiliados")
    else:
        form = AfiliadoForm()
    return render(request, "afiliados/crear_afiliado.html", {"form": form})


@login_required
def editar_afiliado(request, pk):
    afiliado = get_object_or_404(Afiliado, pk=pk)
    if request.method == "POST":
        form = AfiliadoForm(request.POST, instance=afiliado)
        if form.is_valid():
            form.save()
            return redirect("lista_afiliados")
    else:
        form = AfiliadoForm(instance=afiliado)
    return render(request, "afiliados/editar_afiliado.html", {"form": form})


@login_required
def eliminar_afiliado(request, pk):
    afiliado = get_object_or_404(Afiliado, pk=pk)
    afiliado.delete()
    return redirect("lista_afiliados")


@login_required
def upload_excel(request):
    if request.method == "POST":
        excel_file = request.FILES.get("excel_file")
        df = pd.read_excel(excel_file)

        for _, row in df.iterrows():
            try:
                Afiliado.objects.create(
                    dni=row.get("dni"),
                    apellido_nombre=row.get("apellido_nombre", ""),
                    sector=row.get("sector", ""),
                    numero_afiliado=row.get("numero_afiliado", ""),
                    locaalidad=row.get("localidad", ""),
                    telefono=row.get("telefono", ""),
                    direccion=row.get("direccion", ""),
                    horario=row.get("horario"),
                    observacion=row.get("observacion", ""),
                )
            except IntegrityError:
                messages.warning(
                    request, f"El DNI {row.get('dni')} ya existe y no fue cargado."
                )

        messages.success(request, "Carga de Excel completada.")
        return redirect("lista_afiliados")  # redirige a donde quieras
    return render(request, "afiliados/upload_excel.html", {"form": UploadFileForm()})


@login_required
def exportar_excel(request):
    # --- Filtros (igual que en lista_afiliados) ---
    query = request.GET.get("q", "")
    numero_afiliado = request.GET.get("numero_afiliado", "")
    sector = request.GET.get("sector", "")
    localidad = request.GET.get("localidad", "")  # 🔹 nuevo filtro

    afiliados = Afiliado.objects.all()

    if query:
        afiliados = afiliados.filter(
            Q(apellido_nombre__icontains=query) | Q(dni__icontains=query)
        )
    if numero_afiliado:
        afiliados = afiliados.filter(numero_afiliado__icontains=numero_afiliado)
    if sector:
        afiliados = afiliados.filter(sector__icontains=sector)
    if localidad:
        afiliados = afiliados.filter(localidad__icontains=localidad)

    # --- Exportación ---
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Afiliados"

    # Encabezados
    ws.append(["Nombre", "DNI", "Número Afiliado", "Localidad", "Teléfono"])

    # Datos
    for afiliado in afiliados:
        ws.append(
            [
                afiliado.apellido_nombre,
                afiliado.dni,
                afiliado.numero_afiliado,
                afiliado.localidad,
                afiliado.telefono,
            ]
        )

    # Respuesta HTTP
    response = HttpResponse(
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
    response["Content-Disposition"] = "attachment; filename=afiliados.xlsx"
    wb.save(response)
    return response
