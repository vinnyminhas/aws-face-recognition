import boto3

if __name__ == "__main__":

    # bucket='bucket'
    collectionId='ESL'
    photo = open(r'test\1.jpeg', "rb")
    threshold = 70
    maxFaces=1

    client=boto3.client('rekognition', region_name='ap-south-1')

  
    response=client.search_faces_by_image(CollectionId=collectionId,
                                Image={'Bytes': photo.read()},
                                FaceMatchThreshold=threshold,
                                MaxFaces=maxFaces)

                                
    faceMatches=response['FaceMatches']
    print ('Matching faces')
    for match in faceMatches:
            print ('FaceId:' + match['Face']['FaceId'])
            print ('Similarity: ' + "{:.2f}".format(match['Similarity']) + "%")
            print ('ExternalID: ' + match['Face']['ExternalImageId'])