import requests
import matplotlib.pyplot as plt
from github import Github
import os

# Твой GitHub-токен
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
USERNAME = "ТВОЙ_ЮЗЕРНЕЙМ"  # Замени на свой GitHub username

g = Github(GITHUB_TOKEN)
user = g.get_user(USERNAME)

# Получаем список репозиториев и языков
repos = user.get_repos()
lang_stats = {}

for repo in repos:
    langs = repo.get_languages()
    for lang, count in langs.items():
        lang_stats[lang] = lang_stats.get(lang, 0) + count

# Строим график
plt.figure(figsize=(8, 5))
plt.bar(lang_stats.keys(), lang_stats.values(), color="skyblue")
plt.xlabel("Языки программирования")
plt.ylabel("Строк кода")
plt.title(f"Языки, используемые {USERNAME}")
plt.xticks(rotation=45)
plt.tight_layout()

# Сохраняем картинку
plt.savefig("stats.png")
