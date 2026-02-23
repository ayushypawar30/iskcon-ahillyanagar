$files = Get-ChildItem -Path "c:\Users\intel\.gemini\antigravity\scratch\iskcon-ahillyanagar" -Filter "*.html"

foreach ($file in $files) {
    $content = Get-Content $file.FullName -Raw
    
    # Replace Image Height
    $content = $content -replace 'style="height: 85px;', 'style="height: 50px;'
    
    # Replace Text and Style
    # Using regex to capture the div style and content
    $content = $content -replace 'font-size: 0.75rem; color: var\(--text-color\); margin-top: 5px; font-weight: 600; line-height: 1.2;">\s+Founder Acharya:<br>\s+A.C. Bhaktivedanta Swami Prabhupada', 'font-size: 0.8rem; color: var(--text-color); margin-top: 5px; font-weight: 600;">
                        Founder Acharya'
                        
    Set-Content -Path $file.FullName -Value $content
}
Write-Host "Navbar updated in all HTML files."
