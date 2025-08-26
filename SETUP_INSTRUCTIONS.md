# 🚀 GitHub Profile Automation Setup Instructions

This setup will create an automatically updating GitHub profile that displays your daily and monthly contribution activity, coding stats, and achievements.

## 📋 What You'll Get

- **📊 Real-time GitHub statistics**: Commits, PRs, issues, repositories
- **🔥 Contribution streaks**: Track your coding consistency
- **💻 Language usage**: Show your most-used programming languages
- **📈 Activity graphs**: Visual representation of your contributions
- **🏆 Achievement badges**: GitHub trophies and milestones
- **⏰ Coding time tracking**: Integration with WakaTime (optional)
- **🔄 Automatic updates**: Refreshed every 6 hours via GitHub Actions

## 🛠️ Setup Process

### Step 1: Run the Setup Script
```powershell
cd github-profile-setup
.\setup.ps1
```

The script will:
- Configure your Git settings
- Update all template files with your information
- Initialize a Git repository
- Prepare everything for deployment

### Step 2: Create GitHub Repository
1. Go to [GitHub](https://github.com/new)
2. Create a new **PUBLIC** repository
3. **IMPORTANT**: Name it exactly the same as your GitHub username
4. Do **NOT** initialize with README, .gitignore, or license (we have our own files)

### Step 3: Push Your Code
```bash
# Add your GitHub repository as remote
git remote add origin https://github.com/YOUR_USERNAME/YOUR_USERNAME.git

# Set main branch
git branch -M main

# Push to GitHub
git push -u origin main
```

### Step 4: Set Up Secrets (Optional but Recommended)

#### For Enhanced Metrics:
1. Go to your repository → Settings → Secrets and variables → Actions
2. Create these secrets:

**METRICS_TOKEN** (Required for detailed metrics):
- Go to [GitHub Personal Access Tokens](https://github.com/settings/tokens)
- Click "Generate new token (classic)"
- Select scopes: `repo`, `user`, `read:org`
- Copy the token and add it as `METRICS_TOKEN`

**WAKATIME_API_KEY** (Optional, for coding time tracking):
- Sign up at [WakaTime](https://wakatime.com)
- Install WakaTime plugin in your code editors
- Get your API key from [WakaTime Settings](https://wakatime.com/settings/account)
- Add it as `WAKATIME_API_KEY`

### Step 5: Verify Setup
1. Check your GitHub profile - you should see the README displaying
2. Go to Actions tab in your repository
3. The workflows should run automatically or you can trigger them manually

## 📊 Features Explained

### Automated Updates
- **Every 6 hours**: Recent activity updates
- **Daily**: Comprehensive metrics and achievements
- **On push**: Immediate updates when you push to main branch

### Statistics Included
- **GitHub Stats Card**: Commits, PRs, issues, stars
- **Streak Stats**: Current and longest streaks
- **Language Stats**: Most used languages with percentages
- **Contribution Graph**: Visual activity heatmap
- **Trophy Case**: GitHub achievements and milestones
- **Recent Activity**: Latest commits, PRs, and issues

### Visual Elements
- **Snake Animation**: Shows your contribution pattern
- **Activity Graphs**: Multiple chart types
- **Progress Bars**: Language usage breakdown
- **Badges**: Social links and stats

## 🎨 Customization Options

### Themes
You can change themes in the URLs:
- `theme=dark` (default)
- `theme=radical`
- `theme=merko`
- `theme=gruvbox`
- `theme=tokyonight`

### Language Filters
Edit the workflows to include/exclude languages:
```yaml
plugin_languages_ignored: >-
  html, css, tex, less, dockerfile, makefile
```

### Update Frequency
Change the cron schedule in workflows:
```yaml
schedule:
  - cron: '0 */6 * * *'  # Every 6 hours
  - cron: '0 0 * * *'    # Daily
```

## 🔧 Troubleshooting

### Common Issues

**README not showing on profile:**
- Make sure repository name exactly matches your username
- Repository must be PUBLIC
- README.md must be in root directory

**Workflows not running:**
- Check if GitHub Actions are enabled in repository settings
- Verify secrets are properly configured
- Check Actions tab for error messages

**Stats not updating:**
- Wait up to 24 hours for first update
- Check if GITHUB_TOKEN has proper permissions
- Manually trigger workflow from Actions tab

**WakaTime not working:**
- Verify API key is correct
- Make sure WakaTime plugin is installed in your editors
- Check that you have coding activity in the past week

### Manual Updates
You can manually trigger updates:
1. Go to Actions tab in your repository
2. Select the workflow you want to run
3. Click "Run workflow"

## 📱 Mobile Optimization
The profile is optimized for both desktop and mobile viewing with responsive design elements.

## 🔒 Privacy & Security
- All tokens are stored securely in GitHub Secrets
- Only public repository information is displayed
- Private repository stats require explicit permission

## 🎯 Next Steps
1. **Customize the content**: Edit README.md to reflect your personality
2. **Add projects**: Pin your best repositories
3. **Join communities**: Contribute to open source projects
4. **Track progress**: Monitor your stats regularly
5. **Share your profile**: Show off your automated GitHub presence!

---

🎉 **Congratulations!** Your GitHub profile will now automatically showcase your development activity and achievements!

For questions or issues, check the GitHub Actions logs or create an issue in your repository.
