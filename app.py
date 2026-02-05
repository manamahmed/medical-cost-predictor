import gradio as gr
import numpy as np
import pandas as pd
import pickle


#Load the model
with open("medical_gb_pipeline.pkl", "rb") as file:
    model = pickle.load(file)


#Main logic
def predict_cost(age, sex, bmi, children, smoker, region):

    input_df = pd.DataFrame(
        [
            [age, sex, bmi, children, smoker, region]
        ],
        columns=['age', 'sex', 'bmi', 'children', 'smoker', 'region']
    )


    #Prediction
    prediction = model.predict(input_df)[0]
    return f"Prediction medical cost: {prediction : .2f}$"

inputs = [
    gr.Number(label="Age"),
    gr.Radio(["Male", "Female"], label="Gender"),
    gr.Number(label="BMI"),
    gr.Number(label="Children"),
    gr.Radio(["yes", "no"], label="Smoker"),
    gr.Dropdown(['southwest', 'southeast', 'northwest', 'northeast'], label='Region')
]


#Interface

app = gr.Interface(
    fn=predict_cost,
    inputs=inputs,
    outputs="text",
    title="Medical Insurance Cost Predictor"
)


#Launching
app.launch(share=True)