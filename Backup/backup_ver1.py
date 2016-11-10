import os
import time

# 1. List files and directories to be backed up
# Example on Windows:
# source = ['"C:\\My Documents"', 'C:\\Code']
# Example on Mac and Linux:
# source = /Users/name/directory
source = ['C:\\Users\shawn.conrad\Projects\Python\Learn']
# Note we had to use double-quotes inside the
# string.

# 2. The backup must be stored in a main backup
# directory. Windows example:
# target_dir = 'E:\\Backup'
# Linus OS X example:
# target_dir = '/Users/swa/ backup'
target_dir = 'E:\\Backup'

# 3. The files are backed up to a zip file.
# 4. The name of the files use time date
target = target_dir + os.sep + \
    time.strftime('%Y%m%d') + '.zip'

# Create target directory if it is not present
if not os.path.exists(target_dir):
    os.mkdir(target_dir)  # make the directory

# 5. Use the 'zip'command to put files in the zip archive
# Windows add to env path. D/L GnuWin32 zip
zip_command = 'zip -r {0} {1}'.format(target,
                                      ' '.join(source))

# Run the backup
print('The Zip command is:')
print(zip_command)
print('Running:')
if os.system(zip_command) == 0:
    print('Successful backup to', target)
else:
    print('Backup FAILED')
