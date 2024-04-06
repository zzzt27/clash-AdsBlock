import requests
from datetime import datetime
import re

# Daftar item yang akan diperbarui di README.md
items = [
    {
        "name": "oisd_small",
        "url": "https://small.oisd.nl/domainswild"
    },
    {
        "name": "oisd_big",
        "url": "https://big.oisd.nl/domainswild"
    },
    {
        "name": "oisd_nsfw🔞",
        "url": "https://nsfw.oisd.nl/domainswild"
    }
]

# Fungsi untuk mengambil informasi dari URL dan mempersiapkan string yang diperbarui
def update_readme_item(item):
    response = requests.get(item["url"])
    content = response.text

    entries_match = re.search(r"# Entries: (\d+)", content)
    last_modified_match = re.search(r"# Last modified: ([^\s]+)", content)

    if entries_match and last_modified_match:
        entries_count = entries_match.group(1)
        last_modified_str = last_modified_match.group(1)

        last_modified_dt = datetime.strptime(last_modified_str, "%Y-%m-%dT%H:%M:%S%z")
        formatted_last_modified = last_modified_dt.strftime("%Y-%m-%d")

        readme_update = f"[{item['name']}]({item['url']}) | **{formatted_last_modified}** | {entries_count}"

        return readme_update
    else:
        return None

# Membaca README.md dan memperbarui informasi untuk setiap item
with open('README.md', 'r') as file:
    readme_content = file.read()

updated_readme_content = readme_content

for item in items:
    update = update_readme_item(item)
    if update:
        # Mengganti bagian yang diperbarui di README.md
        updated_readme_content = re.sub(
            rf'\[{item["name"]}\]\({re.escape(item["url"])}\) \| \*\*[\d-]+\*\* \| \d+',
            update,
            updated_readme_content
        )

# Menulis kembali README.md dengan perubahan terbaru
with open('README.md', 'w') as file:
    file.write(updated_readme_content)

print("README.md telah diperbarui sukses!")
