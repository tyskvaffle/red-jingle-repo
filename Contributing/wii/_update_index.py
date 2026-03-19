import sys, json

if len(sys.argv) != 4:
    print("Usage: _update_index_wii.py <index.json path> <game title> <jingle path>")
    sys.exit(1)

index_path, game_title, jingle_path = sys.argv[1], sys.argv[2], sys.argv[3]

# Normalize path separators to forward slashes (for cross-platform consistency)
jingle_path = jingle_path.replace('\\', '/')

try:
    with open(index_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
except FileNotFoundError:
    data = {"name": "Red's Jingles Pack", "wii": []}

wii = data.get("wii", [])

# Remove any existing entry with the same file path (idempotent re-runs)
wii = [e for e in wii if e.get("file") != jingle_path]

wii.append({"name": game_title, "file": jingle_path})

# Sort alphabetically by game title (case-insensitive)
wii.sort(key=lambda e: e["name"].lower())

data["wii"] = wii

with open(index_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
    f.write('\n')

print(f"[index.json] Added: {game_title} -> {jingle_path}")
