echo "Instalando dependências..."


if [ ! -d "venv" ]; then
    echo "Criando ambiente virtual..."
    python3 -m venv venv
fi

source /venv/bin/activate

pip install -r requirements.txt
pip install -q git+https://github.com/Olavo-B/LoadDataset

