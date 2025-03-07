import csv
import sys
import os

def main():
	csv_file = sys.argv[1]
	
	with open(csv_file, newline='', encoding='utf-8') as f:
		reader = csv.reader(f)
		data = list(reader)

	html_output = gen_table(data)

	output_file = "output.txt"
	with open(output_file, 'w', encoding='utf-8') as f:
		f.write(html_output)

def gen_table(data):
	table = ""
	for row in data:
		table += gen_row(row)
	return table

def gen_row(row):
	world = row[0].lower().replace(" ", "_")
	area = row[1] 
	action = row[2]
	AP_Name = row[3]
	AP_ID = row[4]
	Item = row[5]

	html_row = "            <tr>\n"
	html_row += f'              <td style="border: 1px solid #ddd; padding: 8px; text-align: left;">{AP_Name}</td>\n'
	html_row += f'              <td style="border: 1px solid #ddd; padding: 8px; text-align: left;">{area}</td>\n'
	html_row += f'              <td style="border: 1px solid #ddd; padding: 8px; text-align: left;">PLACEHOLDER: {action}</td>\n'
	html_row += f'              <td style="border: 1px solid #ddd; padding: 8px; text-align: left;"><img src="./images/locations/{world}/{AP_Name}.png" alt="{AP_Name}" style="max-width: 640px; max-height: 360px;"></td>\n'
	html_row += "            </tr>\n"

	return html_row
	
if __name__ == "__main__":
    main()
