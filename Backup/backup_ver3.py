import os
import time
# Set backup source
source = ['C:\\Users\shawn.conrad\Projects\Python\Learn']
# Set target backup
target_dir = 'E:\\Backup'

if not os.path.exists(target_dir):
    os.mkdir(target_dir)

today = target_dir + os.sep + time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')

# get a comment from the user for perfix
comment = input('Enter comment for filename > ')
# Check if comment was entered
if len(comment) == 0:
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' + \
        comment.replace(' ', '_') + '.zip'  # replace spaces

if not os.path.exists(today):
    os.mkdir(today)
    print('Successfully created directory', today)

zip_command = 'zip -r {0} {1}'.format(target,
                                      ' '.join(source))

# Run the backup
print('Zip command is:')
print(zip_command)
print('Running:')
if os.system(zip_command) == 0:
    print('Successfully backed up to', target)
else:
    print('Backup FAILED')
