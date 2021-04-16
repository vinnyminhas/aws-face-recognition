import boto3
import os


def add_faces_to_collection(photo,ExternalID,collection_id):
    client=boto3.client('rekognition', region_name='ap-south-1')

    response=client.index_faces(CollectionId=collection_id,
                                Image={'Bytes': photo.read()},
                                ExternalImageId=externalID,
                                MaxFaces=1,
                                QualityFilter="AUTO",
                                DetectionAttributes=['ALL'])

    # print ('Results for ' + photo) 	
    print('Faces indexed:')						
    for faceRecord in response['FaceRecords']:
         print('  Face ID: ' + faceRecord['Face']['FaceId'])
         print('  Location: {}'.format(faceRecord['Face']['BoundingBox']))

    print('Faces not indexed:')
    for unindexedFace in response['UnindexedFaces']:
        print(' Location: {}'.format(unindexedFace['FaceDetail']['BoundingBox']))
        print(' Reasons:')
        for reason in unindexedFace['Reasons']:
            print('   ' + reason)
    return len(response['FaceRecords'])


train_dir = os.listdir('dataset/')
collection_id = "ESL" 
for person in train_dir:
    images = os.listdir("dataset/" + person)
    for person_img in images:
        externalID = person
        path = ("dataset/" + person + "/" + person_img)
        photo = open(path, "rb")
        indexed_faces_count=add_faces_to_collection(photo, externalID, collection_id)
        print("Faces indexed count: " + str(indexed_faces_count))

