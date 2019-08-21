# IIIT Cloud Server
Written in **Python(flask)**, this server scrapes the Mandaar 2.0 server and returns an JSON object depending upon the request. Simply put, this is an **unofficial API** for the Mandaar UMS 2.0.  
This server is hosted in IIIT bhubaneswar and is accessible on the IP `14.139.198.171`.(false...use localhost)    

# API Endpoints
### 1. login test
* ##### Verifies user credentials.  
  + > Request URL: localhost/api/hibi/login_test
  + > Request Method: POST
  + > Form Data
    + 'uid':'userID'
    + 'pwd :'pass@123'
   + Returns JSON object **`{"return":"success"}` on successful authentication and `{"return":"failed"}`** otherwise.  
  
### 2. login
* ##### Returns 50 most recent notices.
  + > Request URL: localhost/api/hibi/notice
  + > Request Method: POST
  + > Form Data
    + 'uid':'userID'
    + 'pwd :'pass@123'
  + Returns JSON object **`{"Notices":[{"date":"dd-mm-yyyy","title":"Lorem Ipsum","id":"0000","id_link":"dummyLink.php","posted_by":"XYZ","attention":"XYZ"} , ....49 }]}`**

### 3. notice_data
* ##### Returns notice data in HTML format.
  + > Request URL: http://14.139.198.171/api/hibi/notice_data
  + > Request Method: POST
  + > Form Data
    + 'uid':'userID'
    + 'pwd :'pass@123'
    + 'id':0000
  + Returns JSON object **`{"Notices":[{"html":".....html content......"},{"link":"............."]}`**
