from django.http import JsonResponse
from .models import FunctionDefinition

def call_function(request):
    if request.method == 'GET':
        #function_name = request.POST.get('function_name', '')
        #input_parameters = request.POST.get('input_parameters', '')        
        try:
            # Fetch the function definition from the database
            function_definition = FunctionDefinition.objects.get(name='print_param')
            # Using exec to execute the code
            namespace = {}
            exec(function_definition.code, namespace)

            # Call the dynamically defined function
            result = namespace['print_param']('John')

            print(result)  # Output: Hello, John!

            return JsonResponse({'result': result})
        except Exception as e:
            return JsonResponse({'error': str(e)})
    else:
        return JsonResponse({'error': 'Invalid request method'})
