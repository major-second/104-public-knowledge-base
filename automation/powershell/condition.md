- 前置[[powershell/var]]
```powershell
$x = 3; `
if ($x -lt 5) {
    Write-Output 0
}; `
if ($x -lt 5) {
    Write-Output 1
} else {
    Write-Output 2
}; `
if ($x -gt 5) {
    Write-Output 1
} elseif ($x -eq 3) {
    Write-Output 2
} else {
    Write-Output 3
}; `
$x = "abc"; `
switch ($x) {
    "ab" { Write-Output 1 }
    "abc" { Write-Output 3 }
    default { Write-Output 5 }
}
```