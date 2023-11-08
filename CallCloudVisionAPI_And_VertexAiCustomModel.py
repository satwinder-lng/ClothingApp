import requests
import base64
import json


def convertImageToBase64(image_path):
    with open(image_path, "rb") as img_file:
        encoded_string = base64.b64encode(img_file.read()).decode('utf-8')
    return encoded_string

def MakeCallToVertexAI_API_ENDPOINT(project_id, endpoint_id, image_path):
    endpoint_url = f"https://us-central1-aiplatform.googleapis.com/v1/projects/{project_id}/locations/us-central1/endpoints/{endpoint_id}:predict"
    
    # Generate the payload
    payload = payload = {
        "instances": [
            {
                "content": convertImageToBase64(image_path)
            }
        ]
    }
    
    # Make the POST request
    access_token = VERTEX_AI_ACCESS_TOKEN  # Replace with the access token or use your method to retrieve it
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }

    # Sending the request
    response = requests.post(endpoint_url, headers=headers, json=payload)
    
    if response.status_code == 200:
        print("Request successful!")
        print(json.dumps(response.json(),indent=4))
    else:
        print("Request failed with status code:", response.status_code)


def MakeCallToCloudVisionAPI(image_path):
    
    endpoint = f"https://vision.googleapis.com/v1/images:annotate?key={CLOUD_VISION_API_KEY}"

    headers = {
        "Content-Type": "application/json"
    }

    payload = {
        "requests": [
            {
                "image": {
                    "content": convertImageToBase64(image_path)
                },
                "features": [
                    {"type": "TEXT_DETECTION"},
                    {"type": "LABEL_DETECTION"}
                ]
            }
        ]
    }
    response = requests.post(endpoint, headers=headers, json=payload)
    
    if response.status_code == 200:
        print("Request successful!")
        print(json.dumps(response.json(),indent=4))
    else:
        print("Request failed with status code:", response.status_code)

#region Vertex AI Variables
VERTEX_AI_PROJECT_ID = "756151796035"
VERTEX_AI_ENDPOINT_ID = "4801032915846692864"
VERTEX_AI_ACCESS_TOKEN="ya29.a0AfB_byCYckHhgWwAH9rFi3QBwy6H_GC1x-ypJVO5kebHDwqNPgLxAgJtz_s_Ob6-vmJZWgtu0JAf_SYkb3yKaEJXXvdMBA44RoQo5_v_IhP7DEetVKTJQvt72xLWb-GcLJACa5HAZFPnDZ1qfE7_F-haCHsxOlZpTfpDcuTwLxcaCgYKAfwSARESFQHGX2MiHB5A_VVhuzly6oVU2gwLkg0178"
#endregion

#region Cloud Vision API Variables
CLOUD_VISION_API_KEY="AIzaSyBcHiY47OyOknjJX4ymhOOK2zbYY5Y8fBU"
#endregion

image_path = "D:\ALL DATA\GEN_AI\TEST DATA\images\FloralDress\image1.jpeg"



print(' * * *')
print('######## Cloud Vision API Response START ######')
api_response = MakeCallToCloudVisionAPI(image_path)
print('######## Cloud Vision API Response EN D######')

print('######## Vertex AI API Response START ######')
MakeCallToVertexAI_API_ENDPOINT(VERTEX_AI_PROJECT_ID, VERTEX_AI_ENDPOINT_ID, image_path)
print('######## Vertex AI API Response END ######')