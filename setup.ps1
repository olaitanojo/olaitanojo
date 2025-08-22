# GitHub Profile Automation Setup Script
# Run this script to set up your automated GitHub contribution reporting

Write-Host "🚀 GitHub Profile Automation Setup" -ForegroundColor Green
Write-Host "===================================" -ForegroundColor Green

# Get user information
$username = Read-Host "Enter your GitHub username"
$email = Read-Host "Enter your GitHub email"
$linkedinUsername = Read-Host "Enter your LinkedIn username (optional, press Enter to skip)"

Write-Host "`n📝 Configuring Git..." -ForegroundColor Yellow

# Configure Git if not already configured
git config --global user.name $username
git config --global user.email $email

Write-Host "✅ Git configuration updated" -ForegroundColor Green

# Update README.md with user's information
Write-Host "`n📄 Updating README.md template..." -ForegroundColor Yellow

$readmeContent = Get-Content "README.md" -Raw
$readmeContent = $readmeContent -replace "YOUR_USERNAME", $username
$readmeContent = $readmeContent -replace "YOUR_EMAIL", $email

if ($linkedinUsername) {
    $readmeContent = $readmeContent -replace "YOUR_LINKEDIN", $linkedinUsername
} else {
    # Remove LinkedIn badge if not provided
    $readmeContent = $readmeContent -replace '\[\!\[LinkedIn\].*\]\(.*\)', ''
}

Set-Content "README.md" $readmeContent

Write-Host "✅ README.md updated with your information" -ForegroundColor Green

# Update workflow files
Write-Host "`n🔧 Updating GitHub Actions workflows..." -ForegroundColor Yellow

$updateReadmeContent = Get-Content ".github/workflows/update-readme.yml" -Raw
$updateReadmeContent = $updateReadmeContent -replace "YOUR_USERNAME", $username
Set-Content ".github/workflows/update-readme.yml" $updateReadmeContent

$metricsContent = Get-Content ".github/workflows/metrics.yml" -Raw
$metricsContent = $metricsContent -replace "YOUR_USERNAME", $username
Set-Content ".github/workflows/metrics.yml" $metricsContent

Write-Host "✅ Workflow files updated" -ForegroundColor Green

# Initialize git repository
Write-Host "`n🔄 Initializing Git repository..." -ForegroundColor Yellow

git init
git add .
git commit -m "🎉 Initial commit: GitHub profile automation setup"

Write-Host "✅ Git repository initialized" -ForegroundColor Green

Write-Host "`n📋 Next Steps:" -ForegroundColor Cyan
Write-Host "=============" -ForegroundColor Cyan
Write-Host "1. Create a new GitHub repository named exactly: '$username'" -ForegroundColor White
Write-Host "2. Make sure the repository is PUBLIC" -ForegroundColor White
Write-Host "3. Push this code to your new repository:" -ForegroundColor White
Write-Host "   git remote add origin https://github.com/$username/$username.git" -ForegroundColor Gray
Write-Host "   git branch -M main" -ForegroundColor Gray
Write-Host "   git push -u origin main" -ForegroundColor Gray
Write-Host "`n4. Optional: Set up WakaTime integration for coding time tracking:" -ForegroundColor White
Write-Host "   - Sign up at https://wakatime.com" -ForegroundColor Gray
Write-Host "   - Get your API key from https://wakatime.com/settings/account" -ForegroundColor Gray
Write-Host "   - Add WAKATIME_API_KEY to your repository secrets" -ForegroundColor Gray
Write-Host "`n5. Create Personal Access Token for metrics:" -ForegroundColor White
Write-Host "   - Go to https://github.com/settings/tokens" -ForegroundColor Gray
Write-Host "   - Create a new token with 'repo' and 'user' permissions" -ForegroundColor Gray
Write-Host "   - Add it as METRICS_TOKEN in repository secrets" -ForegroundColor Gray
Write-Host "`n✨ Your GitHub profile will automatically update every 6 hours!" -ForegroundColor Green

# Ask if user wants to open GitHub
$openGitHub = Read-Host "`nWould you like to open GitHub in your browser to create the repository? (y/n)"
if ($openGitHub -eq "y" -or $openGitHub -eq "Y") {
    Start-Process "https://github.com/new"
}

Write-Host "`n🎯 Setup complete! Your automated GitHub profile is ready to go!" -ForegroundColor Green
