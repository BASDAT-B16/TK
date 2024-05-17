from django.shortcuts import render
from psycopg2 import sql
from pacilflix.database_manager import DatabaseManager

from django.shortcuts import render
from django.db import connection

def show_daftarkontributor(request):
    kontributor = []
    try:
        tipe = request.GET.get('tipe', 'all')
        print(tipe)
        cursor = DatabaseManager.get_dict_cursor()
        kontributor = cursor.fetchall()
        cursor.close()
    except Exception as e:
        DatabaseManager.rollback()
        print(e)
    return render(request, "daftarkontributor.html", {'kontributor': kontributor})
