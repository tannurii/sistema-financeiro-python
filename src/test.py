
def filtrar_por_data(inicio):
    from datetime import datetime
    data_inicial = datetime.strptime(inicio, "%Y-%m-%d")
    print(data_inicial)

