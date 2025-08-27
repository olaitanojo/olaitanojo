#!/usr/bin/env python3
"""
Deploy new simplified GitHub Actions workflows
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
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    print("🚀 Deploying new GitHub Actions workflows...")
    
    # Add changes
    print("📝 Adding new workflow files...")
    if run_command("git add .", cwd=script_dir) is None:
        sys.exit(1)
    
    # Check if there are changes to commit
    status = run_command("git status --porcelain", cwd=script_dir)
    if not status:
        print("✅ No changes to commit.")
        return
    
    print("📋 Changes to be committed:")
    print(status)
    
    # Commit changes
    print("\n💾 Committing new workflows...")
    commit_msg = """🔧 Add simplified GitHub Actions workflows

- Add metrics-simple.yml with better error handling
- Add test.yml for debugging GitHub Actions setup  
- Disable original metrics.yml temporarily
- Improved permissions and reliability"""
    
    if run_command(f'git commit -m "{commit_msg}"', cwd=script_dir) is None:
        sys.exit(1)
    
    # Push changes
    print("🚀 Pushing to GitHub...")
    if run_command("git push", cwd=script_dir) is None:
        sys.exit(1)
    
    print("\n✅ New workflows deployed successfully!")
    print("\n📋 What was added:")
    print("  • metrics-simple.yml - Simplified metrics generation")
    print("  • test.yml - Basic workflow to verify Actions work")
    print("  • Disabled original metrics workflow temporarily")
    
    print("\n🔍 Next Steps:")
    print("  1. Go to https://github.com/olaitanojo/olaitanojo/actions")
    print("  2. Run the 'Test Workflow' manually to verify setup")
    print("  3. If test passes, run 'GitHub Profile Metrics (Simple)'")
    print("  4. Check repository settings > Actions > General")
    print("     - Ensure 'Allow all actions and reusable workflows' is enabled")
    print("     - Workflow permissions should be 'Read and write permissions'")

if __name__ == "__main__":
    main()
