# When we print out string it shows result as it is.
google_url = "https://google.com"
print(google_url)

# We can remove 'https://' as prefix.
# So we can focus on just part of URL that user need to enter into address bar
print(google_url.removeprefix('https://'))

# We can make a variable also,
address = google_url.removeprefix('https://')
print(address)