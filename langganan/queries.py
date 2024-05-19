current_subscription_query = '''
  SELECT PAKET.nama, PAKET.harga, PAKET.resolusi_layar, start_date_time, end_date_time, dukungan_perangkat
  FROM TRANSACTION
  JOIN PAKET ON TRANSACTION.nama_paket = PAKET.nama
  JOIN (
    SELECT nama_paket, string_agg(dukungan_perangkat, ', ') AS dukungan_perangkat
    FROM DUKUNGAN_PERANGKAT
    GROUP BY nama_paket
  ) AS DUKUNGAN_PERANGKAT ON TRANSACTION.nama_paket = DUKUNGAN_PERANGKAT.nama_paket
  WHERE TRANSACTION.username = %s AND TRANSACTION.end_date_time > NOW();
'''

other_subscriptions_query = '''
  SELECT *
  FROM PAKET
  JOIN (
    SELECT nama_paket, string_agg(dukungan_perangkat, ', ') AS dukungan_perangkat
    FROM DUKUNGAN_PERANGKAT
    GROUP BY nama_paket
  ) AS DUKUNGAN_PERANGKAT ON PAKET.nama = DUKUNGAN_PERANGKAT.nama_paket
  WHERE PAKET.nama <> %s;
'''

history_of_subscriptions_query = '''
  SELECT nama_paket, start_date_time, end_date_time, metode_pembayaran, timestamp_pembayaran, harga
  FROM TRANSACTION
  JOIN PAKET  ON TRANSACTION.nama_paket = PAKET.nama
  WHERE TRANSACTION.username = %s;
'''

get_paket_query = '''
  SELECT *
  FROM PAKET P
  JOIN (
    SELECT nama_paket, string_agg(dukungan_perangkat, ', ') AS dukungan_perangkat
    FROM DUKUNGAN_PERANGKAT
    GROUP BY nama_paket
  ) AS D ON P.nama = D.nama_paket
  WHERE P.nama = %s;
'''