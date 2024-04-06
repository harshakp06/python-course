import pymongo
from bson import ObjectId

client = pymongo.MongoClient("mongodb+srv://<username>:<password>@cluster0.qrc3lfm.mongodb.net/")

db = client["ytmanager"]

video_collection = db["videos"]

# print(video_collection)


def list_videos():
    for vid in video_collection.find():
        print(f"ID: {vid['_id']}, Name: {vid['name']} and Time: {vid['time']}")

def add_video(name, time):
    video_collection.insert_one({"name": name,"time":time})
    list_videos()

def update_video(video_id, newname, newtime):
    video_collection.update_one({'_id': ObjectId(video_id)},
                                {'$set':{"name":newname, "time":newtime}})
    list_videos()


def delete_video(vidoe_id):
    video_collection.delete_one({'_id':ObjectId(vidoe_id)})
    list_videos()



def main():
    while True:
        print("\n Youtube manager App ")
        print("1. List all videos ")
        print("2. Add a new video ")
        print("3. Update a video ")
        print("4. Delete a video ")
        print("5. Exit the app ")
        choice = input("Enter your choice: ")

        if choice == "1":
            list_videos()
        elif choice == "2":
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            add_video(name,time)
        elif choice == "3":
            video_id = input("Enter video id name to update: ")
            name = input("Enter the updated video name: ")
            time = input("Enter the updated video time: ")
            update_video(video_id, name, time)
        elif choice=='4':
            video_id = input("Enter video id name to update: ")
            delete_video(video_id)
        elif choice=='5':
            break
        else:
            print("Invalid choice")




if __name__ == "__main__":
    main()