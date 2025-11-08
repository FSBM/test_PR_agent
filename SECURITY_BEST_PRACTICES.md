# Security Best Practices for FSBM/test_PR_agent

## Overview

This document outlines security best practices for managing secrets and sensitive information in this repository.

## Secret Management

### ✅ DO:
- Use environment variables for all secrets, API keys, and credentials
- Store secrets in `.env` file locally (never commit this file)
- Use `.env.example` to document required environment variables
- Use secret management services in production (AWS Secrets Manager, HashiCorp Vault, etc.)
- Rotate secrets regularly
- Use different secrets for different environments (dev, staging, production)

### ❌ DON'T:
- Never hardcode secrets in source code
- Never commit `.env` files to git
- Never put secrets in comments (even if commented out)
- Never put secrets in configuration files that are committed
- Never share secrets via email, chat, or other insecure channels

## Setting Up Environment Variables

### Local Development

1. Copy the example environment file:
   ```bash
   cp .env.example .env
   ```

2. Edit `.env` and fill in your actual secret values:
   ```bash
   # .env
   PAYMENT_GATEWAY_KEY=actual-secret-key-here
   ```

3. Load environment variables in your code:
   ```python
   import os
   
   secret_key = os.getenv('PAYMENT_GATEWAY_KEY')
   ```

### Production Deployment

For production, use your platform's secret management:

- **AWS**: AWS Secrets Manager or Parameter Store
- **Azure**: Azure Key Vault
- **GCP**: Google Secret Manager
- **Heroku**: Config Vars
- **Docker**: Docker Secrets or environment variables

## Pre-commit Hooks

Install pre-commit hooks to prevent committing secrets:

```bash
# Install pre-commit
pip install pre-commit

# Install the hooks
pre-commit install

# Test the hooks
pre-commit run --all-files
```

## Tools for Secret Detection

### Recommended Tools:
- **detect-secrets**: https://github.com/Yelp/detect-secrets
- **git-secrets**: https://github.com/awslabs/git-secrets
- **truffleHog**: https://github.com/trufflesecurity/truffleHog
- **GitGuardian**: https://www.gitguardian.com/

### Installation Example (detect-secrets):
```bash
pip install detect-secrets
detect-secrets scan > .secrets.baseline
```

## What to Do If a Secret Is Committed

If you accidentally commit a secret:

1. **Immediately rotate the secret** - invalidate the old one and create a new one
2. **Remove it from the code** in a new commit
3. **Clean git history** to remove the secret:
   ```bash
   # Using BFG Repo-Cleaner
   java -jar bfg.jar --replace-text passwords.txt
   git reflog expire --expire=now --all
   git gc --prune=now --aggressive
   ```
4. **Force push** (coordinate with team):
   ```bash
   git push --force --all
   ```
5. **Notify your team** to re-clone the repository

## Code Review Checklist

Before approving a PR, verify:

- [ ] No hardcoded secrets or credentials
- [ ] No API keys or passwords in code
- [ ] No database connection strings with credentials
- [ ] No private keys or certificates
- [ ] Environment variables used for configuration
- [ ] `.env` is in `.gitignore`
- [ ] Secrets are not in comments
- [ ] No temporary debug credentials left in code

## Resources

- [OWASP Secrets Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html)
- [GitHub Secret Scanning](https://docs.github.com/en/code-security/secret-scanning)
- [12 Factor App - Config](https://12factor.net/config)

## Questions?

If you have questions about secret management or security practices, please contact the security team.

---

**Last Updated**: 2025-11-08
