running on a mac:

#### install virtualenv
    sudo easy_install pip
    sudo pip install virtualenv
#### create a virtualenv called scrapy
    virtualenv scrapy
#### activate the virtualenv (navigate to where your virtualenv is, usually ~/.virtualenvs/<name_of_virtualenv>
    source bin/activate
    
#### clone this repo
    git clone https://github.com/mancdaz/scrapy-heaver/

#### install scrapy and requirements
    cd scrapy-heaver
    pip install -r requirements.txt
    
#### run your desired spider (select output type using filename extension)
    scrapy crawl snickers -o snickers.json
    scrapy crawl snickers -o snickers.csv

    <lots of output>
