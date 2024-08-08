# int orther to create a virtual environment we can run this command: python3 -m venv venv
# after venv folder is created we have to run "actovate" file under venv=>bin by running this command: source venv/bin/activate
# now we need to select an interpreter in VScode => cmd+shift+P and serach for python and select interpreter 
# now we need to install dependencies: first is speech recognition : pip install speechrecognition
#this is a library for speech recognition and documentation can be found on pypi.org/project/speechrecognition
# we will be using Google Speech Recognition API
# We also need to install PyAudio: pip istall pyaudio
# there are so many errors because I didn't have "portaudio" library installed I have to install Homebrew and then install it. 
# Homebrew is installed like this: /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
# After that we need to install protaudio via Homebrew: brew install portaudio