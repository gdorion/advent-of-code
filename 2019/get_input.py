from urllib2 import urlopen, Request
import sys

puzzle_no = sys.argv[1]

f = open('./session', 'r')
session = f.readlines()[0]

def get_url(puzzle_no):
  url = "https://adventofcode.com/2019/day/%s/input" % puzzle_no
  return url

def download_content(puzzle_no):
  request = Request(get_url(puzzle_no))
  request.add_header('Cookie', 'session=%s' % session)  
  response = urlopen(request)
  return response.read()

content = download_content(sys.argv[1])
f = open("./inputs/%s.txt" % puzzle_no, 'w')
f.write(content)