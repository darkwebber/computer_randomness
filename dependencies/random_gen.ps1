param (
    [string]$f_name,
    [int]$n
)

for ($i = 1; $i -le $n; $i++) {
    if ($?) { g++ random_initializer.cpp -o random_initializer } ; 
    if ($?) { .\random_initializer| Out-File -FilePath $f_name -Append }
    $done = ($i/$n)*100
    Write-Progress -Activity "Generating $f_name" -Status "$done% done" -PercentComplete $done
}
Write-Host "$f_name generated"