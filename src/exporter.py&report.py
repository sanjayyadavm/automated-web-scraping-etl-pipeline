import json

def export_csv(df):
    df.to_csv("output/jobs.csv", index=False)

def export_json(df):
    df.to_json(
        "output/jobs.json",
        orient="records",
        indent=4
    )




def generate_report(df):

    total = len(df)

    avg_length = df["quote_length"].mean()

    with open("output/report.txt", "w") as f:
        f.write("WEB SCRAPING REPORT\n")
        f.write("===================\n")
        f.write(f"Total Records : {total}\n")
        f.write(f"Average Length : {avg_length:.2f}\n")
