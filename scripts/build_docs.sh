# inspired by https://github.com/pytorch/botorch/blob/master/scripts/build_docs.sh
# usage: poetry run bash scripts/build_docs.sh
echo "-----------------------------------"
echo "Convert .ipynb to markdown"
echo "-----------------------------------"
echo "-------------"
jupyter nbconvert --to markdown --execute README.ipynb
echo "-------------"
jupyter nbconvert --to markdown --execute website/docs/getting_started.ipynb
echo "-------------"
jupyter nbconvert --to markdown --execute website/docs/example.ipynb