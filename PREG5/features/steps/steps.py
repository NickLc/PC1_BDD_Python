from Formulario import Formulario
from Objeto import Objeto
from behave import given, when, then

@given('un formulario y un objeto')
def step_impl(context):
    context.objeto = Objeto("Dipositivos Moviles", "Nokia 3310", "Nokia", "Pequeño", "2000");
    context.formulario = Formulario();

@when('el formulario a sido rellenado')
def step_impl(context):
    context.formulario.rellenar(context.objeto)

@then('el formulario debe tener los campos obligarios')
def step_impl(context):
    assert (context.formulario.nombre != "")
    assert (context.formulario.categoria != "")
    assert (context.formulario.anio_de_creacion != "")
    
   