param (

    [int]$n1,
    [int]$n2
)

$pythonVisualizer = "python_visualizer/results.py"

[string]$f_name1 = "random$n1.csv"
[string]$f_name2 = "random$n2.csv"

$csvChildern = Get-ChildItem -Path "./*.csv" -Name
foreach($file in $csvChildern){
    if($file -ne $f_name1 -and $file -ne $f_name2)
    {
        Remove-Item -Path $file
    }
};
if(Test-Path -Path $f_name1) {Clear-Content $f_name1};
if ($?) { .\dependencies\random_gen.ps1 -f_name $f_name1 -n $n1 };
if(Test-Path -Path $f_name2) {Clear-Content $f_name2};
if ($?) { .\dependencies\random_gen.ps1 -f_name $f_name2 -n $n2 }

if ($?) {python $pythonVisualizer $f_name1 $f_name2}


