#!/usr/bin/env python3

"""
Bootstrap script for Go template project.
Clones the template and prepares it for use as a new project.
"""

import argparse
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path


def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="Bootstrap a new Go project from templ-project/go template",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Bootstrap in current directory
  uvx --from git+https://github.com/templ-project/go.git bootstrap .

  # Bootstrap in specific directory
  uvx --from git+https://github.com/templ-project/go.git bootstrap ./my-go-project

  # Bootstrap with custom project name
  uvx --from git+https://github.com/templ-project/go.git bootstrap --project-name awesome-lib ./my-project

  # Show help
  uvx --from git+https://github.com/templ-project/go.git bootstrap --help
        """,
    )

    parser.add_argument(
        "path",
        nargs="?",
        default=".",
        help="Target directory (default: current directory)",
    )

    parser.add_argument(
        "--project-name",
        help="Project name (default: extracted from target directory name)",
    )

    return parser.parse_args()


def remove_if_exists(target_path):
    """Remove a directory or file if it exists."""
    if target_path.exists():
        if target_path.is_dir():
            shutil.rmtree(target_path)
        else:
            target_path.unlink()
        print(f"  ✓ Removed: {target_path.name}")


def extract_project_name(target_path):
    """Extract project name from target directory path."""
    # Get the directory name
    dir_name = Path(target_path).name

    # Handle current directory case
    if dir_name == "." or dir_name == "":
        dir_name = Path.cwd().name

    # Convert to a valid Go module name
    # Replace spaces and periods with hyphens, make lowercase
    project_name = (
        dir_name.replace(" ", "-").replace("_", "-").replace(".", "-").lower()
    )

    # Remove any non-alphanumeric characters except hyphens
    project_name = re.sub(r"[^a-z0-9-]", "", project_name)

    # Ensure it doesn't start or end with hyphens
    project_name = project_name.strip("-")

    # Go module names cannot start with numbers
    if project_name and project_name[0].isdigit():
        project_name = f"go-{project_name}"

    # Fallback to default if empty
    if not project_name:
        project_name = "go-template"

    return project_name


def update_go_mod_metadata(go_mod_path, project_name):
    """Update go.mod metadata for new project."""
    if not go_mod_path.exists():
        return

    with open(go_mod_path, "r") as f:
        content = f.read()

    # Update module path
    content = re.sub(
        r"module github\.com/templ-project/go",
        f"module github.com/your-org/{project_name}",
        content,
    )

    with open(go_mod_path, "w") as f:
        f.write(content)

    print("  ✓ Updated go.mod metadata")


def update_taskfile_metadata(taskfile_path, project_name):
    """Update Taskfile.yml metadata for new project."""
    if not taskfile_path.exists():
        return

    with open(taskfile_path, "r") as f:
        content = f.read()

    # Update GO_PROJECT_NAME variable default value
    content = re.sub(
        r'GO_PROJECT_NAME: \'{{default .GO_PROJECT_NAME "go-template"}}\'',
        f"GO_PROJECT_NAME: '{{{{default .GO_PROJECT_NAME \"{project_name}\"}}}}'",
        content,
    )

    with open(taskfile_path, "w") as f:
        f.write(content)

    print("  ✓ Updated Taskfile.yml metadata")


def update_readme_metadata(readme_path, project_name):
    """Update README.md for new project."""
    if not readme_path.exists():
        return

    with open(readme_path, "r") as f:
        content = f.read()

    # Create formatted project title
    project_title = project_name.replace("-", " ").replace("_", " ").title()

    # Update title and description
    content = re.sub(
        r"# Go Bootstrap Template",
        f"# {project_title}",
        content,
    )
    content = re.sub(
        r"> A modern Go project template with testing, linting, formatting, and quality tools built-in\.",
        f"> {project_title} - A Go project",
        content,
    )

    # Update repository references
    content = re.sub(
        r"https://github\.com/templ-project/go",
        f"https://github.com/your-org/{project_name}",
        content,
    )
    content = re.sub(
        r"git clone https://github\.com/templ-project/go\.git my-project",
        f"git clone https://github.com/your-org/{project_name}.git {project_name}",
        content,
    )

    # Update bootstrap examples
    content = re.sub(
        r"uvx --from git\+https://github\.com/templ-project/go\.git bootstrap \./my-go-project",
        f"uvx --from git+https://your-repo-url.git bootstrap ./{project_name}",
        content,
    )

    with open(readme_path, "w") as f:
        f.write(content)

    print("  ✓ Updated README.md metadata")


def update_contributing_metadata(contributing_path, project_name):
    """Update CONTRIBUTING.md for new project."""
    if not contributing_path.exists():
        return

    with open(contributing_path, "r") as f:
        content = f.read()

    # Update repository references
    content = re.sub(
        r"https://github\.com/templ-project/go",
        f"https://github.com/your-org/{project_name}",
        content,
    )
    content = re.sub(
        r"git clone https://github\.com/templ-project/go\.git",
        f"git clone https://github.com/your-org/{project_name}.git",
        content,
    )

    with open(contributing_path, "w") as f:
        f.write(content)

    print("  ✓ Updated CONTRIBUTING.md metadata")


def clone_template(target_path):
    """Clone the template repository to target directory."""
    print("📁 Cloning template repository...\n")

    # Ensure target directory exists
    target_path.mkdir(parents=True, exist_ok=True)

    # Check if directory is empty
    if any(target_path.iterdir()):
        print("❌ Error: Target directory is not empty")
        print(f"   Directory: {target_path}")
        print("   Please use an empty directory or remove existing files.")
        sys.exit(1)

    try:
        # Clone the repository
        print("  Cloning from https://github.com/templ-project/go...")
        subprocess.run(
            [
                "git",
                "clone",
                "--depth",
                "1",
                "https://github.com/templ-project/go.git",
                str(target_path),
            ],
            check=True,
            capture_output=True,
        )
        print(f"  ✓ Template cloned to {target_path}")
    except subprocess.CalledProcessError as e:
        print("❌ Error: Failed to clone repository")
        print(f"   {e}")
        print("\nPlease ensure:")
        print("  1. Git is installed and available in PATH")
        print("  2. You have internet connectivity")
        print("  3. You have access to https://github.com/templ-project/go")
        sys.exit(1)


def bootstrap(target_path, project_name=None):
    """Main bootstrap function."""
    print("\n🚀 Go Template Bootstrap\n")

    target_path = Path(target_path).resolve()

    # Extract project name from directory if not provided
    if project_name is None:
        project_name = extract_project_name(target_path)

    print(f"Project name: {project_name}")

    # Clone template repository to target directory
    clone_template(target_path)

    print("\n📦 Cleaning up template artifacts...\n")

    # Remove .git directory
    git_dir = target_path / ".git"
    remove_if_exists(git_dir)

    # Remove bootstrap script itself
    bootstrap_script = target_path / "bootstrap.py"
    remove_if_exists(bootstrap_script)

    # Remove _uvx_install directory
    install_dir = target_path / "_uvx_install"
    remove_if_exists(install_dir)

    # Remove legacy install directories if they exist
    old_install_dir = target_path / "_install"
    remove_if_exists(old_install_dir)
    legacy_install_dir = target_path / ".uvx-install"
    remove_if_exists(legacy_install_dir)

    # Remove pyproject.toml (bootstrap packaging file)
    pyproject_file = target_path / "pyproject.toml"
    remove_if_exists(pyproject_file)

    # Remove mise.lock file
    mise_lock = target_path / ".mise.lock"
    remove_if_exists(mise_lock)

    # Remove .cwai directory
    cwai_dir = target_path / ".cwai"
    remove_if_exists(cwai_dir)

    # Remove .github/prompts directory
    github_prompts_dir = target_path / ".github" / "prompts"
    remove_if_exists(github_prompts_dir)

    print(f"\n📝 Updating project metadata for '{project_name}'...\n")

    # Update project files with the project name
    update_go_mod_metadata(target_path / "go.mod", project_name)
    update_taskfile_metadata(target_path / "Taskfile.yml", project_name)
    update_readme_metadata(target_path / "README.md", project_name)
    update_contributing_metadata(target_path / "CONTRIBUTING.md", project_name)

    print("\n✨ Bootstrap complete!\n")
    print("Next steps:")
    print("  1. Install Go toolchain (if not already installed):")
    print("     mise install")
    print("     # OR download from: https://go.dev/dl/")
    print("  2. Build the project:")
    print("     go build ./...")
    print("     # OR using task:")
    print("     task build")
    print("  3. Run tests:")
    print("     go test ./...")
    print("     # OR using task with coverage:")
    print("     task test")
    print("  4. Check code quality:")
    print("     task validate")
    print("  5. Start coding!\n")


def main():
    """Entry point."""
    args = parse_args()
    bootstrap(args.path, args.project_name)


if __name__ == "__main__":
    main()
