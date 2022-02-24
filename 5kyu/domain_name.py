# Write a function that when given a URL as a string, parses out just the
# domain name and returns it as a string. For example:
# domain_name("http://github.com/carbonfive/raygun") == "github" 
# domain_name("http://www.zombie-bites.com") == "zombie-bites"
# domain_name("https://www.cnet.com") == "cnet"


def domain_name(url):
  """
  url: url of a website to split from "/" and "."
  return: domain name from the url
  """
  domain_list = ([elt.split(".") for elt in url.split("/")])
  for elt in domain_list:
    name = ([elt[i] for i in range(len(elt)) if elt[i] != "www" and elt[i] != "http:" and elt[i] != "https:" and elt[i] != ""])
    if name != []:
      return name[0]

assert domain_name("http://github.com/carbonfive/raygun") == "github", "domain_name('http://github.com/carbonfive/raygun') == 'github'"
assert domain_name("http://www.zombie-bites.com") == "zombie-bites", "domain_name('http://www.zombie-bites.com') == 'zombie-bites'"