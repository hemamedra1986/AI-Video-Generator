# Video Generator Functions

def create_video_from_images(images, output_filename):
    """Creates a video from a list of image filenames."""
    import cv2

    # Read the first image to get dimensions
    first_image = cv2.imread(images[0])
    height, width, layers = first_image.shape

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video = cv2.VideoWriter(output_filename, fourcc, 1, (width, height))

    for image in images:
        image = cv2.imread(image)
        video.write(image)  # Write out frame to video

    video.release()  # Finalize the video
    print(f'Video {output_filename} created successfully.')


def add_audio_to_video(video_filename, audio_filename, output_filename):
    """Adds audio to a video file."""
    from moviepy.editor import VideoFileClip, AudioFileClip

    video = VideoFileClip(video_filename)
    audio = AudioFileClip(audio_filename)
    video = video.set_audio(audio)
    video.write_videofile(output_filename)
    print(f'Video {output_filename} with audio created successfully.')