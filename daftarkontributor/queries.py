GET_CONTRIBUTORS_ALL = """
  SELECT 
    id, 
    nama, 
    kewarganegaraan, 
    IF(C.jenis_kelamin = 0, 'Laki-laki', 'Perempuan') AS jenis_kelamin,
    CONCAT_WS(', ', 
      IF(C.id IN (SELECT P.id FROM PEMAIN P), 'pemain', NULL),
      IF(C.id IN (SELECT S.id FROM SUTRADARA S), 'sutradara', NULL),
      IF(C.id IN (SELECT PS.id FROM PENULIS_SKENARIO PS), 'penulis_skenario', NULL)
    ) AS tipe
  FROM CONTRIBUTORS C;
"""

GET_CONTRIBUTORS_ALL = """
  SELECT 
    id, 
    nama, 
    kewarganegaraan, 
    IF(C.jenis_kelamin = 0, 'Laki-laki', 'Perempuan') AS jenis_kelamin,
    CONCAT_WS(', ', 
      IF(C.id IN (SELECT P.id FROM PEMAIN P), 'pemain', NULL),
      IF(C.id IN (SELECT S.id FROM SUTRADARA S), 'sutradara', NULL),
      IF(C.id IN (SELECT PS.id FROM PENULIS_SKENARIO PS), 'penulis_skenario', NULL)
    ) AS tipe
  FROM CONTRIBUTORS C;
  JOIN {table} ON C.id = {table}.id;
"""
