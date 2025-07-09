import re
from pathlib import Path

def calcular_progreso(readme_file: str = "README.md"):
    readme_path = Path(readme_file)
    if not readme_path.exists():
        print("❌ README.md no encontrado.")
        return

    with readme_path.open(encoding="utf-8") as f:
        content = f.read()

    sections = re.findall(r"### 🛠️ To implement[\s\S]+?---", content)
    implemented_counts = [len(re.findall(r"- \[`", sec)) for sec in content.split("### 🛠️ To implement")[:-1]]
    todo_counts = [len(re.findall(r"- \[ \]", sec)) for sec in sections]
    titles = re.findall(r"## \[[^\] ]+ ([^\]]+)\]", content)

    print("| Category                | ✅ Done | 🛠️ To Do | 📊 Progress |")
    print("|-------------------------|--------:|----------:|-------------:|")

    total_done = total_todo = 0
    for title, done, todo in zip(titles, implemented_counts, todo_counts):
        total = done + todo
        percent = round(100 * done / total) if total else 0
        bar = "█" * (percent // 10) + "░" * (10 - percent // 10)
        print(f"| {title:<24} | {done:>6} | {todo:>8} | {bar} {percent}% |")
        total_done += done
        total_todo += todo

    total_all = total_done + total_todo
    total_percent = round(100 * total_done / total_all)
    bar_total = "█" * (total_percent // 10) + "░" * (10 - total_percent // 10)
    print(f"| **Total**               | {total_done:>6} | {total_todo:>8} | {bar_total} {total_percent}% |")

if __name__ == "__main__":
    calcular_progreso()
