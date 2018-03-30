import requests
from bs4 import BeautifulSoup
import json
import re

# Turn off HTTTPS warnings since we're using a custom CA
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings()

#Confluence
local_confl = 'https://confluence' # Your Confluence server URL -- CHANGE THIS
username = 'admin' #username with sysadmin privileges -- CHANGE THIS
pw = 'admin' #password for username above -- CHANGE THIS
#Bamboo
local_bamboo = 'https://bamboo' # Your Bamboo server URL -- CHANGE THIS
#Bitbucket
local_bitb = 'https://bitbucket' # Your Bitbucket server URL -- CHANGE THIS


def get_latest_ver_avail(url):
	r = requests.get(url)
	if r.status_code != 200:
		print "Error accessing URL: " + url
		return None
	clean_json = r.text.replace('downloads(','')[:-1]
	#print clean_json
	parsed = json.loads(clean_json)
	for dl in parsed:
		#print dl['description']
		#print dl
		if 'Linux' in dl['description'] or 'TAR' in dl['description']:
			return dl['version'],dl['releaseNotes']

def check_confluence():
	output_title('Confluence')
	
	atlass_url = 'https://my.atlassian.com/download/feeds/current/confluence.json'

	version_uri = '/admin/systeminfo.action'
	auth_uri = '/doauthenticate.action'
	
	r = requests.Session()
	s = r.get(local_confl+version_uri, auth=(username,pw), verify=False)
	if s.status_code != 200:
		print 'Error logging in to Confluence'
		return None
	t = r.post(local_confl+auth_uri, data={'password': pw})
	if t.status_code != 200:
		print 'Error logging in to Confluence'
		return None
	s = r.get(local_confl+version_uri, verify=False)
	if s.status_code != 200:
		print 'Error logging in to Confluence'
		return None
	
	soup = BeautifulSoup(s.text, "html5lib")
	for strong_tag in soup.find_all("strong"):
		if strong_tag.text == "Confluence Version":
			local_ver = strong_tag.findParent().next_sibling.text
	
	latest_ver,rel_notes = get_latest_ver_avail(atlass_url)
	
	compare_versions(local_ver, latest_ver, rel_notes)	

def check_bamboo():
	output_title('Bamboo')
	
	atlass_url = 'https://my.atlassian.com/download/feeds/current/bamboo.json'
	
	r = requests.Session()
	s = r.get(local_bamboo, verify=False)
	if s.status_code != 200:
		print 'Error accessing Bamboo'
		return None
	#print s.text
	
	soup = BeautifulSoup(s.text, "html5lib")
	footer_text = soup.find('div', class_='footer-body').findChild('p').text
	search_obj = re.search(r'version (.*) build', footer_text)
	local_ver = search_obj.group(1)
	
	latest_ver,rel_notes = get_latest_ver_avail(atlass_url)
	
	compare_versions(local_ver, latest_ver, rel_notes)

def check_bitbucket():
	output_title('Bitbucket')
	
	atlass_url = 'https://my.atlassian.com/download/feeds/current/stash.json'
	
	r = requests.Session()
	s = r.get(local_bitb, verify=False)
	if s.status_code != 200:
		print 'Error accessing Bitbucket'
		return None
	#print s.text
	
	soup = BeautifulSoup(s.text, "html5lib")
	local_ver = soup.find('span', {"id": "product-version"}).text.replace(' v','')
	
	latest_ver,rel_notes = get_latest_ver_avail(atlass_url)
	
	compare_versions(local_ver, latest_ver, rel_notes)

def compare_versions(local_ver, latest_ver, rel_notes=None):
	print '\nLocally installed version:'
	print local_ver
	print 'Latest available version: ' + latest_ver
	if str(local_ver) != str(latest_ver):
		print 'Release notes: ' + rel_notes
	print ''

def output_title(title):
	print title + ':'

def main():
	check_confluence()
	print ''
	check_bamboo()
	print ''
	check_bitbucket()

if __name__ == '__main__':
	main()
