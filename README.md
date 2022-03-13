# Fask-Docker-Machine_Learning

# Adopting Machine Learning Model by and flask and docker

![image](https://user-images.githubusercontent.com/82649993/158072280-fb9ef993-452d-40ec-a190-915bc82c2705.png)

![image](https://user-images.githubusercontent.com/82649993/158072301-0c4c0a9a-9cc5-489c-8b45-b61933f9331d.png)

![image](https://user-images.githubusercontent.com/82649993/158072341-80842944-7730-483d-a08a-bf16419f00d8.png)


# Stage 1: ML Stage
 Machine Learning Model Training and Saving:
  Its a Banknote Authentication usecase and the csv dataset is labelled with 0 and 1..0 stands for no authentication and 1 stands for authentication.
  
CSV structure is as follows:

![image](https://user-images.githubusercontent.com/82649993/158071523-36525b2c-ea56-4ba9-8556-9784b95ec358.png)

And the accuracy of Random Forest Classifier in 99 % which perhaps overfitting could be finetuned in code level.Saved Model is saved in sorce foilder as "Classifier.pkl"

# Stage 2: Flask and POSTMAN
Flask App is developed to contain Inference of ML model along with HTTP request "GET" and "POST" Methods.

![image](https://user-images.githubusercontent.com/82649993/158071653-8a66202a-5db4-4e1c-a90e-75dd52e262c5.png)

In Order to Check the outputs "POSTMAN" is used.


![image](https://user-images.githubusercontent.com/82649993/158071709-be91a345-d652-4cee-b55c-60b78c6390e0.png)

# Stage 3: Flask with Flasgger

Now Flask APP is come up with Flasgger Front end which could be seen at http:............/apidocs

![image](https://user-images.githubusercontent.com/82649993/158071802-7cbfd2a2-fba9-4efa-af36-8c117a5d1d61.png)
![image](https://user-images.githubusercontent.com/82649993/158071826-3fcb550e-160a-44b5-8e18-96bdd4842463.png)
![image](https://user-images.githubusercontent.com/82649993/158071849-cf78265a-6875-4d19-893e-13ca34ef0cba.png)

# Stage4 : Dockerize the whole (Flask and Flasgger)
Now, Docker Commands are,

![image](https://user-images.githubusercontent.com/82649993/158071912-6b216a44-9f84-4490-9c76-fa90fd6effdc.png)

And the build commands are,
AT Powershell, 

# 1.Navigate to the root folder>>>>>>>>>>> example: PS C:\Users\Welcome\Desktop\Imp\newcode\flask_docker>
# 2.Build the Imgae >>>>>>example:   docker build -t banknote_authentication_api .
# 3.After the build>>> Run the Image>>>>example:  docker run -p 8000:8000 banknote_authentication_api

![image](https://user-images.githubusercontent.com/82649993/158072044-387b2d5f-9d7b-42b8-940d-764b9a69f92a.png)

Even though the port here mentioned is  http://172.17.0.2:8000/ , the app is opening at http://192.168.18.13:8000/apidocs/ .Pls be aware......
