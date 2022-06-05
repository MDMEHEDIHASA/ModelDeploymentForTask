modelAPiDeploy.py file use for testing the model through postman.

Also you can see the test result through this image.

![api](https://user-images.githubusercontent.com/48857205/172041250-00d6e057-a7ce-4211-81f0-6b72a4046873.PNG)

To use this model and test  it on your dekstop first of all download the folder. Then open the folder in your dekstop. Then open commandprompt

from this folder then run this command in the command prompt which is: python modelApiDeploy.py

After run this open postman and make a post request through this: http://127.0.0.1:5000/predict

Then in the body of postman with raw json file use this value or you can change the value but column name must be same:
[{"ApplicantIncome":5667,"CoapplicantIncome":0,"LoanAmount":131,"Loan_Amount_Term":360, "Credit_History":1,"Gender_Male":1,
       "Married_Yes":0, "Dependents_1":1,"Dependents_2":0,"Dependents_3+":0, "Education_Not Graduate":0,"Self_Employed_Yes":0,
       "Property_Area_Semiurban":0, "Property_Area_Urban":1}]


After sending this you can see the output predict value.

You can see my final result is this: {
    "prediction": "[0]"
}