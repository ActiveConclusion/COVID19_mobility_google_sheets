import requests
import urllib.request
import pandas as pd

apple = pd.read_csv("https://raw.githubusercontent.com/ActiveConclusion/COVID19_mobility/master/apple_reports/apple_mobility_report.csv")
apple_Ireland = apple[(apple['country']=='Ireland') | (apple['sub-region']=='Northern Ireland')]
apple_Ireland.to_csv("apple_mobility_report_Ireland.csv", index=False)