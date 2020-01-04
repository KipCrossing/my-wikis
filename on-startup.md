In my case none of the instructions were a perfect solution. If you were as unlucky as me, try this detailed one

Put all your executing code in a separate text file with an arbitrary name such as foo.sh and save it in an arbitrary place.
Add

#!/bin/sh
as first line of your code.

Try executing your foo.sh by

sudo foo.sh
to check there are no errors at all.

Provide your /etc/rc.local script with full path and name of your created script after the sh command

sh '/path/to/your/script/foo.sh'
Remember to put the above line before the last line of code

exit 0
at the end of the /etc/rc.local script.

Check first line of /etc/rc.local to be

#!/bin/sh -e
Make your /etc/rc.local executable in case it is not already executable by

sudo chown root /etc/rc.local
sudo chmod 755 /etc/rc.local
Check everything works fine by executing

sudo /etc/init.d/rc.local start
Test restart your system.
