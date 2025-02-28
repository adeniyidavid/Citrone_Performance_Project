import numpy as np
import pickle
import streamlit as st

loaded_model = pickle.load(open("citrone_deployment_model.pkl", 'rb'))

def performance_prediction(input_data):
    # input_data = (45, 36, 29, 25, False, False, 1)

    #converted to array
    input_data_array = np.asarray(input_data)
    # input_data_array.shape

    #reshape so the model can understand it
    input_data_reshape = input_data_array.reshape(1, -1)
    # loaded_model.predict(input_data_reshape)

    # Getting a prediction 
    prediction = loaded_model.predict(input_data_reshape)

    if prediction[0] == 0:
        return("This student is not eligible")
    else:
        return("Passed")

def main():
    # giving the app a title
    st.title('Citrone performance Web App')

    # getting input data from the user
    Quiz_summary = st.text_input("Quiz_summary score")
    Assignment_summary = st.text_input("Assignment summary score")
    Grade_point_average = st.text_input("Learner's Grade point Average")
    Age = st.text_input("Learner's Age")
    Children = st.text_input(
        "Does leaner have child/children ? 1 for Yes/0 for No"
    )
    Completed_NYSC = st.text_input("completed NYSC ? 1 for Yes/0 for No")
    Gender = st.text_input("Learner's Gender ? 1 for Male/0 for Female")

    performance = ""

    if st.button("Eligibity Result"):
        performance = performance_prediction(
            [float(Quiz_summary), float(Assignment_summary), float(Grade_point_average), int(Age), 
             int(Children), int(Completed_NYSC), int(Gender)]
        )
        st.success(performance)

if __name__ == "__main__":
        main()