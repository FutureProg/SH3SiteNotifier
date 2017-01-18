
# COMPSCI 3SH3 Site Notifier
## Usage
1. Install [Virtualenv](https://virtualenv.pypa.io/en/stable/) using pip

    <code>$ pip install virtualenv </code>   

2. Download [terminal-notifier](https://github.com/julienXX/terminal-notifier)

3. Create an environment called "env"

    <code>$ virtualenv env</code>

4. Init the program through the virtual environment using <code>./gen init</code>

5. You can run or test the program using <code> ./gen run </code> and <code> ./gen test </code>

<b>Note: Do not use the makefile without working through the environment. This is done through:</b>

<code>$ source ./env/bin/activate</code>

## End Notes

- using ``launchctl`` I was able to create a daemon that runs on OSX and displays notifications of changes every hour

