import sqlite3

# Crear base de datos y tabla
conn = sqlite3.connect('sprint1/data/network_traffic.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS traffic
             (protocol TEXT, src_addr TEXT, src_port INTEGER, dst_addr TEXT, dst_port INTEGER)''')

# Función para almacenar paquetes en la base de datos
def store_packet(packet):
    try:
        protocol = packet['protocol']
        src_addr = packet['src_addr']
        src_port = packet['src_port']
        dst_addr = packet['dst_addr']
        dst_port = packet['dst_port']
        c.execute("INSERT INTO traffic (protocol, src_addr, src_port, dst_addr, dst_port) VALUES (?, ?, ?, ?, ?)",
                  (protocol, src_addr, src_port, dst_addr, dst_port))
        conn.commit()
        print(f"Stored packet: {protocol} {src_addr}:{src_port} -> {dst_addr}:{dst_port}")
    except AttributeError as e:
        print(f"Packet skipped: {e}")

# Almacenar los datos analizados
for index, row in df_packets.iterrows():
    store_packet(row)

# Verificar los datos almacenados
df = pd.read_sql_query("SELECT * FROM traffic", conn)
print(df)

# Mostrar los datos en Jupyter Notebook
display(df.head())

# Cerrar la conexión a la base de datos
conn.close()
