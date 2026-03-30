---
name: capsolver
description: Use CapSolver to automatically resolve Geetest, reCAPTCHA v2, reCAPTCHA v3, MTCaptcha, DataDome, AWS WAF, Cloudflare Turnstile, and Cloudflare Challenge captchas via API.
homepage: https://capsolver.com/
credentials:
  - API_KEY
env:
  required:
    - API_KEY
metadata:
  author: capsolver
  version: "1.0.0"
---

# CapSolver Skill

Use this skill to automatically resolve various CAPTCHA challenges using the CapSolver API service.

**Authentication:** Set `API_KEY` in your environment or in a `.env` file in the repo root. Get your key from the [CapSolver Dashboard](https://dashboard.capsolver.com/).

**Errors:** If it fails, the script will exit with code 1.

## Supported Captcha Types

### Task (Recognition)

- **ImageToTextTask** -- Solve text-based captcha from images
- **ReCaptchaV2Classification** -- Classify reCAPTCHA v2 images
- **AwsWafClassification** -- Classify AWS WAF images
- **VisionEngine** -- Advanced AI vision-based captcha solving

### Task (Token)

- **GeeTest** -- Solve GeeTest v3/v4
- **reCAPTCHA v2** -- Solve Google reCAPTCHA v2 (checkbox/invisible)
- **reCAPTCHA v3** -- Solve Google reCAPTCHA v3
- **MTCaptcha** -- Solve MTCaptcha
- **DataDome** -- Solve DataDome slider
- **AWS WAF** -- Solve AWS WAF challenges
- **Cloudflare Turnstile** -- Solve Cloudflare Turnstile
- **Cloudflare Challenge** -- Solve Cloudflare 5-second shield

## Usage

See the README for full usage examples, or run:

```bash
python3 ./scripts/solver.py --help
```

## Resources

- [CapSolver Docs](https://docs.capsolver.com/) -- Official documentation
