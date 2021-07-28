import webbrowser

print('Enter your champion:')

k = input()

url = 'https://www.mobafire.com/league-of-legends/champion/' + k

# MacOS
# chrome_path = 'open -a /Applications/Google\ Chrome.app %s'

# Windows
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

webbrowser.get(chrome_path).open(url)