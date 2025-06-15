import boto3
import json
from collections import defaultdict
import pandas as pd

# Map of AWS region code to full location name used by the Pricing API
REGION_NAME_TO_LOCATION = {
    'us-east-1': 'US East (N. Virginia)',
    'us-east-2': 'US East (Ohio)',
    'us-west-1': 'US West (N. California)',
    'us-west-2': 'US West (Oregon)',
    'af-south-1': 'Africa (Cape Town)',
    'ap-east-1': 'Asia Pacific (Hong Kong)',
    'ap-south-1': 'Asia Pacific (Mumbai)',
    'ap-south-2': 'Asia Pacific (Hyderabad)',
    'ap-southeast-1': 'Asia Pacific (Singapore)',
    'ap-southeast-2': 'Asia Pacific (Sydney)',
    'ap-southeast-3': 'Asia Pacific (Jakarta)',
    'ap-northeast-1': 'Asia Pacific (Tokyo)',
    'ap-northeast-2': 'Asia Pacific (Seoul)',
    'ap-northeast-3': 'Asia Pacific (Osaka)',
    'ca-central-1': 'Canada (Central)',
    'eu-central-1': 'EU (Frankfurt)',
#    'eu-central-2': 'EU (Zurich)',
    'eu-west-1': 'EU (Ireland)',
    'eu-west-2': 'EU (London)',
    'eu-west-3': 'EU (Paris)',
    'eu-north-1': 'EU (Stockholm)',
    'eu-south-1': 'EU (Milan)',
#    'eu-south-2': 'EU (Spain)',
    'me-south-1': 'Middle East (Bahrain)',
    'me-central-1': 'Middle East (UAE)',
#    'sa-east-1': 'South America (São Paulo)',
    'il-central-1': 'Israel (Tel Aviv)',
}

INSTANCE_TYPES = [ 'm8g.medium','t3.medium', 'm7g.medium', 'm6g.medium', 't3a.medium',]

pricing_client = boto3.client('pricing', region_name='us-east-1')
prices = defaultdict(dict)

for instance_type in INSTANCE_TYPES:
    for region_code, location_name in REGION_NAME_TO_LOCATION.items():
        try:
            response = pricing_client.get_products(
                ServiceCode='AmazonEC2',
                Filters=[
                    {'Type': 'TERM_MATCH', 'Field': 'instanceType', 'Value': instance_type},
                    {'Type': 'TERM_MATCH', 'Field': 'location', 'Value': location_name},
                    {'Type': 'TERM_MATCH', 'Field': 'operatingSystem', 'Value': 'Linux'},
                    {'Type': 'TERM_MATCH', 'Field': 'preInstalledSw', 'Value': 'NA'},
                    {'Type': 'TERM_MATCH', 'Field': 'tenancy', 'Value': 'Shared'},
                    {'Type': 'TERM_MATCH', 'Field': 'capacitystatus', 'Value': 'Used'},
                ],
                MaxResults=1
            )

            if not response['PriceList']:
                prices[region_code][instance_type] = None
                continue

            price_item = json.loads(response['PriceList'][0])
            on_demand = next(iter(price_item['terms']['OnDemand'].values()))
            price_dimensions = next(iter(on_demand['priceDimensions'].values()))
            price_per_hour = int(
                float(price_dimensions['pricePerUnit']['USD']) * 8760
              )  # Convert hourly price to annual price
            prices[region_code][instance_type] = price_per_hour

        except Exception:
            prices[region_code][instance_type] = None

# Create DataFrame
df = pd.DataFrame.from_dict(prices, orient='index')
df.index.name = 'Region'

# Convert to HTML table

def colorize(val):
    if pd.isna(val):
        return 'background-color: white; color: gray'
    return 'text-align: center;'

html = (
    df.sort_index()
    .style
    .format(na_rep="", precision=0)
    .background_gradient(cmap='RdYlGn_r', axis=None)
    .applymap(colorize)
    .set_caption("Yearly EC2 On-Demand Prices ($)")
    .to_html()
)

# Save to file
with open("ec2_prices_table_2.html", "w") as f:
    f.write(html)

print("HTML table saved to ec2_prices_table.html")
