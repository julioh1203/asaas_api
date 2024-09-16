# Asaas API Integration

## Project Description

This project provides an API for integration with Asaas. It allows you to perform various operations such as GET, POST, PUT, and DELETE requests to the Asaas API.

The project is divided into three modules: `asaas_customers`, `asaas_charging`, and `asaas_subscription`. Each module contains a class that provides methods for interacting with the Asaas API.

## Requirements

- Python >= 3.11
- httpx
- pytest
- pytest-env
- pytest-order
- black
- flake8
- ipdb
- ipython
- pyright
- isort
- python-dotenv

## Installation

1. Clone the repository:
    ```sh
    git clone <repository_url>
    cd asaas_api
    ```

2. Install the required dependencies:
    ```sh
    pip install -r requirements.in
    ```

3. Create a `.env` file in the root directory of the project and add your Asaas API key and URL:
    ```dotenv
    ASAAS_API_KEY=your_api_key
    ASAAS_API_URL=the_Asaas_api_url
    ```

## Usage

### Initialization

To use the `Asaas` class, you need to initialize it with your API key and API URL. The API key and URL can be loaded from the `.env` file using the `python-dotenv` package:

```python
from asaas_customers import AsaasCustomer
from asaas_charging import AsaasCharging
from asaas_subscription import AsaasSubscription

from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("ASAAS_API_KEY")
api_url = os.getenv("ASAAS_API_URL")
asaas_charging = AsaasCharging()
asaas_customers = AsaasCustomer()
asaas_subscription = AsaasSubscription()
```

### Example
```python
from asaas_customers import AsaasCustomer

from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("ASAAS_API_KEY")
api_url = os.getenv("ASAAS_API_URL")
asaas_customers = AsaasCustomer(api_key, api_url)
response = asaas_customers.get_customer('cpf', '12345678901')
print(response.json()) 
```
