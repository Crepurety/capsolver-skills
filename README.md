# CapSolver Skills

A collection of agent skills for [CapSolver](https://capsolver.com/) — automatically resolve captchas using AI. Compatible with [skills.sh](https://skills.sh) and `npx skills`.

## Installation

```bash
npx skills add Crepurety/capsolver-skills
```

## Setup

1. Install Python dependencies:

2. ```bash
   pip install -r requirements.txt
   ```

   2. Create a `.env` file from the example:
  
   3. ```bash
      cp .env.example .env
      ```

      3. Add your CapSolver API key to `.env`:
     
      4. ```
         API_KEY=CAP-XXXXX-your-api-key-here
         ```

         Get your API key from the [CapSolver Dashboard](https://dashboard.capsolver.com/).

         ## Supported Captcha Types

         ### Recognition Tasks

         | Task | Description |
         |------|-------------|
         | ImageToTextTask | Solve text-based captcha from images |
         | ReCaptchaV2Classification | Classify reCAPTCHA v2 images |
         | AwsWafClassification | Classify AWS WAF images |
         | VisionEngine | Advanced AI vision-based captcha solving |

         ### Token Tasks

         | Task | Description |
         |------|-------------|
         | GeeTest v3/v4 | Solve GeeTest captchas |
         | reCAPTCHA v2 | Solve Google reCAPTCHA v2 (checkbox/invisible) |
         | reCAPTCHA v3 | Solve Google reCAPTCHA v3 |
         | MTCaptcha | Solve MTCaptcha |
         | DataDome | Solve DataDome slider |
         | AWS WAF | Solve AWS WAF challenges |
         | Cloudflare Turnstile | Solve Cloudflare Turnstile |
         | Cloudflare Challenge | Solve Cloudflare 5-second shield |

         ## Quick Examples

         ```bash
         # Solve text captcha from image
         python3 ./scripts/solver.py ImageToTextTask --body "base64_image_data"

         # Solve reCAPTCHA v2
         python3 ./scripts/solver.py ReCaptchaV2TaskProxyLess --websiteURL "https://example.com" --websiteKey "site_key"

         # Solve Cloudflare Turnstile
         python3 ./scripts/solver.py AntiTurnstileTaskProxyLess --websiteURL "https://example.com" --websiteKey "site_key"

         # Solve Cloudflare Challenge
         python3 ./scripts/solver.py AntiCloudflareTask --websiteURL "https://example.com" --proxy "host:port:user:pass"
         ```

         ## Directory Structure

         ```
         capsolver-skills/
           scripts/
             solver.py          # CapSolver API client script
           SKILL.md             # Skill metadata for skills.sh
           README.md            # This file
           requirements.txt     # Python dependencies
           .env.example         # Example environment file
           LICENSE              # MIT License
         ```

         ## Resources

         - [CapSolver Documentation](https://docs.capsolver.com/)
         - - [CapSolver Dashboard](https://dashboard.capsolver.com/)
           - - [skills.sh Directory](https://skills.sh)
            
             - ## License
            
             - MIT
