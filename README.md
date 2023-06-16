# Tokenizacja energii elektrycznej

## Założenia projektu</br>
* Opracowanie systemu z elementami sieci blockchain zamieniającego wyprodukowaną energię elektryczną na tokeny
* Anonimowa autentykacja użytkowników​
* Stworzenie aplikacji mobilnej​ dla użytkowników, która umożliwia zarządzanie portfelem, przelewanie tokenów innym użytkownikom, przegląd historii transakcji, udostępnianie identyfikatora generując kod QR, odbiór energii elektrycznej
* Dynamiczna zmiana wartości tokenów

## Uruchomienie aplikacji
### Instalacja bibliotek i uruchomienie serwera
* `pip install -r requirements.txt`</br>
* `cd app`</br>
* `python main.py`

### Wygenerowanie pliku APK do instalacji aplikacji w systemie operacyjnym Android
<i>Używając Android Stuido</i></br>
* `Build -> Build Bundle(s)/APK(s) -> Build APK(s)`</br>
* Zlokalizowanie pliku w folderze electricity-tokenization\mobileApp\app\build\outputs\apk\debug</br>
* Instalacja na telefonie z systemem Android


## Zrzuty ekranu z aplikacji mobilnej

### Rejestracja i logowanie
![image](https://github.com/majkelw/electricity-tokenization/assets/75738353/305371f6-2131-4a43-93f1-c86cb522c9a2)

### Portfel, kod QR, odbiór energii
![image](https://github.com/majkelw/electricity-tokenization/assets/75738353/55ad7eb8-f695-496e-b57b-8a1d1bd8796f)

### Transakcje
![image](https://github.com/majkelw/electricity-tokenization/assets/75738353/79ef5a7b-3b80-4ce2-9976-62ad3fbf3016)


