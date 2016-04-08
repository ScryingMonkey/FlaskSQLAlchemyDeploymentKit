echo "...instaling requirements.txt"
sudo pip install -r requirements.txt
echo "...installing ElasticBeanstalk CLI"
sudo pip install awsebcli
echo "...installing SQL Development headers"
sudo apt-get install libsqlite3-dev
echo "...complete"