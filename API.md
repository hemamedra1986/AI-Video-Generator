# API Documentation

## Endpoints

### 1. Generate Video
- **POST /api/generate-video**  
  - Description: Generates a video based on the provided parameters.  
  - Request Body:  
    - `title`: The title of the video (string)  
    - `description`: A brief description of the video content (string)  
    - `duration`: The duration of the video in seconds (integer)  
    - `templateId`: The ID of the template to use (string)  

### 2. Get Video Status
- **GET /api/video-status/{videoId}**  
  - Description: Retrieve the status of a specific video generation process.  
  - Path Parameters:  
    - `videoId`: The ID of the video (string)  

### 3. Get All Videos
- **GET /api/videos**  
  - Description: Retrieve a list of all generated videos.  

### 4. Delete Video
- **DELETE /api/delete-video/{videoId}**  
  - Description: Deletes a specific video.  
  - Path Parameters:  
    - `videoId`: The ID of the video (string) 

## Response Format

All API responses will be in JSON format. 

### Example Response
```json
{
  "status": "success",
  "data": { 
    "videoId": "123456",
    "title": "My Video Title",
    "status": "completed"
  }
}
```

## Error Handling

In case of an error, the response will include an `error` object with the details. For example:
```json
{
  "status": "error",
  "error": "Video not found"
}
```