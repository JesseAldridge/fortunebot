sudo apt-get install fortune
sudo apt-get install fortunes
git clone https://github.com/JesseAldridge/fortunebot
git clone https://github.com/JesseAldridge/logrot
python fortunebot/fortunebot.py 2>&1 | python logrot/logrot.py fortunebot/out.txt &
