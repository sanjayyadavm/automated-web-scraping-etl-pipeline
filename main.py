import os
import logging

from src.scraper import scrape_quotes
from src.transformer import transform
from src.exporter import export_csv, export_json
from src.report import generate_report

os.makedirs("output", exist_ok=True)
os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename="logs/scraper.log",
    level=logging.INFO
)

logging.info("Pipeline Started")

data = scrape_quotes()

df = transform(data)

export_csv(df)
export_json(df)

generate_report(df)

logging.info("Pipeline Completed")

print("Pipeline executed successfully!")