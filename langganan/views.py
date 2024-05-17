from django.shortcuts import render
from pacilflix.database_manager import DatabaseManager
import langganan.queries as queries
from django.views.decorators.csrf import csrf_exempt

def show_langganan(request):
    context = {}

    username = request.COOKIES.get('username')

    try:
        cursor = DatabaseManager.get_dict_cursor()
        cursor.execute(queries.current_subscription_query, (username,))
        current_subscription = cursor.fetchone()
        if current_subscription:
            nama_paket = current_subscription.get('nama', '')
        else:
            nama_paket = ''
        cursor.execute(queries.other_subscriptions_query, (nama_paket,))
        other_subscriptions = cursor.fetchall()
        cursor.execute(queries.history_of_subscriptions_query, (username,))
        history_of_subscriptions = cursor.fetchall()

        context = {
            'current_subscription': current_subscription,
            'other_subscriptions': other_subscriptions,
            'history_of_subscriptions': history_of_subscriptions,
        }

    except Exception as e:
        DatabaseManager.rollback()
        print(e)
    
    return render(request, "langganan.html", context)

@csrf_exempt
def show_beli(request):
    if request.method == 'POST':
        username = request.COOKIES.get('username')

        try:
            cursor = DatabaseManager.get_dict_cursor()
            cursor.execute(queries.current_subscription_query, (username,))
            current_subscription = cursor.fetchone()
        
        except Exception as e:
            DatabaseManager.rollback()
            print(e)

    return render(request, 'beli.html')