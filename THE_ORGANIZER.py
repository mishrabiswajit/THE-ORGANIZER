import os
from time import sleep

# ALL THE EXT DATABASES
img_ext = [
    ".3dm",
    ".3ds",
    ".max",
    ".bmp",
    ".dds",
    ".gif",
    ".jpg",
    ".jpeg",
    ".png",
    ".psd",
    ".xcf",
    ".tga",
    ".thm",
    ".tif",
    ".tiff",
    ".yuv",
    ".ai",
    ".eps",
    ".ps",
    ".svg",
    ".dwg",
    ".dxf",
    ".gpx",
    ".kml",
    ".kmz",
    ".webp",
]
doc_ext = [
    ".doc",
    ".docx",
    ".pptx",
    ".htm",
    ".odt",
    ".pdf",
    ".xls",
    ".xlsx",
    ".ods",
    ".ppt",
    ".txt",
]

video_ext = [
    ".3g2",
    ".3gp",
    ".aaf",
    ".asf",
    ".avchd",
    ".avi",
    ".drc",
    ".flv",
    ".m2v",
    ".m4p",
    ".m4v",
    ".mkv",
    ".mng",
    ".mov",
    ".mp2",
    ".mp4",
    ".mpe",
    ".mpeg",
    ".mpg",
    ".mpv",
    ".mxf",
    ".nsv",
    ".ogg",
    ".ogv",
    ".ogm",
    ".qt",
    ".rm",
    ".rmvb",
    ".roq",
    ".srt",
    ".svi",
    ".vob",
    ".webm",
    ".wmv",
    ".yuv",
]

audio_ext = [
    ".aac",
    ".aiff",
    ".ape",
    ".au",
    ".flac",
    ".gsm",
    ".it",
    ".m3u",
    ".m4a",
    ".mid",
    ".mod",
    ".mp3",
    ".mpa",
    ".pls",
    ".ra",
    ".s3m",
    ".sid",
    ".wav",
    ".wma",
    ".xm",
]

archive_ext = [
    ".7z",
    ".a",
    ".apk",
    ".ar",
    ".bz2",
    ".cab",
    ".cpio",
    ".deb",
    ".dmg",
    ".egg",
    ".gz",
    ".iso",
    ".jar",
    ".lha",
    ".mar",
    ".pea",
    ".rar",
    ".rpm",
    ".s7z",
    ".shar",
    ".tar",
    ".tbz2",
    ".tgz",
    ".tlz",
    ".war",
    ".whl",
    ".xpi",
    ".zip",
    ".zipx",
    ".xz",
    ".pak",
]

book_ext = [
    ".mobi",
    ".epub",
    ".azw1",
    ".azw3",
    ".azw4",
    ".azw6",
    ".azw",
    ".cbr",
    ".cbz",
]

code_ext = [
    ".1.ada",
    ".2.ada",
    ".ada",
    ".adb",
    ".ads",
    ".asm",
    ".bas",
    ".bash",
    ".bat",
    ".c",
    ".c++",
    ".cbl",
    ".cc",
    ".class",
    ".clj",
    ".cob",
    ".cpp",
    ".cs",
    ".csh",
    ".cxx",
    ".d",
    ".diff",
    ".e",
    ".el",
    ".f",
    ".f77",
    ".f90",
    ".fish",
    ".for",
    ".fth",
    ".ftn",
    ".go",
    ".groovy",
    ".h",
    ".hh",
    ".hpp",
    ".hs",
    ".html",
    ".htm",
    ".hxx",
    ".java",
    ".js",
    ".jsx",
    ".jsp",
    ".ksh",
    ".kt",
    ".lhs",
    ".lisp",
    ".lua",
    ".m",
    ".m4",
    ".nim",
    ".patch",
    ".php",
    ".pl",
    ".po",
    ".pp",
    ".py",
    ".r",
    ".rb",
    ".rs",
    ".s",
    ".scala",
    ".sh",
    ".swg",
    ".swift",
    ".v",
    ".vb",
    ".vcxproj",
    ".xcodeproj",
    ".xml",
    ".zsh",
]

directory_path = """"""

# FILE LIST
files = os.listdir()


# ALL FUNCTIONS
def arrange_images():
    try:
        images = [
            file for file in files if os.path.splitext(file)[1].lower() in img_ext
        ]
        print("\nSearching for Images", end="")
        for i in range(10):
            print(".", end="", flush=True)
            sleep(0.2)
        print("Done")
        if len(images) == 0:
            print("No images found !!")
        else:
            print(f"Found {len(images)} images !!")
            print("\nSearching for 'Images' directory", end="")
            for i in range(10):
                print(".", end="", flush=True)
                sleep(0.2)
            if os.path.exists("Images") == False:
                print("Not Found !!\nSo creating", end="")
                for i in range(10):
                    print(".", end="", flush=True)
                sleep(0.2)
                os.mkdir("Images")
                print("Done!!")
            else:
                print("Found !!")
            for item in images:
                os.replace(item, f"Images/{item}")
            print(f"Successfully Moved {len(images)} image files in 'Images' folder")
    except Exception as error:
        print(f"\nI have encountered an unexpected error :(\nError : {error}")
        print(
            "\n\nTips :-\n1.Try restarting this program\n.Open this program as administrator or sudo"
        )


def arrange_docs():
    try:
        documents = [
            file for file in files if os.path.splitext(file)[1].lower() in doc_ext
        ]
        print("\nSearching for Documents", end="")
        for i in range(10):
            print(".", end="", flush=True)
            sleep(0.2)
        print("Done")
        if len(documents) == 0:
            print("No documents found !!")
        else:
            print(f"Found {len(documents)} documents !!")
            print("\nSearching for 'Documents' directory", end="")
            for i in range(10):
                print(".", end="", flush=True)
                sleep(0.2)
            if os.path.exists("Documents") == False:
                print("Not Found !!\nSo creating", end="")
                for i in range(10):
                    print(".", end="", flush=True)
                sleep(0.2)
                os.mkdir("Documents")
                print("Done!!")
            else:
                print("Found !!")
            for item in documents:
                os.replace(item, f"Documents/{item}")
            print(
                f"Successfully Moved {len(documents)} document files in 'Documents' folder"
            )
    except Exception as error:
        print(f"\nI have encountered an unexpected error :(\nError : {error}")
        print(
            "\n\nTips :-\n1.Try restarting this program\n.Open this program as administrator or sudo"
        )


def arrange_videos():
    try:
        videos = [
            file for file in files if os.path.splitext(file)[1].lower() in video_ext
        ]
        print("\nSearching for Videos", end="")
        for i in range(10):
            print(".", end="", flush=True)
            sleep(0.2)
        print("Done")
        if len(videos) == 0:
            print("No videos found !!")
        else:
            print(f"Found {len(videos)} videos !!")
            print("\nSearching for 'Videos' directory", end="")
            for i in range(10):
                print(".", end="", flush=True)
                sleep(0.2)
            if os.path.exists("Videos") == False:
                print("Not Found !!\nSo creating", end="")
                for i in range(10):
                    print(".", end="", flush=True)
                sleep(0.2)
                os.mkdir("Videos")
                print("Done !!")
            for item in videos:
                os.replace(item, f"Videos/{item}")
            print(f"Successfully Moved {len(videos)} videos files in 'Videos' folder")
    except Exception as error:
        print(f"\nI have encountered an unexpected error :(\nError : {error}")
        print(
            "\n\nTips :-\n1.Try restarting this program\n.Open this program as administrator or sudo"
        )


def arrange_audios():
    try:
        audios = [
            file for file in files if os.path.splitext(file)[1].lower() in audio_ext
        ]
        print("\nSearching for Audios", end="")
        for i in range(10):
            print(".", end="", flush=True)
            sleep(0.2)
        print("Done")
        if len(audios) == 0:
            print("No audio found !!")
        else:
            print(f"Found {len(audios)} audios !!")
            print("\nSearching for 'Audios' directory", end="")
            for i in range(10):
                print(".", end="", flush=True)
                sleep(0.2)
            if os.path.exists("Audios") == False:
                print("Not Found !!\nSo creating", end="")
                for i in range(10):
                    print(".", end="", flush=True)
                sleep(0.2)
                os.mkdir("Audios")
                print("Done !!")
            else:
                print("Found !!")
            for item in audios:
                os.replace(item, f"Audios/{item}")
            print(f"Successfully Moved {len(audios)} audios files in 'Audios' folder")
    except Exception as error:
        print(f"\nI have encountered an unexpected error :(\nError : {error}")
        print(
            "\n\nTips :-\n1.Try restarting this program\n.Open this program as administrator or sudo"
        )


def arrange_archives():
    try:
        archives = [
            file for file in files if os.path.splitext(file)[1].lower() in archive_ext
        ]
        print("\nSearching for Archives", end="")
        for i in range(10):
            print(".", end="", flush=True)
            sleep(0.2)
        print("Done")
        if len(archives) == 0:
            print("No archives found !!")
        else:
            print(f"Found {len(archives)} archives !!")
            print("\nSearching for 'Archives' directory", end="")
            for i in range(10):
                print(".", end="", flush=True)
                sleep(0.2)
            if os.path.exists("Archives") == False:
                print("Not Found !!\nSo creating", end="")
                for i in range(10):
                    print(".", end="", flush=True)
                sleep(0.2)
                os.mkdir("Archives")
                print("Done !!")
            for item in archives:
                os.replace(item, f"Archives/{item}")
            print(
                f"Successfully Moved {len(archives)} archive files in 'Archives' folder"
            )
    except Exception as error:
        print(f"\nI have encountered an unexpected error :(\nError : {error}")
        print(
            "\n\nTips :-\n1.Try restarting this program\n.Open this program as administrator or sudo"
        )


def arrange_books():
    try:
        books = [
            file for file in files if os.path.splitext(file)[1].lower() in book_ext
        ]
        print("\nSearching for Books", end="")
        for i in range(10):
            print(".", end="", flush=True)
            sleep(0.2)
        print("Done")
        if len(books) == 0:
            print("No books found !!")
        else:
            print(f"Found {len(books)} books !!")
            print("\nSearching for 'Books' directory", end="")
            for i in range(10):
                print(".", end="", flush=True)
                sleep(0.2)
            if os.path.exists("Books") == False:
                print("Not Found !!\nSo creating", end="")
                for i in range(10):
                    print(".", end="", flush=True)
                sleep(0.2)
                os.mkdir("Books")
                print("Done !!")
            for item in books:
                os.replace(item, f"Books/{item}")
            print(f"Successfully Moved {len(books)} books files in 'Books' folder")
    except Exception as error:
        print(f"\nI have encountered an unexpected error :(\nError : {error}")
        print(
            "\n\nTips :-\n1.Try restarting this program\n.Open this program as administrator or sudo"
        )


def arrange_codes():
    try:
        codes = [
            file for file in files if os.path.splitext(file)[1].lower() in code_ext
        ]
        print("\nSearching for Codes", end="")
        for i in range(10):
            print(".", end="", flush=True)
            sleep(0.2)
        print("Done")
        if len(codes) == 0:
            print("No codes found !!")
        else:
            print(f"Found {len(codes)} codes !!")
            print("\nSearching for 'Codes' directory", end="")
            for i in range(10):
                print(".", end="", flush=True)
                sleep(0.2)
            if os.path.exists("Codes") == False:
                print("Not Found !!\nSo creating", end="")
                for i in range(10):
                    print(".", end="", flush=True)
                sleep(0.2)
                os.mkdir("Codes")
                print("Done !!")
            for item in codes:
                os.replace(item, f"Codes/{item}")
            print(f"Successfully Moved {len(codes)} codes files in 'Codes' folder")
    except Exception as error:
        print(f"\nI have encountered an unexpected error :(\nError : {error}")
        print(
            "\n\nTips :-\n1.Try restarting this program\n.Open this program as administrator or sudo"
        )


def arrange_other():
    file_to_be_skipped = ["THE_ORGANIZER.exe", "THE_ORGANIZER.py", "DumpStack.log.tmp"]
    others_ext = []
    try:
        for file in files:
            ext = os.path.splitext(file)[1].lower()
            if (
                (ext not in img_ext)
                and (ext not in doc_ext)
                and (ext not in video_ext)
                and (ext not in audio_ext)
                and (ext not in archive_ext)
                and (ext not in book_ext)
                and (ext not in code_ext)
                and os.path.isfile(file)
                and (os.path.basename(file) not in file_to_be_skipped)
            ):
                others_ext.append(file)
        print("\nSearching for other files", end="")
        for i in range(10):
            print(".", end="", flush=True)
            sleep(0.2)
        print("Done")
        if len(others_ext) == 0:
            print("No others files found !!")
        else:
            print(f"Found {len(others_ext)} others files !!")
            print("\nSearching for 'Others' directory", end="")
            for i in range(10):
                print(".", end="", flush=True)
                sleep(0.2)
            if os.path.exists("Others") == False:
                print("Not Found !!\nSo creating", end="")
                for i in range(10):
                    print(".", end="", flush=True)
                sleep(0.2)
                os.mkdir("Others")
                print("Done !!")
            else:
                print("Found !!")
            for item in others_ext:
                os.replace(item, f"Others/{item}")
            print(
                f"Successfully Moved {len(others_ext)} others files in 'Others' folder"
            )
    except Exception as error:
        print(f"\nI have encountered an unexpected error :(\nError : {error}")
        print(
            "\n\nTips :-\n1.Try restarting this program\n.Open this program as administrator or sudo"
        )


def delete_empty_folder():
    try:
        empty_folders = []
        count = 0
        print("\nSearching for Empty folders", end="")
        for i in range(10):
            print(".", end="", flush=True)
            sleep(0.3)
        for file in files:
            if os.path.isdir(file) == True:
                if len(os.listdir(file)) == 0:
                    empty_folders.append(file)
                    count += 1
                    os.rmdir(file)
        print("Done !!")
        if len(empty_folders) != 0:
            print(f"Successfully deleted {count} empty folders\n")
        else:
            print("No empty folders found !!\n")
    except Exception as error:
        print(f"\nI have encountered an unexpected error :(\nError : {error}")
        print(
            "\n\nTips :-\n1.Try restarting the program with admin rights\n.Open this program as administrator or sudo"
        )


be_organised_text = (
    "\n\n\t\t\t\t THANKS FOR CHOOSING ORGANIZER ^_^\n\t\t\t\t\t #be_organized ✌️"
)
if __name__ == "__main__":
    print(
        "\n\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx WELCOME TO ORGANIZER xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    )
    print("\t\t\t\t\t\t\t\t\t\t   Made by Biswajit Mishra")
    print(
        "\n\nWhat it does --> This is a organizer program which will orgranize all the clutter in your folder\n"
    )
    print("Note : Press 'q' to exit anytime\n")
    print(f"ATTENTION !!\nCurrent working directory is : {os.getcwd()}\n")

    while True:
        user_choice = input(
            "Options Available :- \n\n0. Enter custom file path\n1. Arrange Images\n2. Arrange Documents\n3. Arrange Videos\n4. Arrange Audio Files\n5. Arrange Archive Files \n6. Arrange Books\n7. Arrange Codes\n8. Arrange Other Files \n9. Clear Empty folders \n10. Arrange All File Type\n\nSo BOSS !! What you wanna do ?\nAns : "
        )
        if user_choice.lower() == "q":
            print(be_organised_text)
            break
        elif user_choice == "0":
            directory_path = input(
                "\nEnter the folder path which you want to organize : "
            )
            try:
                os.chdir(directory_path)
                print(f"\nCurrent working directory has been set to : {os.getcwd()}\n")
                files = os.listdir()
            except FileNotFoundError:
                print("\nPlease enter a valid file path\n")
        elif user_choice == "1":
            arrange_images()
            files = os.listdir()
            print(be_organised_text)
        elif user_choice == "2":
            arrange_docs()
            files = os.listdir()
            print(be_organised_text)
        elif user_choice == "3":
            arrange_videos()
            files = os.listdir()
            print(be_organised_text)
        elif user_choice == "4":
            arrange_audios()
            files = os.listdir()
            print(be_organised_text)
        elif user_choice == "5":
            arrange_archives()
            files = os.listdir()
            print(be_organised_text)
        elif user_choice == "6":
            arrange_books()
            files = os.listdir()
            print(be_organised_text)
        elif user_choice == "7":
            arrange_codes()
            files = os.listdir()
            print(be_organised_text)
        elif user_choice == "8":
            arrange_other()
            files = os.listdir()
            print(be_organised_text)
        elif user_choice == "9":
            delete_empty_folder()
            files = os.listdir()
            print(be_organised_text)
        elif user_choice == "10":
            arrange_images()
            arrange_docs()
            arrange_videos()
            arrange_audios()
            arrange_archives()
            arrange_books()
            arrange_codes()
            arrange_other()
            delete_empty_folder()
            files = os.listdir()
            print(be_organised_text)
        else:
            print("\nPlease enter a valid index number from the given options !!\n")
