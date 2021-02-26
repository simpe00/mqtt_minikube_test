#########################
# virtual enviroment
#########################
$TestVar = $(get-location).Path+"\venv\"
#echo $TestVar
if (-not (Test-Path $TestVar)) {
    Write-Output "creat virtual enviroment"
    python3 -m venv $TestVar
    Write-Output "venv: done"

    .\venv\Scripts\activate
    
    Write-Output "install python packages via pip"
    pip install -r requirements.txt
    Write-Output "installed packages"
} 
