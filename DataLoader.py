import os
import pandas as pd

_dataColumns = [
    'Date',
    'ApName',
    'NumOfUsers',
    'TransmittedFragments',  # liczba otrzymanych MSDU typu Data lub Management
    'MulticastTransmittedFrames',  # wysłąne MSDU z ustawionym bitem multicast
    'Retries',  # pomyślne przesłanie MSDU po jednej lub kilku ponownych próbach
    'MultipleRetries',  # pomyślne przesłane MSDU po więcej niż jednej ponownej próbach
    'FrameDuplicates',  # wystąpienia duplikatów przesyłąnych ramek
    'RtsSuccesses',
    'RtsFailures',
    'AckFailures',  # brak otrzymania ACK kiedy powinien zostać przesłany
    'ReceivedFragments',  # liczba otrzymanych MSDU typu Data lub Management
    'MulticastReceivedFrames',  # liczba otrzymanych MSDU z ustawionym bitem multicast
    'FcsErrors',  # liczba błędów FCS w przesyłanych MSDU
    'TransmittedFrames',  # pomyślnie przesłane MSDU
    'WepUndecryptables',
    'Failed',  # niepowodzenia w przesłaniu MSDU
    'RxUtilization',  # procent od 100 do 100 oznaczający jak długo receiver był zajęty przetwarzaniem pakietów
    'TxUtilization',  # procent od 0 do 100 oznaczający jak długo transmitter był zajęty przetwarzaniem pakietów
    'ChannelUtilization',  # oznacza przez jak długi czas kanał był zajęty
    'NumOfClients',  # liczba klientów podłączonych do AP
    'PoorSnrClients'  # podłączone urządzenia ze słabym sygnałem
]


def load_single_file(path):
    data = pd.read_csv(path, sep=';', header=None)
    expected_num_of_columns = 22
    actual_num_of_columns = len(data.columns)
    data.drop(
        data.iloc[:, expected_num_of_columns: actual_num_of_columns],
        inplace=True,
        axis=1
    )
    data.columns = _dataColumns
    return data


def load_from_folder(folder_path):
    data_arr = []
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        data = load_single_file(file_path)
        data_arr.append(data)
    return pd.concat(data_arr)
