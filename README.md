<img src=https://d1r5llqwmkrl74.cloudfront.net/notebooks/fsi/fs-lakehouse-logo-transparent.png width="600px">

[![DBR](https://img.shields.io/badge/DBR-10.4ML-red?logo=databricks&style=for-the-badge)](https://docs.databricks.com/release-notes/runtime/10.4ml.html)
[![CLOUD](https://img.shields.io/badge/CLOUD-GCP-blue?logo=googlecloud&style=for-the-badge)](https://cloud.google.com/databricks)
[![POC](https://img.shields.io/badge/POC-5_days-green?style=for-the-badge)](https://databricks.com/try-databricks)

*The future of finance goes hand in hand with social responsibility, environmental stewardship and corporate ethics. 
In order to stay competitive, Financial Services Institutions (FSI)  are increasingly  disclosing more information 
about their environmental, social and governance (ESG) performance. By better understanding and quantifying the 
sustainability and societal impact of any investment in a company or business, FSIs can mitigate reputation risk and 
maintain the trust with both their clients and shareholders. At Databricks, we increasingly hear from our customers 
that ESG has become a C-suite priority. This is not solely driven by altruism but also by economics: 
Higher ESG ratings are generally positively correlated with valuation and profitability while negatively correlated with 
volatility ([source](https://corpgov.law.harvard.edu/2020/01/14/esg-matters/)). 
In this solution, we offer a novel approach to sustainable finance by combining NLP techniques and news analytics to 
extract key strategic ESG initiatives and learn companies' commitments to corporate responsibility.*

___
<antoine.amend@databricks.com>

___

<img src='images/reference_architecture.png' width=800>

___

&copy; 2022 Databricks, Inc. All rights reserved. The source in this notebook is provided subject to the Databricks License [https://databricks.com/db-license-source].  All included or referenced third party libraries are subject to the licenses set forth below.

| library                                | description             | license    | source                                              |
|----------------------------------------|-------------------------|------------|-----------------------------------------------------|
| beautifulsoup4                         | Web scraper             | MIT        | https://www.crummy.com/software/BeautifulSoup       |
| PyPDF2                                 | PDF parser              | BSD        | https://pypi.org/project/PyPDF2                     |
| NLTK                                   | NLP toolkit             | Apache2    | https://github.com/nltk/nltk                        |
| Spacy                                  | NLP toolkit             | MIT        | https://spacy.io/                                   |
| Wordcloud                              | Visualization           | MIT        | https://github.com/amueller/word_cloud              |
