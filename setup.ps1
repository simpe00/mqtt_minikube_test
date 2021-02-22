#########################
# virtual enviroment
#########################
$TestVar = $(get-location).Path+"\venv\"
#echo $TestVar
if (-not (Test-Path $TestVar)) {
    echo "creat virtual enviroment"
    python3 -m venv $TestVar
    echo "venv: done"

    .\venv\Scripts\activate
    
    echo "install python packages via pip"
    pip install -r requirements.txt
    echo "installed packages"
} 
