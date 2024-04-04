import json

def load_data():
    try:
        with open("youtube.txt","r") as file:
            test= json.load(file)
            # print(test)
            # print(type(test))
            return test
        
    except FileNotFoundError:
        return []


def save_data_helper(videos):
    with open("youtube.txt", "w") as file:
        json.dump(videos, file)



def list_all_videos(videos):
    print("\n")
    print("*"*50)
    for index, vid in enumerate(videos, start=1): # enumerate is used to get index and loop on the list
        print(f'{index} {vid["name"]}, Duration: {vid["time"]} ')

    print("\n")
    print("*"*70)

def add_video(videos):
    name = input("Enter video name: ")
    time = input("Enter video time: ")
    videos.append({'name': name, 'time': time})
    save_data_helper(videos)

def update_video(videos):
    list_all_videos(videos)
    index = int(input("Enter index to be updated"))
    if 1<= index <= len(videos):
        name = input("Enter the new name to be updated ")
        time = input("Enter the new time to be updated ")
        videos[index-1]={'name':name,'time':time}
        save_data_helper(videos)



def delete_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number to be deleted"))

    if 1<= index <= len(videos):
        del videos[index-1]
        save_data_helper(videos)

def main():
    videos = load_data()

    while True:
        print("\n Youtube Manager")
        print("1. List a favourite vidoes ")
        print("2. Add a youtube video")
        print("3. Update a youtube video details")
        print("4. Delete a youtube video")
        print("5. Exit the app")
        choice = input("Enter your choice: ")
        # print(videos)

        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case _:
                print("Invalid choice")


if __name__== "__main__":
    main()


