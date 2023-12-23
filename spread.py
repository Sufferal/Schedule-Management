from google.oauth2 import service_account
from googleapiclient.discovery import build
from main import sorted_table

spreadsheet_id = "19N4p0UT28_3VoL3Ne8MhvKbPnrQavqpE5fgtI-cO_3Y"
# For example:
# spreadsheet_id = "8VaaiCuZ2q09IVndzU54s1RtxQreAxgFNaUPf9su5hK0"

credentials = service_account.Credentials.from_service_account_file("sheets.json", scopes=["https://www.googleapis.com/auth/spreadsheets"])
service = build("sheets", "v4", credentials=credentials)

range_ = "Foaie1!A1"
values = []

for key, value in sorted_table.items():
    values.append(value)
# Build the request to append the values
request = service.spreadsheets().values().append(
    spreadsheetId=spreadsheet_id,
    range=range_,
    valueInputOption="RAW",
    insertDataOption="INSERT_ROWS",
    body={"values": values},
)
sheet_props = request.execute()

print(sheet_props)