# How to Release a New Version

This document describes the step-by-step process to release a new version of UVP to PyPI.

## Release Process

1. **Update Version**

   - Update the version in `pyproject.toml`
   - The version follows semantic versioning (e.g., 0.0.1 → 0.0.2)

2. **Update CHANGELOG.md**

   - Add a new section for the new version
   - Document all significant changes, new features, and bug fixes
   - Use the format:

     ```
     ## [0.0.2] - YYYY-MM-DD
     ### Added
     - New feature descriptions

     ### Changed
     - Changes to existing functionality

     ### Fixed
     - Bug fixes
     ```

3. **Commit Changes**

   ```bash
   git add pyproject.toml CHANGELOG.md
   git commit -m "chore: bump version to 0.0.2"
   ```

4. **Create and Push Git Tag**

   ```bash
   git tag v0.0.2
   git push origin main v0.0.2
   ```

5. **Create GitHub Release**

   - Go to the GitHub repository's "Releases" section
   - Click "Create a new release"
   - Choose the tag you just pushed (v0.0.2)
   - Title: "v0.0.2"
   - Description: Copy the relevant section from CHANGELOG.md
   - **IMPORTANT**: Click "Publish release" (not "Save as draft")

   > ⚠️ The PyPI release workflow will only trigger automatically when you publish a proper GitHub
   > Release. Just pushing a tag is not enough!

6. **Verify Release**
   - Check the "Actions" tab on GitHub to ensure the publish workflow started automatically
   - Once completed, verify the new version is available on PyPI: https://pypi.org/p/uvp

## Troubleshooting

If the workflow doesn't trigger automatically:

1. Ensure you clicked "Publish release" and not "Save as draft"
2. Ensure the release tag matches exactly with your version number
3. As a last resort, you can manually trigger the workflow from the Actions tab

Remember: The release process is automated, and manual workflow runs should not be necessary if you
follow these steps carefully.
