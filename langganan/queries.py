GET_ACTIVE_SUBSCRIPTION = '''
  SELECT P.nama, P.harga, P.resolusi_layar, start_date_time, end_date_time, dukungan_perangkat
  FROM TRANSACTION T
  JOIN PAKET P ON T.nama_paket = P.nama
  JOIN (
    SELECT nama_paket, string_agg(dukungan_perangkat, ', ') AS dukungan_perangkat
    FROM DUKUNGAN_PERANGKAT
    GROUP BY nama_paket
  ) AS D ON T.nama_paket = D.nama_paket
  WHERE T.username = %s AND T.end_date_time > NOW();
'''


GET_OTHER_SUBSCRIPTIONS = '''
  SELECT *
  FROM PAKET P
  JOIN (
    SELECT nama_paket, string_agg(dukungan_perangkat, ', ') AS dukungan_perangkat
    FROM DUKUNGAN_PERANGKAT
    GROUP BY nama_paket
  ) AS D ON P.nama = D.nama_paket
  WHERE P.nama <> %s;
'''

GET_SUBSCRIPTION_HISTORY = '''
  SELECT nama_paket, start_date_time, end_date_time, metode_pembayaran, timestamp_pembayaran, harga
  FROM TRANSACTION T
  JOIN PAKET P ON T.nama_paket = P.nama
  WHERE T.username = %s;
'''

GET_PAKET = '''
  SELECT *
  FROM PAKET P
  JOIN (
    SELECT nama_paket, string_agg(dukungan_perangkat, ', ') AS dukungan_perangkat
    FROM DUKUNGAN_PERANGKAT
    GROUP BY nama_paket
  ) AS D ON P.nama = D.nama_paket
  WHERE P.nama = %s;
'''

CREATE_TRANSACTION = '''
  INSERT INTO TRANSACTION (username, start_date_time, end_date_time, nama_paket, metode_pembayaran, timestamp_pembayaran)
  VALUES (%s, NOW(), NOW() + INTERVAL '1 month', %s, %s, NOW());
'''

UPDATE_SUBSCRIPTION = '''
  UPDATE TRANSACTION
  SET 
    start_date_time = NOW(),
    end_date_time = NOW() + INTERVAL '1 month',
    metode_pembayaran = %(metode_pembayaran)s,
    nama_paket = %(nama_paket)s
  WHERE username = %(username)s AND end_date_time > NOW();
'''