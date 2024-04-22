export environment=local
echo $environment

mkdir tmp
mkdir outputs
mkdir logs

source venv/bin/activate

pip install -r requirements.txt

python main.py

