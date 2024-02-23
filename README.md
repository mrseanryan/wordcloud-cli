# word-cloud-etl

Generate wordcloud images from a data file: raw text, CSV or Parquet.

## Examples

### Reading from a Parquet file:

- Countries trading with New Zealand

```
pipenv run python main.py examples\NZ_trade.parquet   country_code     images\mask.small.png
```

![NZ trade countries](./images/country_code.png)

... adding a mask:
![NZ trade countries with mask](./images/country_code_masked.png)

### Reading from a CSV file:

```
pipenv run python main.py examples\NZ_trade.csv   country_codez     images\mask.small.png
```

![NZ trade countries - CSV](./images/country_codez.png)

... adding a mask:
![NZ trade countries - CSV with mask](./images/country_codez_masked.png)

### Reading from a raw text file:

```
pipenv run python main.py examples\king_lear.txt   word     images\mask.small.png
```
![King Lear - raw text](./images/word.png)

... adding a mask:
![King Lear - raw text with mask](./images/word_masked.png)

## Setup

```shell
pipenv install
pipenv shell
python main.py <path to parquet file> <word column name>
```

## References

- https://amueller.github.io/word_cloud/
- https://amueller.github.io/word_cloud/auto_examples/index.html#example-gallery
- https://medium.com/mlearning-ai/wordclouds-with-python-c287887acc8b
