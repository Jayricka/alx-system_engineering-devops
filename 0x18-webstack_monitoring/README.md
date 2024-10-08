0x18. Webstack monitoring

# Webstack monitoring

# Datadog Setup Guide

## Overview

This document provides instructions for setting up Datadog monitoring on your server `web-01`. It includes steps for signing up for Datadog, installing the Datadog Agent, creating an application key, and verifying the setup.

## Prerequisites

- Access to the `web-01` server.
- Datadog account credentials.

## 1. Sign Up for Datadog

1. Go to [Datadog's US website](https://app.datadoghq.com).
2. Click on **Get Started** or **Sign Up**.
3. Fill in the required details such as your email address, password, and company name.
4. Select the US1 region during the sign-up process.
5. Verify your email address by clicking the verification link sent to your email.

## 2. Install the Datadog Agent on `web-01`

1. **Log in to `web-01`:**
   ```bash
   ssh user@web-01

## 3. Create and Configure Datadog Dashboards

### Create a New Dashboard

1. Log in to Datadog.
2. Navigate to **Dashboards** > **New Dashboard**.
3. Enter a title for your dashboard and configure its layout.

### Add Widgets to the Dashboard

Add at least 4 widgets. Example widgets include:

- **Time Series Widget:**
  - Query: `avg:system.disk.read_time{*}`.

- **Top List Widget:**
  - Query: `top(sum:system.network.in{*}, 10)`.

- **Heatmap Widget:**
  - Query: `heatmap(avg:system.io.await{*})`.

- **Query Value Widget:**
  - Query: `sum:system.disk.write_time{*}`.

### Retrieve Dashboard ID

Use the Datadog API to get the dashboard ID:

```bash
curl -X GET "https://api.datadoghq.com/api/v1/dashboard" \
    -H "DD-API-KEY: your_api_key_here" \
    -H "DD-APPLICATION-KEY: your_application_key_here"
