$files = Get-ChildItem -Path "c:\Users\intel\.gemini\antigravity\scratch\iskcon-ahillyanagar" -Filter "*.html"

foreach ($file in $files) {
    if ($file.Name -ne "store.html" -and $file.Name -ne "index.html") { # store and index might be handled manual or strict, let's include all actually
    }
    
    $content = Get-Content $file.FullName -Raw
    
    # 1. Remove margin: 0 auto; from nav-links to respect flex gap
    $content = $content -replace 'style="margin: 0 auto;"', ''
    
    # 2. Force Founder Acharya text to one line
    # Regex to find the div and add white-space: nowrap
    $content = $content -replace 'font-weight: 600;">\s+Founder Acharya\s+</div>', 'font-weight: 600; white-space: nowrap;">Founder Acharya</div>'
    
    Set-Content -Path $file.FullName -Value $content
}
Write-Host "Navbar styles cleaned and text fixed."
