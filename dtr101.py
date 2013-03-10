import os
import datetime
import shutil

t = datetime.date.today()

sites = ["Baguio", "Bontoc", "Vigan", "Laoag", "La-Union", "Solano", "Tuguegarao", "Cauayan"]
src = 'C:/Users/probook/Documents/Projects/src/'
dst = 'C:/Users/probook/Desktop/EAK_DTR(%s)' %t
pos = ['Yes','yes','ok','y','Y','okay']
okay = []
nokay = []
	
def check():
	for site in sites:
		src1 = src + site
		if os.path.exists(src1) and len(os.listdir(src1)) != 0:
			okay.append(site)
		else:
			nokay.append(site)
	print 'North Luzon DTR'	
	print '-'*40
	print 'Branch{:15s}Status'.format('')
	print '-'*40
	for site in okay:
		a = 'Sent'
		print '{:<20s} {:<20s}'.format(site,a)
	for site in nokay:
		a = 'Empty'
		print '{:<20s} {:<20s}'.format(site,a)
	print '-'*40
	
def download():
	for site in okay:
		try:
			src2 = src + site
			shutil.copytree(src2, dst)
			print '%s file downloaded \n' %site
		except WindowsError:
			print 'Destination Folder already exist. Delete?'
			ch = raw_input('Delete: ')
			if ch in pos:
				shutil.copy(src2, dst)
				print 'File deleted, press 2 to download again'
			else:
				print 'Cancelled'
		except IOError:
			print 'Something went wrong\n'
			
print 'Welcome...'
print 'Logging in...'
print 'Checking directories...'		

n = '0'
print 'Functions: (1)Check Status (2)Download DTR (3)Quit'
while n != '3':
	n = raw_input('Function: ')
	if n == '1':
		check()
	elif n == '2':
		download()
	elif n == '3':
		print 'Good Bye...'
	else:
		print 'Not a valid function'