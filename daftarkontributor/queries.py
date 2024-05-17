GET_CONTRIBUTORS_ALL = """
  SELECT id, nama, kewarganegaraan, 
  CASE WHEN C.jenis_kelamin = 0 THEN 'Laki-laki' ELSE 'Perempuan' END AS jenis_kelamin,
  CONCAT_WS(', ', 
      CASE WHEN C.id IN (SELECT P.id FROM PEMAIN P) THEN 'pemain' END,
      CASE WHEN C.id IN (SELECT S.id FROM SUTRADARA S) THEN 'sutradara' END,
      CASE WHEN C.id IN (SELECT PS.id FROM PENULIS_SKENARIO PS) THEN 'penulis_skenario' END
    ) AS tipe
  FROM CONTRIBUTORS C;
"""

GET_CONTRIBUTORS_TIPE = """
  SELECT C.id, C.nama, C.kewarganegaraan,
  CASE WHEN C.jenis_kelamin = 0 THEN 'Laki-laki' ELSE 'Perempuan' END AS jenis_kelamin,
  CONCAT_WS(', ', 
      CASE WHEN C.id IN (SELECT P.id FROM PEMAIN P) THEN 'pemain' END,
      CASE WHEN C.id IN (SELECT S.id FROM SUTRADARA S) THEN 'sutradara' END,
      CASE WHEN C.id IN (SELECT PS.id FROM PENULIS_SKENARIO PS) THEN 'penulis_skenario' END
    ) AS tipe
  FROM CONTRIBUTORS C
  JOIN {table} ON C.id = {table}.id;
"""


