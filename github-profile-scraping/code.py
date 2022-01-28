try:
    import requests
    from bs4 import BeautifulSoup as bs
except:
    print("<Install the module requests, bs4>")
    commands = """
    pip install requests bs4
    """
    print(":::Commands:::")
    print(commands)
    exit()

github_user = input("Input github username: ")

url = f"https://github.com/{github_user.strip()}"

response = requests.get(url)

if response.status_code == 200:

    print("\n<User Found>")
    print("<Loading Information>")

    # html parse all the content
    try:
        soup = bs(response.content, 'html.parser')
        user_info = soup.title.text

        profile_image = soup.find('img', {"alt": "Avatar"})['src']
        user_name = soup.find('span', {"itemprop": "name"}).text.strip()

        raw_data = soup.find_all(
            "a", {"class": "Link--secondary no-underline no-wrap"})
        followers = raw_data[0].text.strip().split()[0]
        following = raw_data[1].text.strip().split()[0]
        repositories = soup.find('span', {'class': 'Counter'}).text
        additional_data = soup.find_all(
            'a', {"class": "Link--primary", "rel": "nofollow me"})

        information = f"""
		::::: Information :::::
		{user_info}
		Username    : {user_name}
		Followers   : {followers}
		Following   : {following}
		Repositories: {repositories}

		:::: Additional Information And Links ::::"""
        print(information)

        print("Profile image :: "+profile_image)
        # new_data = soup.find_all('div', {'class': 'p-note user-profile-bio mb-3 js-user-profile-bio f4'})[0].\
        #     find_all('a', {'class': 'user-mention'})
        # for info in new_data:
        #     print(info.text)
        data = soup.find_all(
            'div', {'class': 'p-note user-profile-bio mb-3 js-user-profile-bio f4'})
        print(data[0].text)
        links = soup.find_all('a', {'rel': 'nofollow'})
        for link in links:
            print(link.text, end=" :: ")
            print(link['href'])

    except:
        print(f'<{github_user} doesn\'t have any public repositories yet>')
else:
    print(f"<No Username with {github_user}>")
