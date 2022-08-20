import streamlit as st
from audio_feature.audio_featurizer import audio_process, spectrogram_plot
from models.load_model import model_loader
import numpy as np
from pydub import AudioSegment
import os

#importing the models which are saved as .sav file. 
model, encoding = model_loader("Saved_model.sav", "Encodings.sav")

st.sidebar.markdown(
    """<h1 style='text-align: center;color:  #0e76a8;'><a style='text-align: center;color:  #0e76a8;' href="https://www.linkedin.com/in/harish-natarajan-82a4b418b/" target="_blank">Linkedin Profile</a></h1>""",
    unsafe_allow_html=True)
# st.sidebar.markdown("""<h1 style='text-align: center;color: black;' ><a style='text-align: center;color: black;'href="https://github.com/rohankokkula/TEATH" target="_blank">Github Source Code</a></h1>""", unsafe_allow_html=True)

st.sidebar.markdown(
    """<style>body {background-color: #2C3454; background-image: url('https://i2.wp.com/highland-music.com/wp-content/uploads/2016/04/Blue-Background-Music-Headphone-Wallpaper-Picture-HD-Free-298292334-e1459743028815.png?ssl=1'); color:white;}</style><body></body>""",
    unsafe_allow_html=True)
st.markdown(
    """<h1 style='text-align: center; color: white;font-size:60px;margin-top:-50px;'>AUDIO CLASSIFIER</h1><h1 style='text-align: center; color: white;font-size:30px;margin-top:-30px;'>Using Machine Learning</h1>""",
    unsafe_allow_html=True)

# radio = st.sidebar.radio("Select format of audio file", options=['mp3', 'wav'])
#
# if radio == 'wav':
#
#     file = st.sidebar.file_uploader("Upload Audio To Classify", type=["wav"])
#
#     if file is not None:
#         st.markdown(
#             """<h1 style='color:yellow;'>Audio : </h1>""",
#             unsafe_allow_html=True)
#         st.audio(file)
#
#         rad = st.sidebar.radio("Choose Options", options=["Predict", "Spectrogram"])
#
#         # rad = st.sidebar.checkbox(label="Do You want to see the spectrogram ?")
#         if rad == "Predict":
#             if st.button("Classify Audio"):
#                 uploaded_audio = audio_process(file)
#
#                 predictions = model.predict(uploaded_audio)
#
#                 targets = encoding.inverse_transform(np.array(predictions).reshape(1, -1))
#                 #
#                 # st.write(targets[0][0])
#                 #
#                 # st.success(targets[0][0])
#
#                 st.markdown(
#                     f"""<h1 style='color:yellow;'>Prediction : <span style='color:white;'>{targets[0][0]}</span></h1>""",
#                     unsafe_allow_html=True)
#
#         elif rad == "Spectrogram":
#             fig = spectrogram_plot(file)
#             # st.set_option('deprecation.showPyplotGlobalUse', False)
#             st.markdown(
#                 f"""<h1 style='color:yellow;'>Spectrogram : </h1>""",
#                 unsafe_allow_html=True)
#             st.pyplot(fig)
#
#
#
# elif radio == 'mp3':
#     file = st.sidebar.file_uploader("Upload Audio To Classify", type="mp3")
#
#     if file is not None:
#         sound = AudioSegment.from_mp3(file)
#         sound.export("file.wav", format="wav")
#         st.markdown(
#             """<h1 style='color:yellow;'>Audio : </h1>""",
#             unsafe_allow_html=True)
#         a = st.audio(file, format="audio/mp3")
#
#         rad = st.sidebar.radio("Choose Options", options=["Predict", "Spectrogram"])
#
#         # rad = st.sidebar.checkbox(label="Do You want to see the spectrogram ?")
#         if rad == "Predict":
#             if st.button("Classify Audio"):
#                 uploaded_audio = audio_process("file.wav")
#
#                 predictions = model.predict(uploaded_audio)
#
#                 targets = encoding.inverse_transform(np.array(predictions).reshape(1, -1))
#                 #
#                 # st.write(targets[0][0])
#                 #
#                 # st.success(targets[0][0])
#
#                 st.markdown(
#                     f"""<h1 style='color:yellow;'>Prediction : <span style='color:white;'>{targets[0][0]}</span></h1>""",
#                     unsafe_allow_html=True)
#
#         elif rad == "Spectrogram":
#             fig = spectrogram_plot("file.wav")
#             st.set_option('deprecation.showPyplotGlobalUse', False)
#             st.markdown(
#                 f"""<h1 style='color:yellow;'>Spectrogram : </h1>""",
#                 unsafe_allow_html=True)
#             st.pyplot(fig)
#
#         # sound = AudioSegment.from_mp3(file)
#         # st.write("Please Upload in wav form")
#         # st.markdown(
#         #     """<h1 style='color:yellow;'>Audio : </h1>""",
#         #     unsafe_allow_html=True)
#         # st.audio(file)
#
#         os.remove("file.wav")

check = st.sidebar.checkbox('Do you want a demo')

if check:
    rad_test = st.sidebar.radio("Select format of audio file", options=['mp3', 'wav'])

    if rad_test == "mp3":
        rad_file = st.sidebar.radio("Select the name of song", ["Man Out Of Town", "Trumpet Tune"])
        if rad_file == "Man Out Of Town":
            rad = st.sidebar.radio("Choose Options", options=["Predict", "Spectrogram"])
            st.audio("Man Out Of Town.mp3")
            # rad = st.sidebar.checkbox(label="Do You want to see the spectrogram ?")
            if rad == "Predict":
                if st.button("Classify Audio"):
                    uploaded_audio = audio_process("Man Out Of Town.mp3")

                    predictions = model.predict(uploaded_audio)

                    targets = encoding.inverse_transform(np.array(predictions).reshape(1, -1))
                    #
                    # st.write(targets[0][0])
                    #
                    # st.success(targets[0][0])

                    st.markdown(
                        f"""<h1 style='color:yellow;'>Prediction : <span style='color:white;'>{targets[0][0]}</span></h1>""",
                        unsafe_allow_html=True)

            elif rad == "Spectrogram":
                fig = spectrogram_plot("Man Out Of Town.mp3")
                st.set_option('deprecation.showPyplotGlobalUse', False)
                st.markdown(
                    f"""<h1 style='color:yellow;'>Spectrogram : </h1>""",
                    unsafe_allow_html=True)
                st.pyplot(fig)

        elif rad_file == "Trumpet Tune":
            rad = st.sidebar.radio("Choose Options", options=["Predict", "Spectrogram"])
            st.audio("Trumpet Tune.mp3")
            # rad = st.sidebar.checkbox(label="Do You want to see the spectrogram ?")
            if rad == "Predict":
                if st.button("Classify Audio"):
                    uploaded_audio = audio_process("Trumpet Tune.mp3")

                    predictions = model.predict(uploaded_audio)

                    targets = encoding.inverse_transform(np.array(predictions).reshape(1, -1))
                    #
                    # st.write(targets[0][0])
                    #
                    # st.success(targets[0][0])

                    st.markdown(
                        f"""<h1 style='color:yellow;'>Prediction : <span style='color:white;'>{targets[0][0]}</span></h1>""",
                        unsafe_allow_html=True)

            elif rad == "Spectrogram":
                fig = spectrogram_plot("Trumpet Tune.mp3")
                st.set_option('deprecation.showPyplotGlobalUse', False)
                st.markdown(
                    f"""<h1 style='color:yellow;'>Spectrogram : </h1>""",
                    unsafe_allow_html=True)
                st.pyplot(fig)

    elif rad_test == "wav":
        rad_file = st.sidebar.radio("Select the name of song", ["Man Out Of Town", "Trumpet Tune"])
        if rad_file == "Man Out Of Town":
            rad = st.sidebar.radio("Choose Options", options=["Predict", "Spectrogram"])
            st.audio("Man Out Of Town.wav")
            # rad = st.sidebar.checkbox(label="Do You want to see the spectrogram ?")
            if rad == "Predict":
                if st.button("Classify Audio"):
                    uploaded_audio = audio_process("Man Out Of Town.wav")

                    predictions = model.predict(uploaded_audio)

                    targets = encoding.inverse_transform(np.array(predictions).reshape(1, -1))
                    #
                    # st.write(targets[0][0])
                    #
                    # st.success(targets[0][0])

                    st.markdown(
                        f"""<h1 style='color:yellow;'>Prediction : <span style='color:white;'>{targets[0][0]}</span></h1>""",
                        unsafe_allow_html=True)

            elif rad == "Spectrogram":
                fig = spectrogram_plot("Man Out Of Town.wav")
                st.set_option('deprecation.showPyplotGlobalUse', False)
                st.markdown(
                    f"""<h1 style='color:yellow;'>Spectrogram : </h1>""",
                    unsafe_allow_html=True)
                st.pyplot(fig)

        elif rad_file == "Trumpet Tune":
            rad = st.sidebar.radio("Choose Options", options=["Predict", "Spectrogram"])
            st.audio("Trumpet Tune.wav")
            # rad = st.sidebar.checkbox(label="Do You want to see the spectrogram ?")
            if rad == "Predict":
                if st.button("Classify Audio"):
                    uploaded_audio = audio_process("Trumpet Tune.wav")

                    predictions = model.predict(uploaded_audio)

                    targets = encoding.inverse_transform(np.array(predictions).reshape(1, -1))
                    #
                    # st.write(targets[0][0])
                    #
                    # st.success(targets[0][0])

                    st.markdown(
                        f"""<h1 style='color:yellow;'>Prediction : <span style='color:white;'>{targets[0][0]}</span></h1>""",
                        unsafe_allow_html=True)

            elif rad == "Spectrogram":
                fig = spectrogram_plot("Trumpet Tune.wav")
                st.set_option('deprecation.showPyplotGlobalUse', False)
                st.markdown(
                    f"""<h1 style='color:yellow;'>Spectrogram : </h1>""",
                    unsafe_allow_html=True)
                st.pyplot(fig)

else:
    radio = st.sidebar.radio("Select format of audio file", options=['mp3', 'wav']) # Radio to select an audio file type- mp3 or wav

    if radio == 'wav':

        file = st.sidebar.file_uploader("Upload Audio To Classify", type=["wav"]) #Allows to load a wav file

        if file is not None:
            st.markdown(
                """<h1 style='color:yellow;'>Audio : </h1>""",
                unsafe_allow_html=True)
            st.audio(file) # To get an audio player in the webpage

            rad = st.sidebar.radio("Choose Options", options=["Predict", "Spectrogram"])   #Selecr feature Predict or spectogram

            # rad = st.sidebar.checkbox(label="Do You want to see the spectrogram ?")
            if rad == "Predict":
                if st.button("Classify Audio"):
                    uploaded_audio = audio_process(file) # Sends the audio file for audio processing with librosa

                    predictions = model.predict(uploaded_audio)  #Checking audio genre with the model

                    targets = encoding.inverse_transform(np.array(predictions).reshape(1, -1))
                    #
                    # st.write(targets[0][0])
                    #
                    # st.success(targets[0][0])

                    st.markdown(
                        f"""<h1 style='color:yellow;'>Prediction : <span style='color:white;'>{targets[0][0]}</span></h1>""",
                        unsafe_allow_html=True)

            elif rad == "Spectrogram":
                fig = spectrogram_plot(file)
                # st.set_option('deprecation.showPyplotGlobalUse', False)
                st.markdown(
                    f"""<h1 style='color:yellow;'>Spectrogram : </h1>""",
                    unsafe_allow_html=True)
                st.pyplot(fig)



    elif radio == 'mp3':
        file = st.sidebar.file_uploader("Upload Audio To Classify", type="mp3")

        if file is not None:
            sound = AudioSegment.from_mp3(file)
            sound.export("file.wav", format="wav")
            st.markdown(
                """<h1 style='color:yellow;'>Audio : </h1>""",
                unsafe_allow_html=True)
            a = st.audio(file, format="audio/mp3")

            rad = st.sidebar.radio("Choose Options", options=["Predict", "Spectrogram"])

            # rad = st.sidebar.checkbox(label="Do You want to see the spectrogram ?")
            if rad == "Predict":
                if st.button("Classify Audio"):
                    uploaded_audio = audio_process("file.wav")

                    predictions = model.predict(uploaded_audio)

                    targets = encoding.inverse_transform(np.array(predictions).reshape(1, -1))
                    #
                    # st.write(targets[0][0])
                    #
                    # st.success(targets[0][0])

                    st.markdown(
                        f"""<h1 style='color:yellow;'>Prediction : <span style='color:white;'>{targets[0][0]}</span></h1>""",
                        unsafe_allow_html=True)

            elif rad == "Spectrogram":
                fig = spectrogram_plot("file.wav")
                st.set_option('deprecation.showPyplotGlobalUse', False)
                st.markdown(
                    f"""<h1 style='color:yellow;'>Spectrogram : </h1>""",
                    unsafe_allow_html=True)
                st.pyplot(fig)

            # sound = AudioSegment.from_mp3(file)
            # st.write("Please Upload in wav form")
            # st.markdown(
            #     """<h1 style='color:yellow;'>Audio : </h1>""",
            #     unsafe_allow_html=True)
            # st.audio(file)

            os.remove("file.wav")
