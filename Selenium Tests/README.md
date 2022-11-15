# Object/Class based Selenium for Python example for indexing public video libraries. 

This is minimum demo of headless Chrome and Selenium on Python 3.10.7.  

Requirements:

- Python 3.10.7
- chromium 107.0.5304.0
- chromedriver 107.0.5304.62
- selenium 4.6.0


## Running the demo

Execute Main.exe or on the command line:
  py Selenium Test.py

## Public image is available 
```

Available tags are listed [here](https://github.com/samfisherirl/Geo3D_Manager)

## Side Project

If you don't want to create functions each time for each purpose, Please check out [pythonista-chromeless](https://github.com/samfisherirl/Geo3D_Manager)
# Selenium Tests

This is minimum demo of headless chrome and selenium on container 
 

- Python 3.9.15
- chromium 107.0.5304.0
- chromedriver 107.0.5304.62
- selenium 4.6.0


## Running the demo

```bash
$ npm install -g serverless # skip this line if you have already installed Serverless Framework
$ export AWS_REGION=ap-northeast-1 # You can specify region or skip this line. us-east-1 will be used by default.
$ sls create --template-url "https://github.com/samfisherirl/docker-selenium-lambda/tree/main" --path docker-selenium-lambda && cd $_
$ sls deploy
$ sls invoke --function demo # Yay! You will get texts of example.com
```

If your goal is to use selenium to download files instead of just scraping content from web pages, then
you will need to specify a `download_dir` when initializing the WebDriverWrapper. Your download location 
should be a writable Lambda directory such as `/tmp`. For example, the first code in 
`lambda_handler` would become 

```python
driver = WebDriverWrapper(download_location='/tmp')
```
If your goal is to use selenium to download files rather than just scrape content from web pages, then
you will need to specify a `download_dir` when initializing the WebDriverWrapper. Your download location
it must be a writable Lambda directory, for example `/ tmp`. For example, enter the first code
`lambda_handler` would become

`` python
driver = WebDriverWrapper (download_location = '/ tmp')
``

This causes file downloads to be automatically downloaded to the "download_location" without
require a confirmation dialog. You may need to let the manager sleep until the file is downloaded
because this happens asynchronously.

To download a file from a link that opens in a new tab (e.g. `target = '_ blank'`), you need to
call `enable_download_in_headless_chrome` in your scraping script after switching to the desired page, but before
click to download. This will replace all `target = '_ blank'` with` target =' _ self'`. For instance:

`` python
# Go to the download page
driver._driver.find_element_by_xpath ('// a [@href = "/ downloads /"]'). click ()
# Enable headless Chrome file download
driver.enable_download_in_headless_chrome ()
# Click the download link
driver._driver.find_element_by_class_name ("btn"). click ()
``

```python
# Navigate to download page
driver._driver.find_element_by_xpath('//a[@href="/downloads/"]').click()
# Enable headless chrome file download
driver.enable_download_in_headless_chrome()
# Click the download link
driver._driver.find_element_by_class_name("btn").click()
```
```

Available tags are listed [here](https://hub.docker.com/r/samfisherirl/aws-lambda-selenium-python/tags)
 
