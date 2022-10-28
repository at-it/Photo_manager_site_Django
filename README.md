## Further developments needed:
- Performance improvement of loading images from website to database (asynchronous adding of the width/height once database is loaded?)

## Assumptions:
- Initialization of the database pulls only 30 photos due to demo nature of this app
- Recognition of the dominant color in the photo works for RGB pictures - 4bit examples from website are omitted in the code
- There is certain amount of randomness in getting the dominant color due to the clusteroid initialization in machine learning model