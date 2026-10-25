source /root/miniconda-24/etc/profile.d/conda.sh
conda activate notion

python -m PyInstaller --noconfirm --onefile --name notion-sync \
  --paths ./src \
  --add-data "./src/notion_workspace/dota/dict/heroes.csv:notion_workspace/dota/dict" \
  --collect-data tzdata \
  ./src/notion_workspace/main.py

install -m 755 ./dist/notion-sync /usr/local/bin/notion-sync
