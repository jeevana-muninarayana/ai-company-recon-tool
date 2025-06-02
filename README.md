# AI Company Recon Tool

![Python](https://img.shields.io/badge/python-3.9+-blue.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Build Status](https://img.shields.io/badge/build-passing-brightgreen)

GenAI-powered reconnaissance engine to automate discovery of exposed surface area, open ports, CDN usage, and risky metadata across a target company’s infrastructure.

## Amazon-Relevant Use Case

Used to simulate AppSec threat modeling at scale — ideal for early security reviews in fast-moving product teams, aligning with AWS AppSec’s mission of secure-by-design tooling.

## Features
- DNS and ASN enumeration
- Open ports and CDN trace detection
- Natural language enrichment using OpenAI
- Custom metadata tagging for IPs and endpoints

## Stack
- Python, Shodan API, Censys, OpenAI
- IPWHOIS, aiohttp

## Setup

```bash
git clone https://github.com/jeevana-muninarayana/ai-company-recon-tool
cd ai-company-recon-tool
pip install -r requirements.txt
