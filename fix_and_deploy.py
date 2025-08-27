#!/usr/bin/env python3
"""
Script to commit and push the fixed GitHub Actions workflows
"""
import subprocess
import sys
import os

def run_command(command, cwd=None):
    """Run a shell command and return the result"""
    try:
        result = subprocess.run(
            command, 
            shell=True, 
            cwd=cwd, 
            capture_output=True, 
            text=True, 
            check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {command}")
        print(f"Error: {e.stderr}")
        return None

def main():
    # Get the script directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    print("🔧 Fixing GitHub Actions authentication issues...")
    
    # Add the changes
    print("📝 Staging changes...")
    if run_command("git add .", cwd=script_dir) is None:
        sys.exit(1)
    
    # Check if there are changes to commit
    status = run_command("git status --porcelain", cwd=script_dir)
    if not status:
        print("✅ No changes to commit.")
        return
    
    # Commit the changes
    print("💾 Committing changes...")
    commit_msg = "🔧 Fix GitHub Actions authentication issues\n\n- Replace METRICS_TOKEN with GITHUB_TOKEN in metrics workflow\n- Fix GH_TOKEN reference in update-readme workflow\n- Comment out WakaTime integration until API key is configured\n- Add proper permissions for workflows"
    
    if run_command(f'git commit -m "{commit_msg}"', cwd=script_dir) is None:
        sys.exit(1)
    
    # Push the changes
    print("🚀 Pushing changes to GitHub...")
    if run_command("git push", cwd=script_dir) is None:
        sys.exit(1)
    
    print("✅ Successfully fixed and deployed GitHub Actions workflows!")
    print("\n📋 What was fixed:")
    print("  • Replaced custom METRICS_TOKEN with built-in GITHUB_TOKEN")
    print("  • Fixed token reference in README update workflow")
    print("  • Temporarily disabled WakaTime integration")
    print("  • Added proper workflow permissions")
    print("\n🔄 Your workflows should now run without authentication errors!")

if __name__ == "__main__":
    main()
