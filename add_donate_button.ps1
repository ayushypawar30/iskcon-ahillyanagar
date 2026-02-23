$files = Get-ChildItem -Path "c:\Users\intel\.gemini\antigravity\scratch\iskcon-ahillyanagar" -Filter "*.html"

foreach ($file in $files) {
    if ($file.Name -ne "index.html") {
        $content = Get-Content $file.FullName -Raw
        
        # Check if button acts already to avoid duplication
        if ($content -notmatch "btn-donate") {
            # Regex to find the Contact link and append Donate link
            $content = $content -replace '<li><a href="contact.html">Contact</a></li>', '<li><a href="contact.html">Contact</a></li>
                <li><a href="donation.html" class="btn-donate">Donate</a></li>'
            
            Set-Content -Path $file.FullName -Value $content
        }
    }
}
Write-Host "Donate button added to all HTML files."
