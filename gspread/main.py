import gspread
from google.oauth2.service_account import Credentials

scopes = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

credentials = Credentials.from_service_account_file(
    "./credential.json",
    scopes=scopes
)

spread_sheet_url = "https://docs.google.com/spreadsheets/d/1vwK758ipAkbGym0j5KCMFwLGDGQE8XrHGs3uVIecgGU"

# https://zenn.dev/yamagishihrd/articles/2022-09_01-google-spreadsheet-with-python#fn-d711-5
# https://docs.gspread.org/en/v5.7.2/user-guide.html
if __name__ == '__main__':
    gc = gspread.authorize(credentials)
    sh = gc.open_by_url(spread_sheet_url)
    worksheet = sh.worksheet("demo")
    print(worksheet.get_all_values())

    cell = worksheet.find("Hello!")
    print("Found something at R%sC%s" % (cell.row, cell.col))

    worksheet.update('B1', 'Bingo!')
