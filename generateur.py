# Liste des tâches
taches = [
    "Apprendre Python",
    "Créer une page HTML avec CSS",
    "Publier un projet sur GitHub",
    "Explorer Flask pour le développement web"
]

# Génération du contenu HTML
html_content = """
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ToDo List</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <h1>Ma ToDo List</h1>
    <ul>
"""

for tache in taches:
    html_content += f"<li>{tache}</li>\n"
    html_content += """
    </ul>
    <p>Page générée dynamiquement avec Python.</p>
</body>
</html>
"""

# Écriture dans un fichier HTML
with open("index.html", "w", encoding="utf-8") as file:
    file.write(html_content)

print("La page index.html a été générée avec succès !")
