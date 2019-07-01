running on a mac:

#### install virtualenv
    sudo easy_install pip
    sudo pip install virtualenv
#### create a virtualenv called scrapy
    virtualenv scrapy
#### activate the virtualenv (navigate to where your virtualenv is, usually ~/.virtualenvs/<name_of_virtualenv>
    source bin/activate
    
#### install scrapy
    pip install scrapy
    
#### clone this repo
    git clone https://github.com/mancdaz/scrapy-heaver/
    
#### run your desired spider
    cd scrapy-heaver
    scrapy crawl snickers
