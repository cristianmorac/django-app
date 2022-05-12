from django.shortcuts import render, redirect
from core.erp.forms import CategoryForm
from core.erp.models import Category, Product
from django.http import JsonResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt, csrf_protect
# lib de decorador
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
#funciones
def category_list(request):
    data = {
        'title': 'Listado de Categorías',
        'categories': Category.objects.all()
    }
    return render(request, 'category/list.html', data)

#clase de listar
class CategoryListView(ListView):
    model = Category
    template_name = 'category/list.html'

    #crear queryset
    
    ''' def get_queryset(self):
        return Category.objects.filter(name__startswith='L')   '''  
        
    # intermediario entre solicitudes y respuestas
    #@method_decorator(login_required)# decorador para forzar logueo
    @method_decorator(csrf_exempt)#desactivar proteccion csrf
    def dispatch(self,request,*args,**kwargs):
        #redireccionar a otra url
        ''' if request.method == 'GET':
            return redirect('erp:category_list2') '''
        return super().dispatch(request,*args,**kwargs) 

    def post(self,request,*args,**kwargs):
        data = {}
        #Controlar el error
        try:
           data = Category.objects.get(pk=request.POST['id']).toJson()
        except Exception as e:
            data['error'] = str(e)
        #obtener el id
        
        return JsonResponse(data)
    
    # decoradores funcionalidades a otras funciones


    #Sobreescribir archivos
    def get_context_data(self, **kwargs):
        # mostrar el titulo Listado de categorias
        context = super().get_context_data(**kwargs)
        # Nombres dianmicos
        context['title'] = 'Listado de categorias'
        context['entity'] = 'categorias'
        # redirecciones dinamicas
        context['create_url'] = reverse_lazy('erp:category_create')
        context['list_url'] = reverse_lazy('erp:category_list')
        
        #traer informacion del modelo
        #context['object_list'] = Product.objects.all()
        return context

# clase de crear
class CategoryCreateView(CreateView):
    model = Category
    # Variable para enviar al formulario
    form_class = CategoryForm
    # plantilla a utilizar
    template_name = 'category/create.html'
    # ruta redireccion url
    success_url = reverse_lazy('erp:category_list')

    def post(self, request,*args, **kwargs):
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            # Redireccionar             
            return HttpResponseRedirect(self.success_url)
        # no agregar valores nulos
        self.object = None
        context = self.get_context_data(**kwargs)
        context['form'] = form
        return render(request,self.template_name, context)
        

    def get_context_data(self, **kwargs):
        # mostrar el titulo Listado de categorias
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear categorias'
        context['entity'] = 'categorias'
        context['list_url'] = reverse_lazy('erp:category_list')
        #traer informacion del modelo
        #context['object_list'] = Product.objects.all()
        return context
