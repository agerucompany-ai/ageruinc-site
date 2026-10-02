#!/bin/zsh
# ビルドして gh-pages ブランチへ公開（GitHub Pages）
set -e
cd "$(dirname "$0")"
source ~/.github_env
T=${GITHUB_TOKEN:-$GH_TOKEN}
python3 build.py
cd public
rm -rf .git && git init -q -b gh-pages && git config user.name agerucompany-ai && git config user.email ageru.company@gmail.com
git add -A && git commit -qm "deploy $(date '+%Y-%m-%d %H:%M')"
git push -qf "https://x-access-token:$T@github.com/agerucompany-ai/ageruinc-site.git" gh-pages
rm -rf .git
echo "deployed"
