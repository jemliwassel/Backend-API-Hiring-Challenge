import argparse
import requests

def main():
    # create a parser for command-line arguments
    parser = argparse.ArgumentParser()

    # add arguments for each of the API actions
    parser.add_argument("--list", action="store_true", help="List all datasets")
    parser.add_argument("--create", type=str, help="Create a new dataset from a CSV file")
    parser.add_argument("--info", type=int, help="Get info for a specific dataset")
    parser.add_argument("--delete", type=int, help="Delete a specific dataset")
    parser.add_argument("--export", type=int, help="Export a specific dataset to an Excel file")
    parser.add_argument("--stats", type=int, help="Get statistics for a specific dataset")
    parser.add_argument("--plot", type=int, help="Get a plot for a specific dataset")
    
    ###################################
    def create_dataset(csv_file):
        # set the API endpoint and the headers for the request
        url = "http://localhost:8000/datasets/"
        # open the CSV file and read its contents
        with open(csv_file, "rb") as f:
            file_content = f.read()

        # create a dictionary with the file data to be sent as part of the request
        data = {"csv_file": (csv_file, file_content, "text/csv")}

        # send a POST request to the API endpoint
        response = requests.post(url,files=data)

        # check the status code of the response
        if response.status_code == 200:
            # if the request was successful, print the id of the new dataset
            print(response.json())
        else:
            # if the request failed, print an error message
            print("Error:", response.status_code)
    ######################################  
      
    def get_dataset_info(id: int):
        # send a GET request to the API endpoint with the ID of the dataset
        response = requests.get("http://localhost:8000/datasets/{id}/")

        # check the status code of the response
        if response.status_code == 200:
            # if the request was successful, print the information for the dataset
            print(response.json())
        else:
            # if the request failed, print an error message
            print("Error:", response.status_code)
    ########################################       
    def list_datasets(): 
        # send a GET request to the API endpoint
        response = requests.get("http://localhost:8000/datasets/")
        # check the status code of the response
        if response.status_code == 200:
            # if the request was successful, print the list of datasets
            print(response.json())
        else:
            #if the request failed, print an error message
            print("Error:", response.status_code)
    ########################################            
    def delete_dataset(id: int):
        # send a DELETE request to the API endpoint with the ID of the dataset
        response = requests.delete("http://localhost:8000/datasets/{id}/")

        # check the status code of the response
        if response.status_code == 204:
            # if the request was successful, print a message indicating that the dataset was deleted
            print(f"Dataset {id} was successfully deleted")
        else:
            # if the request failed, print an error message
            print("Error:", response.status_code)   
    ########################################
    def export_dataset(id: int):
        # set the headers for the request
        headers = {
            "Accept": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        }
        # send a GET request to the API endpoint with the ID of the dataset
        response = requests.get("http://localhost:8000/datasets/{id}/export/", headers=headers)

        # check the status code of the response
        if response.status_code == 200:
            # if the request was successful, write the Excel file to disk
            with open("export.xlsx", "wb") as f:
                f.write(response.content)
            print("Dataset exported successfully")
        else:
            # if the request failed, print an error message
            print("Error:", response.status_code) 
    ######################################## 
    def get_dataset_stats(id: int):
        # send a GET request to the API endpoint with the ID of the dataset
        response = requests.get("http://localhost:8000/datasets/{id}/stats/")

        # check the status code of the response
        if response.status_code == 200:
            # if the request was successful, print the statistics for the dataset
            print(response.json())
        else:
            # if the request failed, print an error message
            print("Error:", response.status_code)
        
    ########################################  
    def get_dataset_plot(id: int):
        # send a GET request to the API endpoint with the ID of the dataset
        # specify that the response should be a PDF file
        headers = {
            "Accept": "application/pdf"
        }
        response = requests.get("http://localhost:8000/datasets/{id}/plot/", headers=headers)

        # check the status code of the response
        if response.status_code == 200:
            # if the request was successful, save the PDF file to disk
            with open("plot.pdf", "wb") as f:
                f.write(response.content)
            print("Plot saved to 'plot.pdf'")
        else:
            # if the request failed, print an error message
            print("Error:", response.status_code)
    ########################################
        
    # parse the command-line arguments
    args = parser.parse_args()

    # perform the action based on the arguments provided
    if args.list:
        list_datasets()
        pass
    elif args.create:
        create_dataset(args.create)
        pass
    elif args.info:
        get_dataset_info(args.info)
        pass
    elif args.delete:
        delete_dataset(args.delete)
        pass
    elif args.export:
        export_dataset(args.export)
        pass
    elif args.stats:
        get_dataset_stats(args.stats)
        pass
    elif args.plot:
        get_dataset_plot(args.plot)
        pass

if __name__ == "__main__":
    main()