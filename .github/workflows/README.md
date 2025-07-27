# GitHub Actions Workflows Configuration
# This directory contains automated CI/CD workflows for the BDD test automation framework

## Available Workflows:

### 1. 🎯 BDD Test Automation (bdd-test-automation.yml)
- **Triggers**: Push to main/develop, Pull Requests, Daily schedule, Manual dispatch
- **Features**: 
  - Matrix testing across all test suites
  - Automated report generation
  - GitHub Pages deployment
  - Test result notifications
- **Artifacts**: Test reports, screenshots, HTML reports

### 2. 🚀 Quick CI (quick-ci.yml)  
- **Triggers**: Push/PR to main branch
- **Purpose**: Fast feedback for code changes
- **Scope**: Smoke tests only
- **Runtime**: ~2-3 minutes

### 3. 🎮 Manual Test Execution (manual-test.yml)
- **Triggers**: Manual workflow dispatch
- **Features**:
  - Configurable test suites
  - Browser mode selection (headless/headed)
  - MCP mode selection (simulation/real)
  - Environment selection
  - Automatic issue creation on failure

## Setup Requirements:

### Repository Settings:
1. Enable GitHub Actions in repository settings
2. Enable GitHub Pages (Settings > Pages > Source: GitHub Actions)
3. Set up branch protection rules (optional)

### Secrets (if needed):
- Add any required API keys or credentials to repository secrets
- Configure notification webhooks (optional)

## Usage:

### Automatic Runs:
- Every push to main/develop triggers full test suite
- Every PR triggers quick smoke tests
- Daily scheduled runs at 6 AM UTC

### Manual Runs:
- Go to Actions tab > Manual Test Execution > Run workflow
- Select test configuration and execute

### View Results:
- Test reports: https://[username].github.io/[repository-name]/
- Workflow runs: Repository Actions tab
- Artifacts: Download from completed workflow runs
