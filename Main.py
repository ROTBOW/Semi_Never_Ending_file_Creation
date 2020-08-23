
## the end is never the end script
## something like small space virus
## 8000 files is what is needed to make 1 gb of data
import os,time

PPath = "/Total_Not_Useless_Data"
download_folder = os.path.expanduser('~')+'/Downloads/'
download_folder_file = download_folder + PPath


def spam(X):
    for i in range (X):
        var1 = "The End "
        num1 = 1 + i
        var2 = ".txt"
        name = var1 + str(num1) + var2
        Y = open(os.path.join(download_folder_file, name), "w+")
        for i in range (99):
                for i in range (20):
                    Y.write("The End Is Never The End Is Never ")
                Y.write("\n")
                for i in range (20):
                    Y.write("The End Is Never The End Is Never ")
                if num1 == 1000:
                    print("12.5% done")
                elif num1 == 2000:
                    print("25% done")
                    
                elif num1 == 3000:
                    print("37.5% done")
                    
                elif num1 == 4000:
                    print("50% done")
                    
                elif num1 == 5000:
                    print("62.5% done")
                    
                elif num1 == 6000:
                    print("75% done")
                    
                elif num1 == 7000:
                    print("87.5% done")
                    
                elif num1 == 8000:
                    print("100% done!")
                    print("program done!")
                    print("check your downloads folder ;)")
                    time.sleep(3.5)
        Y.close()

try:
    path = os.path.join(download_folder, "Total_Not_Useless_Data")
    os.makedirs(path)
except Exception as X:
    print(X)
spam(8000)

