import requests
import pandas as pd


url = "https://remoteok.com/api"
response = requests.get(url)


if response.status_code == 200:
    jobs_data = response.json()

    
    jobs_list = jobs_data[1:]

    
    records = []
    for job in jobs_list:
        company = job.get("company")
        position = job.get("position")            
        location = job.get("location")
        tags = job.get("tags")                   

        
        records.append({
            "Company Name": company,
            "Job Role": position,
            "Location": location,
            "Tags/Features": ", ".join(tags) if tags else ""
        })

    
    df = pd.DataFrame(records)

    
    output_file = "scrape01.csv"
    df.to_csv(output_file, index=False)
    print(f"CSV file saved successfully as: {output_file}")

else:
    print("Failed to fetch data from RemoteOK API. Status Code:", response.status_code)
