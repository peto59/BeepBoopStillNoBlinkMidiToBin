from basic_pitch.inference import predict_and_save, predict
from basic_pitch import ICASSP_2022_MODEL_PATH
import scipy.signal

# predict_and_save(
#     "./",
#     "out/",
#     True,
#     True,
#     False,
#     False,
#     ICASSP_2022_MODEL_PATH
# )
model_output, midi_data, note_events = predict("in.mp3", ICASSP_2022_MODEL_PATH)