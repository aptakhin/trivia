
if [ -z "$1" ]
then
  echo "Usage: ./commit.sh <commit-prefix>"
  exit 1
fi

set -e

echo "Staged changes"
# git show staged file names only with modifications marked M, A or D and print modification
git diff --cached --name-status | grep -E '^[MAD]' | while read status file; do
  echo "$status $file"
done

# uv tool run ruff check --fix .
uv run pytest -s

# read the message interactivelyfrom typed input
echo "Enter commit message: "
read MESSAGE

# commit staged files with message
git commit -m "[$1] $MESSAGE"
