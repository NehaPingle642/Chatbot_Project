from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
import json
from .chatbot import get_response

@ensure_csrf_cookie
def chat_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_input = data.get('message')
            response = get_response(user_input)
            return JsonResponse({'response': response})
        except json.JSONDecodeError:
            return JsonResponse({'response': 'Invalid request'}, status=400)
    return render(request, 'chatbot/index.html')
