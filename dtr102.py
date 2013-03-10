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

def superCopy(src, dst):
	try:
		shutil.copy(src, dst)
	except WindowsError:
		raise
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
	if not os.path.exists('C:\Users\probook\Desktop\DTR'):
		os.mkdir('C:\Users\probook\Desktop\DTR')
	print 'Copying files...'
	os.system('for %R IN ( \
		C:\Users\probook\Documents\Projects\src\Baguio \
		C:\Users\probook\Documents\Projects\src\Vigan \
		C:\Users\probook\Documents\Projects\src\Bontoc \
		) do copy %R C:\Users\probook\Desktop\DTR')
	shutil.rmtree(dst)
	os.rename('C:\Users\probook\Desktop\DTR', dst)
	print 'Done copying...'
	os.startfile(dst)
	
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