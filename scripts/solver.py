#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Discover seamless automatic captcha solving with capsolver
AI-powered Auto Web Unblock technology!
Supports automatic resolution of Geetest, reCAPTCHA v2, reCAPTCHA v3,
MTCaptcha, DataDome, AWS WAF, Cloudflare Turnstile, and Cloudflare Challenge, etc.
"""

import os
import sys
import json
import time
import argparse
from typing import Optional, Dict, Any

import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class CapSolver:
      SUPPORTED_TYPES = [
                # Task(Recognition)
          'ImageToTextTask',
                'ReCaptchaV2Classification',
                'AwsWafClassification',
                'VisionEngine',
                # Task(Token)
                'GeeTestTaskProxyLess',
                'ReCaptchaV2TaskProxyLess',
                'ReCaptchaV2EnterpriseTask',
                'ReCaptchaV2EnterpriseTaskProxyLess',
                'ReCaptchaV3Task',
                'ReCaptchaV3TaskProxyLess',
                'ReCaptchaV3EnterpriseTask',
                'ReCaptchaV3EnterpriseTaskProxyLess',
                'MtCaptchaTask',
                'MtCaptchaTaskProxyLess',
                'DatadomeSliderTask',
                'AntiAwsWafTask',
                'AntiAwsWafTaskProxyLess',
                'AntiTurnstileTaskProxyLess',
                'AntiCloudflareTask',
      ]

    def __init__(self, api_key: Optional[str] = None):
              self.api_key = api_key or os.getenv('API_KEY')
              if not self.api_key:
                            raise ValueError(
                                              'API key not found. Please set API_KEY in .env file or environment variable.'
                            )
                        self.api_base = 'https://api.capsolver.com'
        self.create_task_endpoint = '/createTask'
        self.get_task_result_endpoint = '/getTaskResult'
        self.get_balance_endpoint = '/getBalance'
        self.timeout = 60
        self.interval = 1
        self.create_task_payload = {
                      'source': 'capsolver-skill',
                      'clientKey': self.api_key,
                      'task': {}
        }
        self.get_task_result_payload = {
                      'source': 'capsolver-skill',
                      'clientKey': self.api_key,
                      'taskId': ''
        }
        self.headers = {
                      'Content-Type': 'application/json',
        }

    def check_type(self, _type: str) -> bool:
              return _type in self.SUPPORTED_TYPES

    def solve(self, args: argparse.Namespace) -> Dict[str, Any]:
              if not self.check_type(args.command):
                            raise ValueError(f"Unsupported type: {args.command}. Supported: {', '.join(self.SUPPORTED_TYPES)}")
                        self.build_task_payload(args)
        task_id, solution = self.create_task()
        if solution is not None:
                      return solution
                  return self.get_result(
                                task_id=task_id,
                                max_retries=args.max_retries
                  )

    def build_task_payload(self, args: argparse.Namespace):
              if args.command == 'ImageToTextTask':
                            if args.module == 'common' and args.body is None:
                                              raise ValueError('Body cannot be empty')
                                          if args.module == 'number' and args.images is None:
                                                            raise ValueError('Images cannot be empty')
                                                        self.create_task_payload['task'] = {
                                                                          'type': args.command,
                                                                          'websiteURL': args.websiteURL,
                                                                          'body': args.body,
                                                                          'images': args.images,
                                                                          'module': args.module
                                                        }
elif args.command == 'ReCaptchaV2Classification':
            self.create_task_payload['task'] = {
                              'type': args.command,
                              'websiteURL': args.websiteURL,
                              'image': args.image,
                              'question': args.question
            }
elif args.command == 'AwsWafClassification':
            self.create_task_payload['task'] = {
                              'type': args.command,
                              'websiteURL': args.websiteURL,
                              'images': args.images,
                              'question': args.question
            }
elif args.command == 'VisionEngine':
            self.create_task_payload['task'] = {
                              'type': args.command,
                              'websiteURL': args.websiteURL,
                              'module': args.module,
                              'image': args.image,
                              'imageBackground': args.imageBackground,
                              'question': args.question
            }
elif args.command == 'GeeTestTaskProxyLess':
            self.create_task_payload['task'] = {
                              'type': args.command,
                              'websiteURL': args.websiteURL,
                              'gt': args.gt,
                              'challenge': args.challenge,
                              'captchaId': args.captchaId,
                              'geetestApiServerSubdomain': args.geetestApiServerSubdomain
            }
elif 'ReCaptchaV2' in args.command:
            if args.command == 'ReCaptchaV2EnterpriseTask' and args.proxy is None:
                              raise ValueError('Proxy cannot be empty')
                          self.create_task_payload['task'] = {
                                            'type': args.command,
                                            'websiteURL': args.websiteURL,
                                            'websiteKey': args.websiteKey,
                                            'proxy': args.proxy,
                                            'pageAction': args.pageAction,
                                            'enterprisePayload': args.enterprisePayload,
                                            'isInvisible': args.isInvisible,
                                            'isSession': args.isSession
                          }
elif 'ReCaptchaV3' in args.command:
            if (args.command == 'ReCaptchaV3Task' or args.command == 'ReCaptchaV3EnterpriseTask') and args.proxy is None:
                              raise ValueError('Proxy cannot be empty')
                          self.create_task_payload['task'] = {
                                            'type': args.command,
                                            'websiteURL': args.websiteURL,
                                            'websiteKey': args.websiteKey,
                                            'proxy': args.proxy,
                                            'pageAction': args.pageAction,
                                            'enterprisePayload': args.enterprisePayload,
                                            'isSession': args.isSession
                          }
elif 'MtCaptchaTask' in args.command:
            if args.command == 'MtCaptchaTask' and args.proxy is None:
                              raise ValueError('Proxy cannot be empty')
                          self.create_task_payload['task'] = {
                                            'type': args.command,
                                            'websiteURL': args.websiteURL,
                                            'websiteKey': args.websiteKey,
                                            'proxy': args.proxy
                          }
elif args.command == 'DatadomeSliderTask':
            self.create_task_payload['task'] = {
                              'type': args.command,
                              'captchaUrl': args.captchaUrl,
                              'userAgent': args.userAgent,
                              'proxy': args.proxy
            }
elif 'AntiAwsWafTask' in args.command:
            if args.command == 'AntiAwsWafTask' and args.proxy is None:
                              raise ValueError('Proxy cannot be empty')
                          self.create_task_payload['task'] = {
                                            'type': args.command,
                                            'websiteURL': args.websiteURL,
                                            'proxy': args.proxy,
                                            'awsKey': args.awsKey,
                                            'awsIv': args.awsIv,
                                            'awsContext': args.awsContext,
                                            'awsChallengeJS': args.awsChallengeJS,
                                            'awsApiJs': args.awsApiJs,
                                            'awsProblemUrl': args.awsProblemUrl,
                                            'awsApiKey': args.awsApiKey,
                                            'awsExistingToken': args.awsExistingToken
                          }
elif args.command == 'AntiTurnstileTaskProxyLess':
            self.create_task_payload['task'] = {
                              'type': args.command,
                              'websiteURL': args.websiteURL,
                              'websiteKey': args.websiteKey,
                              'metadata': {
                                                    'action': args.action,
                                                    'cdata': args.cdata,
                              }
            }
elif args.command == 'AntiCloudflareTask':
            if args.proxy is None:
                              raise ValueError('Proxy cannot be empty')
                          self.create_task_payload['task'] = {
                                            'type': args.command,
                                            'websiteURL': args.websiteURL,
                                            'userAgent': args.userAgent,
                                            'html': args.html,
                                            'proxy': args.proxy
                          }
else:
            raise TypeError(f"Unsupported type: {args.command}")

    def create_task(self) -> tuple[str, Any]:
              response = requests.post(
                            f"{self.api_base}{self.create_task_endpoint}",
                            headers=self.headers,
                            json=self.create_task_payload,
                            timeout=self.timeout
              )
        if response.status_code == 200:
                      result = response.json()
            task_id = result.get("taskId")
            status = result.get('status')
            if not task_id:
                              raise RuntimeError(f"Failed to create task, get taskId failed: {response.text}")
                          if status == 'ready':
                                            return task_id, result.get('solution')
                                        return task_id, None
        if response.status_code == 400:
                      result = response.json()
            error_description = result.get("errorDescription")
            raise ValueError(f"Failed to create task, invalid task: {error_description}")
        if response.status_code == 401:
                      result = response.json()
            error_description = result.get("errorDescription")
            raise RuntimeError(f"Failed to create task, authentication failed: {error_description}")
else:
            raise RuntimeError(f"Failed to create task, unexpected error {response.status_code}: {response.text}")

    def get_result(self, task_id: str, max_retries: int = 30) -> Dict[str, Any]:
              for attempt in range(1, max_retries + 1):
                            result = self.get_task_result(task_id)
            if result is not None:
                              return result
                          if attempt < max_retries:
                                            print(f"Task {task_id} still pending, waiting {self.interval} seconds")
                                            time.sleep(self.interval)
                                    raise TimeoutError(f"Get task result failed after {max_retries} attempts.")

    def get_task_result(self, task_id: str) -> Optional[Dict[str, Any]]:
              self.get_task_result_payload['taskId'] = task_id
        response = requests.post(
                      f"{self.api_base}{self.get_task_result_endpoint}",
                      headers=self.headers,
                      json=self.get_task_result_payload,
                      timeout=self.timeout
        )
        if response.status_code == 200:
                      result = response.json()
            status = result.get('status')
            if status == 'ready':
                              return result.get('solution')
elif status in ['idle', 'processing']:
                return None
elif status == 'failed':
                raise RuntimeError(f"Get task result failed: {result}")
elif response.status_code == 400:
            result = response.json()
            error_description = result.get("errorDescription")
            raise ValueError(f"Failed to get task result, invalid task: {error_description}")
else:
            raise RuntimeError(f"Unexpected status code {response.status_code}")
        return None


def main():
      parser = argparse.ArgumentParser(
                description='CapSolver - AI-powered automatic captcha solving',
                formatter_class=argparse.RawDescriptionHelpFormatter,
      )
    subparsers = parser.add_subparsers(dest='command', help='Available commands')

    # ImageToTextTask
    p = subparsers.add_parser('ImageToTextTask', help='Solve text-based captcha')
    p.add_argument('-u', '--websiteURL', required=False)
    p.add_argument('-b', '--body', required=False)
    p.add_argument('-i', '--images', nargs='+', required=False)
    p.add_argument('-m', '--module', default='common', required=False)
    p.add_argument('-r', '--max-retries', type=int, default=60)

    # ReCaptchaV2Classification
    p = subparsers.add_parser('ReCaptchaV2Classification', help='Classify reCAPTCHA v2 images')
    p.add_argument('-u', '--websiteURL', required=False)
    p.add_argument('-k', '--websiteKey', required=False)
    p.add_argument('-q', '--question', required=True)
    p.add_argument('-i', '--image', required=True)
    p.add_argument('-r', '--max-retries', type=int, default=60)

    # AwsWafClassification
    p = subparsers.add_parser('AwsWafClassification', help='Classify AWS WAF images')
    p.add_argument('-u', '--websiteURL', required=False)
    p.add_argument('-q', '--question', required=True)
    p.add_argument('-i', '--images', nargs='+', required=True)
    p.add_argument('-r', '--max-retries', type=int, default=60)

    # VisionEngine
    p = subparsers.add_parser('VisionEngine', help='Advanced AI vision-based captcha solving')
    p.add_argument('-u', '--websiteURL', required=False)
    p.add_argument('-m', '--module', required=True)
    p.add_argument('-q', '--question', required=False)
    p.add_argument('-i', '--image', required=True)
    p.add_argument('-b', '--imageBackground', required=False)
    p.add_argument('-r', '--max-retries', type=int, default=60)

    # GeeTestTaskProxyLess
    p = subparsers.add_parser('GeeTestTaskProxyLess', help='Solve GeeTest captcha (v3/v4)')
    p.add_argument('-u', '--websiteURL', required=True)
    p.add_argument('-g', '--gt', required=False)
    p.add_argument('-c', '--challenge', required=False)
    p.add_argument('-i', '--captchaId', required=False)
    p.add_argument('-d', '--geetestApiServerSubdomain', required=False)
    p.add_argument('-r', '--max-retries', type=int, default=60)

    # reCAPTCHA v2 variants
    for name in ['ReCaptchaV2TaskProxyLess', 'ReCaptchaV2EnterpriseTask', 'ReCaptchaV2EnterpriseTaskProxyLess']:
              p = subparsers.add_parser(name, help='Solve Google reCAPTCHA v2')
        p.add_argument('-u', '--websiteURL', required=True)
        p.add_argument('-k', '--websiteKey', required=True)
        p.add_argument('-p', '--proxy', required=False)
        p.add_argument('-a', '--pageAction', required=False)
        p.add_argument('-e', '--enterprisePayload', required=False)
        p.add_argument('-i', '--isInvisible', type=bool, default=False, required=False)
        p.add_argument('-s', '--isSession', type=bool, default=False, required=False)
        p.add_argument('-r', '--max-retries', type=int, default=60)

    # reCAPTCHA v3 variants
    for name in ['ReCaptchaV3Task', 'ReCaptchaV3TaskProxyLess', 'ReCaptchaV3EnterpriseTask', 'ReCaptchaV3EnterpriseTaskProxyLess']:
              p = subparsers.add_parser(name, help='Solve Google reCAPTCHA v3')
        p.add_argument('-u', '--websiteURL', required=True)
        p.add_argument('-k', '--websiteKey', required=True)
        p.add_argument('-p', '--proxy', required=False)
        p.add_argument('-a', '--pageAction', required=False)
        p.add_argument('-e', '--enterprisePayload', required=False)
        p.add_argument('-s', '--isSession', type=bool, default=False, required=False)
        p.add_argument('-r', '--max-retries', type=int, default=60)

    # MTCaptcha variants
    for name in ['MtCaptchaTask', 'MtCaptchaTaskProxyLess']:
              p = subparsers.add_parser(name, help='Solve MTCaptcha')
        p.add_argument('-u', '--websiteURL', required=True)
        p.add_argument('-k', '--websiteKey', required=True)
        p.add_argument('-p', '--proxy', required=False)
        p.add_argument('-r', '--max-retries', type=int, default=60)

    # DatadomeSliderTask
    p = subparsers.add_parser('DatadomeSliderTask', help='Solve DataDome')
    p.add_argument('-u', '--captchaUrl', required=True)
    p.add_argument('-a', '--userAgent', required=False)
    p.add_argument('-p', '--proxy', required=False)
    p.add_argument('-r', '--max-retries', type=int, default=60)

    # AWS WAF variants
    for name in ['AntiAwsWafTask', 'AntiAwsWafTaskProxyLess']:
              p = subparsers.add_parser(name, help='Solve AWS WAF')
        p.add_argument('-u', '--websiteURL', required=True)
        p.add_argument('-p', '--proxy', required=False)
        p.add_argument('-k', '--awsKey', required=False)
        p.add_argument('-i', '--awsIv', required=False)
        p.add_argument('-c', '--awsContext', required=False)
        p.add_argument('--awsChallengeJS', required=False)
        p.add_argument('--awsApiJs', required=False)
        p.add_argument('--awsProblemUrl', required=False)
        p.add_argument('--awsApiKey', required=False)
        p.add_argument('--awsExistingToken', required=False)
        p.add_argument('-r', '--max-retries', type=int, default=60)

    # AntiTurnstileTaskProxyLess
    p = subparsers.add_parser('AntiTurnstileTaskProxyLess', help='Solve Cloudflare Turnstile')
    p.add_argument('-u', '--websiteURL', required=True)
    p.add_argument('-k', '--websiteKey', required=True)
    p.add_argument('-a', '--action', required=False)
    p.add_argument('-c', '--cdata', required=False)
    p.add_argument('-r', '--max-retries', type=int, default=60)

    # AntiCloudflareTask
    p = subparsers.add_parser('AntiCloudflareTask', help='Solve Cloudflare Challenge')
    p.add_argument('-u', '--websiteURL', required=True)
    p.add_argument('-p', '--proxy', required=False)
    p.add_argument('-a', '--userAgent', required=False)
    p.add_argument('-t', '--html', required=False)
    p.add_argument('-r', '--max-retries', type=int, default=60)

    args = parser.parse_args()
    if not args.command:
              parser.print_help()
        sys.exit(1)

    try:
              solver = CapSolver()
        solution = solver.solve(args)
        print(json.dumps(solution, indent=2))
except Exception as e:
        print('Solve failed:', e)
        sys.exit(1)


if __name__ == "__main__":
      main()
