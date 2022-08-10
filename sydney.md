THESE ARE ALL THE TASK I DID IN ZURI PROJECT PHASE 
project: CHUNK_49

1. I created the ChunkOrder model, this is the model that is responsible for logging user chunk request, this model was later update several times to suit the needs of the project https://github.com/zuri-training/Chunk-File_Proj_team_49/issues/4
2. I worked on the algorithm that is being used to chunk JSON files, the function chunks the JSON and returns valid JSON, it only works with valid structured JSON data https://github.com/zuri-training/Chunk-File_Proj_team_49/pull/42
3. I created a production branch and setup and hosted the chunk-it application on heroku https://github.com/zuri-training/Chunk-File_Proj_team_49/issues/120 this is the current state of the application https://chunk-it.herokuapp.com/ on the heroku server
4. I created signals that delete the zipfile once a chunk order is deleted https://github.com/zuri-training/Chunk-File_Proj_team_49/issues/128
5. I wrote javascript code that routes the user to the zip file location on the server to start the download process, and the redirects the user to the recently chunked files view https://github.com/zuri-training/Chunk-File_Proj_team_49/issues/129
6. Generated the schema diagram for the project using pydot and graphviz https://github.com/zuri-training/Chunk-File_Proj_team_49/blob/main/schema.png
