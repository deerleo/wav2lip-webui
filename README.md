# Wav2Lip Interface

This is a web interface for PaddleGAN's Wav2Lip model, built using the Gradio library. The interface allows you to upload a video and an audio file to generate a lip-synced video.

## Installation

1. Clone the repository: git clone https://github.com/deerleo/wav2lip-webui.git

2. Navigate to the project directory:
cd wav2lip-webui

3. Install the required dependencies:
pip install gradio paddlepaddle paddlehub opencv-python

Make sure you have PaddlePaddle and PaddleHub installed properly.

## Usage

1. Run the following command to start the interface:

python app.py


2. Open your web browser and visit `http://localhost:9870`.

3. In the interface, click on the "Choose File" button in the "Video" section to upload a video file. The video file should be in a common video format, such as MP4 or AVI.

4. Similarly, click on the "Choose File" button in the "Audio" section to upload an audio file. The audio file should be in a format supported by the Wav2Lip model.

5. After selecting the video and audio files, click on the "Submit" button to start the lip-syncing process.

6. The interface will process the files using the Wav2Lip model and display the synthesized video.

7. You can click on the "Download" button to save the synthesized video to your local machine.

## Customize

If you want to customize the code or make any modifications, you can do so in the `app.py` file. You can modify the interface layout, add additional input fields, or change the styling as per your requirements.

## License

This project is licensed under the [MIT License](LICENSE).

## Author

The Author is Leo Lu(AKA Deer Leo / 小鹿哥), feel free to contact deer leo at l#ll.works.



