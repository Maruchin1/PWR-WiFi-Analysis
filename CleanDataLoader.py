import os
import pandas as pd

dataColumns = [
    'Day',
    'Hour',
    'Minute',
    'ApName',
    'NumOfClients',  # liczba klientów podłączonych do AP
    'TransmittedFrames',  # pomyślnie przesłane MSDU
    'ChannelUtilization',  # oznacza przez jak długi czas kanał był zajęty
    'PoorSnrClients',  # podłączone urządzenia ze słabym sygnałem
    'Retries',  # pomyślne przesłanie MSDU po jednej lub kilku ponownych próbach
    'MultipleRetries',  # pomyślne przesłane MSDU po więcej niż jednej ponownej próbach
    'FrameDuplicates',  # wystąpienia duplikatów przesyłanych ramek
    'Failed',  # niepowodzenia w przesłaniu MSDU
    'FcsErrors',  # liczba błędów FCS w przesyłanych MSDU
    'AckFailures',  # brak otrzymania ACK kiedy powinien zostać przesłany
]


def loadFile(path):
    data = pd.read_csv(path, sep=',')
    return data


def loadFolder(path):
    data_arr = []
    for file_name in os.listdir(path):
        file_path = os.path.join(path, file_name)
        data = loadFile(file_path)
        data_arr.append(data)
    return pd.concat(data_arr)
