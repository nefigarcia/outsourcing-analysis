import csv
open_file = 'jobs_postings.csv'

def transform_data(data):
    country_map = {
        'IN': 'India',
        'US': 'United States',
        'GB': 'United Kingdom',
        'CA': 'Canada',
        'DE': 'Germany',
        'FR': 'France',
        # Add more as needed
    }
    transformed_data = []
    for entry in data:

        if len(entry) > 2 and '\n' in entry[2]:
            level,location = entry[2].split('\n', 1)
            if ',' in location:
                parts = location.split(',')
                country_code = parts[-1].strip()
                country_full = country_map.get(country_code, country_code)
                location = country_full
            transformed_data.append([entry[0], entry[1], location, level])
        else:
            transformed_data.append(entry)
    return transformed_data

# save to csv file
def save_to_csv(data):
    with open(open_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Company', 'Role', 'Location', 'Level'])
        for row in data:
            writer.writerow(row)
