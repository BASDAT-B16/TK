from django.shortcuts import render
from psycopg2 import sql
from pacilflix.database_manager import DatabaseManager
import daftarkontributor.queries

from django.shortcuts import render
from django.db import connection

def show_daftarkontributor(request):
    kontributor = []
    try:
        tipe = request.GET.get('tipe', 'all')
        cursor = DatabaseManager.get_dict_cursor()

        if tipe in ['pemain', 'sutradara', 'penulis_skenario']:
            cursor.execute(sql.SQL(daftarkontributor.queries.contributors_by_type_query).format(table=sql.Identifier(tipe)))
        else:
            tipe = 'all'
            cursor.execute(daftarkontributor.queries.contributors_all_query)

        kontributor = cursor.fetchall()
        cursor.close()

    except Exception as e:
        DatabaseManager.rollback()
        print(e)
    return render(request, "daftarkontributor.html", {'kontributor': kontributor})
