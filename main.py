import subprocess

# Beispiel: ls-Kommando unter Linux/macOS oder dir-Kommando unter Windows ausführen
process = subprocess.Popen(["ls", "-l"], stdout=subprocess.PIPE, text=True)

# Warten, bis der Prozess abgeschlossen ist
process.wait()

# Ausgabe lesen
output, _ = process.communicate()

# Ausgabe anzeigen
print(output)

