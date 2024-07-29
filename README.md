# anonymize
This is a spark code base, written in python with support of multiple workflows.  

Data-anonymize
  3 functions are provided to anonymize the data 
  replace
  replace_with_regex
  sha256 
  You can configure these based on your own requirement, this is maintained in config/anonymize.py
          ```json
          {
              "read_path": "file:///app/data/original/",
              "anonymizer_config": [
                  {
                      "method": "sha256",
                      "parameters": {
                          "column_name": "first_name"
                      }
                  },
                  {
                      "method": "replace",
                      "parameters": {
                          "column_name": "last_name",
                          "replace_to": "****"
                      }
                  },
                  {
                      "method": "replace_with_regex",
                      "parameters": {
                          "column_name": "address",
                          "replace_from_regex": "R\\d",
                          "replace_to": "*"
                      }
                  }
              ],
              "sink_path": "file:///app/data/anonymize/"
          }
          ```
  
  read_path :  from where to read the csv data 
  sink_path :  where to write the anonymize data

Data Generator : 
  Data generator function is responsible for generating fake data. It can be configed in config/data_generator.py

      {
        "number_of_records": 1000, 
        "columns": ["first_name", "last_name", "address", "date_of_birth"],  # can be extended further
        "sink_path": "file:///app/data/original/"
      }
  number_of_records: change the record num
  cols : columns to be added # dynamic support not added
  sink_path : write location


Workflows :
  1.generate_and_anonymize : generate fake data and anonymize ***recommended to use this 
  2.generate  : if only need to generate record
  3.anonymize : if only to anonymize data

How to run?
  1. run build.sh, it will create a dist folder
  2. cd dist
  3. docker build -t anonymize .
  4. docker run -v "$(pwd)/data:/app/data" anonymize
  5. A new folder will be created named data, which will contain anonymize and original data.

<img width="1640" alt="image" src="https://github.com/user-attachments/assets/e9f906d3-5302-4dc7-8a91-f53710f52583">

