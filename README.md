# Backend-API-Hiring-Challenge
This project is a REST API for managing datasets. It allows users to perform different actions on the datasets, such as creating new ones, listing all the available datasets, getting information about a specific dataset, deleting a dataset, exporting a dataset to an Excel file, and getting statistics and plots for a dataset.
Usage
* To start the API server, run the following command: uvicorn main:app --reload
* The API server will be available at http://localhost:8000/.
* To perform an action on a dataset, send a request to the appropriate API endpoint using a tool such as cURL or Postman.

For example, to create a new dataset from a CSV file, send a POST request to the /datasets/ endpoint with the CSV file as the request body: curl -X POST -F "csv_file=@/path/to/file.csv" http://localhost:8000/datasets/
To list all the available datasets, send a GET request to the /datasets/ endpoint: curl http://localhost:8000/datasets/
To get information about a specific dataset, send a GET request to the /datasets/{id}/ endpoint, where {id} is the ID of the dataset: curl http://localhost:8000/datasets/{id}/
To delete a specific dataset, send a DELETE request to the /datasets/{id}/ endpoint, where {id} is the ID of the dataset: curl -X DELETE http://localhost:8000/datasets/{id}/
To export a specific dataset to an Excel file, send a GET request to the /datasets/{id}/excel/ endpoint, where {id} is the ID of the dataset: curl -o data.xlsx http://localhost:8000/datasets/{id}/excel/
To get statistics for a specific dataset, send a GET request to the /datasets/{id}/stats/ endpoint, where {id} is the ID of the dataset.

