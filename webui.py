import gradio as gr
import paddlehub as hub
import cv2

# Load the Wav2Lip model from PaddleHub
model = hub.Module(name='wav2lip')

def wav2lip_interface(video, audio):
    # Read the video file
    video_data = cv2.VideoCapture(video.name)
    
    # Read the audio file
    with open(audio.name, "rb") as f:
        audio_data = f.read()
    
    # Perform lip-syncing using Wav2Lip model
    result = model.synthesize(
        video=video_data,
        audio=audio_data,
        save_path='./output/result.mp4',
    )
    
    # Return the synthesized video file
    return './output/result.mp4'

# Define the input and output interfaces
inputs = [
    gr.inputs.Video(type="filepath", label="Video"),
    gr.inputs.Audio(type="filepath", label="Audio")
]
output = gr.outputs.Video(type="file", label="Synthesized Video")

# Create the Gradio interface
interface = gr.Interface(
    fn=wav2lip_interface,
    inputs=inputs,
    outputs=output,
    title="Wav2Lip Interface",
    description="Upload a video and an audio file to generate a lip-synced video.",
    theme="default"
)

# Launch the interface on port 9870
interface.launch(server_port=7895)
