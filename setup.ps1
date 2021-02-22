#########################
# virtual enviroment
#########################
$TestVar = $(get-location).Path+"\venv"
#echo $TestVar
if (-not (Test-Path $TestVar)) {
    echo "creat virtual enviroment"
    python3 -m venv $TestVar
    echo "venv: done"

    .\venv\Scripts\activate
    
    echo "install python packages via pip"
    pip install elasticsearch
    pip install pandas
    echo "installed packages"
} 

"
astroid           2.4.2
certifi           2020.12.5
colorama          0.4.4
elasticsearch     7.11.0
isort             5.7.0
lazy-object-proxy 1.4.3
mccabe            0.6.1
numpy             1.20.1
pandas            1.2.2
pip               20.2.3
pylint            2.6.0
python-dateutil   2.8.1
pytz              2021.1
setuptools        49.2.1
six               1.15.0
toml              0.10.2
urllib3           1.26.3
wrapt             1.12.1"