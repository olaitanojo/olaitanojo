# GitHub Actions Troubleshooting Guide

## 🚀 Quick Start

Your workflows should now work! Here's what was fixed and how to verify:

### ✅ What Was Fixed
1. **Authentication Issues** - Replaced custom tokens with `GITHUB_TOKEN`
2. **Permission Problems** - Added proper workflow permissions  
3. **Complex Configuration** - Simplified workflows for reliability
4. **Added Test Workflow** - Easy way to verify setup works

---

## 🔧 Troubleshooting Steps

### Step 1: Verify Repository Settings
Go to `https://github.com/olaitanojo/olaitanojo/settings/actions`

**Check these settings:**
- ✅ **Actions permissions**: "Allow all actions and reusable workflows"
- ✅ **Workflow permissions**: "Read and write permissions"  
- ✅ **Allow GitHub Actions to create and approve pull requests**: Enabled

### Step 2: Test Basic Functionality
1. Go to `https://github.com/olaitanojo/olaitanojo/actions`
2. Click "Test Workflow" 
3. Click "Run workflow" → "Run workflow"
4. Wait for it to complete (should show green ✅)

### Step 3: Run Metrics Generation
1. After test passes, click "GitHub Profile Metrics (Simple)"
2. Click "Run workflow" → "Run workflow"  
3. This will generate `github-metrics.svg` in your repository

---

## 🐛 Common Issues & Solutions

### Issue: "Bad credentials" Error
**Solution:** 
- Repository settings → Actions → General
- Set workflow permissions to "Read and write permissions"
- Ensure you're using `GITHUB_TOKEN`, not custom tokens

### Issue: Workflow doesn't trigger
**Solutions:**
1. Check if Actions are enabled in repository settings
2. Verify the workflow file is in `.github/workflows/`
3. Check YAML syntax with an online validator

### Issue: Permission denied
**Solutions:**
1. Add proper permissions to workflow:
   ```yaml
   permissions:
     contents: write
     actions: read
     metadata: read
   ```
2. Check repository settings allow write access

### Issue: Metrics action fails
**Solutions:**
1. Use the simplified `metrics-simple.yml` workflow
2. Verify your username in the workflow matches your GitHub username
3. Check if you have public repositories (private repos need special setup)

---

## 📝 Available Workflows

### 1. Test Workflow (`test.yml`)
- **Purpose**: Verify GitHub Actions work
- **When to use**: First thing to run when troubleshooting
- **What it does**: Basic checks, lists repo contents, tests permissions

### 2. GitHub Profile Metrics Simple (`metrics-simple.yml`) 
- **Purpose**: Generate GitHub profile statistics
- **Output**: `github-metrics.svg` file
- **Features**: Activity, languages, repository stats

### 3. Update README (`update-readme.yml`)
- **Purpose**: Add recent activity to README
- **Note**: WakaTime integration commented out (needs API key)

---

## 🔍 Debugging Commands

If workflows still fail, check these in your repository:

```bash
# Check workflow files exist
ls -la .github/workflows/

# Verify YAML syntax  
cat .github/workflows/test.yml

# Check repository permissions
git remote -v
```

---

## 🆘 Still Not Working?

1. **Run the Test Workflow first** - This will show if basic Actions work
2. **Check the Actions tab** - Look for specific error messages
3. **Repository Settings** - Verify Actions are enabled and have write permissions
4. **Branch Protection** - Make sure branch protection rules allow Actions to commit

### Manual Steps to Enable GitHub Actions:
1. Go to repository Settings
2. Scroll to "Actions" → "General"  
3. Select "Allow all actions and reusable workflows"
4. Under "Workflow permissions" select "Read and write permissions"
5. Save changes

---

## 📊 Expected Results

After successful runs:
- `github-metrics.svg` - Your profile statistics
- Updated README (if using update-readme workflow)
- Green checkmarks in Actions tab
- Automated daily updates via cron schedule

---

**Need more help?** Check the Actions logs in GitHub for specific error messages!
