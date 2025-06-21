#!/usr/bin/env python3
"""
Analyze the detailed click data from email-launch-detailed-clicks.csv
"""

import csv
from collections import defaultdict
from datetime import datetime

# Read the detailed clicks file
with open('/mnt/c/Users/jcerv/Jose/search-costs/02_intervention_materials/email_campaigns/launch-prep/email-launch-detailed-clicks.csv', 'r') as f:
    reader = csv.DictReader(f)
    data = list(reader)

print(f'Total records: {len(data)}')

# Analyze click patterns
total_clicks = sum(int(row['total_clicks']) for row in data)
records_with_clicks = sum(1 for row in data if int(row['total_clicks']) > 0)
print(f'Records with clicks: {records_with_clicks}')
print(f'Total clicks: {total_clicks}')

# Group by date
clicks_by_date = defaultdict(int)
unique_clickers_by_date = defaultdict(set)

for row in data:
    if row['date'] != 'NA':
        clicks_by_date[row['date']] += int(row['clicks'])
        if int(row['clicks']) > 0:
            unique_clickers_by_date[row['date']].add(row['contact_email'])

print('\nClicks by date:')
for date in sorted(clicks_by_date.keys()):
    print(f'  {date}: {clicks_by_date[date]} clicks from {len(unique_clickers_by_date[date])} unique clickers')

# Analyze by condition
control_data = [row for row in data if row['condition'] == 'control']
treatment_data = [row for row in data if row['condition'] == 'treatment']

control_clicks = sum(int(row['total_clicks']) for row in control_data)
treatment_clicks = sum(int(row['total_clicks']) for row in treatment_data)
control_clickers = sum(1 for row in control_data if int(row['total_clicks']) > 0)
treatment_clickers = sum(1 for row in treatment_data if int(row['total_clicks']) > 0)

print(f'\nControl group:')
print(f'  Total emails: {len(control_data)}')
print(f'  Emails clicked: {control_clickers}')
print(f'  Total clicks: {control_clicks}')
print(f'  Click rate: {control_clickers/len(control_data)*100:.2f}%')

print(f'\nTreatment group:')
print(f'  Total emails: {len(treatment_data)}')
print(f'  Emails clicked: {treatment_clickers}')
print(f'  Total clicks: {treatment_clicks}')
print(f'  Click rate: {treatment_clickers/len(treatment_data)*100:.2f}%')

# Find high-engagement recipients
high_engagement = [(row['contact_email'], int(row['total_clicks']), row['condition']) 
                   for row in data if int(row['total_clicks']) >= 3]
high_engagement.sort(key=lambda x: x[1], reverse=True)

if high_engagement:
    print('\nHigh engagement recipients (3+ clicks):')
    for email, clicks, condition in high_engagement[:10]:
        print(f'  {email}: {clicks} clicks ({condition})')

# Analyze temporal patterns
print('\nTemporal analysis:')
# Parse dates to identify email periods
email1_dates = []
email2_dates = []

for row in data:
    if row['date'] != 'NA':
        try:
            date = datetime.strptime(row['date'], '%m/%d/%Y')
            if date < datetime(2024, 7, 9):
                email1_dates.append(date)
            else:
                email2_dates.append(date)
        except:
            pass

if email1_dates:
    print(f'  Email 1 period: {min(email1_dates).strftime("%Y-%m-%d")} to {max(email1_dates).strftime("%Y-%m-%d")}')
if email2_dates:
    print(f'  Email 2 period: {min(email2_dates).strftime("%Y-%m-%d")} to {max(email2_dates).strftime("%Y-%m-%d")}')

# Export summary
output_file = '/mnt/c/Users/jcerv/Jose/search-costs/01_experiment_design/click_analysis_summary.csv'
with open(output_file, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['metric', 'control', 'treatment', 'total'])
    writer.writerow(['emails_sent', len(control_data), len(treatment_data), len(data)])
    writer.writerow(['emails_clicked', control_clickers, treatment_clickers, records_with_clicks])
    writer.writerow(['total_clicks', control_clicks, treatment_clicks, total_clicks])
    writer.writerow(['click_rate_pct', f'{control_clickers/len(control_data)*100:.2f}', 
                     f'{treatment_clickers/len(treatment_data)*100:.2f}',
                     f'{records_with_clicks/len(data)*100:.2f}'])

print(f'\nSummary saved to: {output_file}')