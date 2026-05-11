{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyO9aKIh882KN1GFobOM5PGY",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/emilioocervantes/portfolio-strategy-analyzer/blob/main/financial_analysis.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "1BQfHJB6y9Ea"
      },
      "outputs": [],
      "source": [
        "#importing some data libraries\n",
        "import pandas as pd\n",
        "import matplotlib.pyplot as plt\n",
        "import yfinance as yf"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from numpy import info\n",
        "#Downloading companies comparison data and basis data\n",
        "\n",
        "ticker1 = \"AMD\"\n",
        "ticker2 = \"NVDA\"\n",
        "ticker3 = \"AAPL\"\n",
        "\n",
        "info1 = yf.Ticker(ticker1).info\n",
        "info2 = yf.Ticker(ticker2).info\n",
        "info3 = yf.Ticker(ticker3).info\n",
        "\n",
        "companyN1 = (info1[\"longName\"])\n",
        "companyN2 = (info2[\"longName\"])\n",
        "companyN3 = (info3[\"longName\"])\n",
        "\n",
        "label1 = (companyN1)\n",
        "label2 = (companyN2)\n",
        "label3 = (companyN3)\n",
        "\n",
        "stock1 = yf.download(ticker1, start=\"2021-01-01\", end=\"2026-01-01\")\n",
        "stock2 = yf.download(ticker2, start=\"2021-01-01\", end=\"2026-01-01\")\n",
        "stock3 = yf.download(ticker3, start=\"2021-01-01\", end=\"2026-01-01\")"
      ],
      "metadata": {
        "id": "rbjGNsyN02Tk"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "plt.title(\"Comparison of stock prices\")\n",
        "plt.xlabel(\"Date\")\n",
        "plt.ylabel(\"Opening price\")\n",
        "\n",
        "plt.plot(stock1[\"High\"], label=(label1))\n",
        "plt.plot(stock2[\"High\"], label=(label2))\n",
        "plt.plot(stock3[\"High\"], label=(label3))\n",
        "\n",
        "plt.legend()"
      ],
      "metadata": {
        "id": "yWssrt4e15RB"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#Getting the stock prices dataframes\n",
        "prices = pd.DataFrame()\n",
        "\n",
        "prices[ticker1] = stock1[\"Close\"]\n",
        "prices[ticker2] = stock2[\"Close\"]\n",
        "prices[ticker3] = stock3[\"Close\"]\n",
        "\n",
        "prices.head()"
      ],
      "metadata": {
        "id": "Nu7-gTdsIIJA"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "prices[\"AMD_MA25\"] = prices[ticker1].rolling(25).mean()\n",
        "prices.head()\n",
        "\n",
        "plt.title(\"AMD Price vs MA25\")\n",
        "plt.xlabel(\"Date\")\n",
        "plt.ylabel(\"Price\")\n",
        "\n",
        "plt.plot(prices[ticker1], label=ticker1)\n",
        "plt.plot(prices[\"AMD_MA25\"], label=\"MA25\")\n",
        "\n",
        "plt.legend()"
      ],
      "metadata": {
        "id": "bRNHv0vJJcz1"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}