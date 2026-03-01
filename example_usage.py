# Example Usage of AI Video Generator

"""
This script demonstrates basic usage of the AI Video Generator.
"""

def main():
    # Initialize the AI Video Generator
    video_generator = AIVideoGenerator(api_key='YOUR_API_KEY')
    
    # Define video parameters
    title = 'My AI-Generated Video'
    duration = 60  # Duration in seconds
    resolution = '1080p'
    
    # Generate the video
    video = video_generator.create_video(title=title, duration=duration, resolution=resolution)
    
    # Save the video to a file
    video.save('my_ai_video.mp4')
    
    print('Video generated successfully!')


if __name__ == '__main__':
    main()