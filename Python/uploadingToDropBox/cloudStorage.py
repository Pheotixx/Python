import dropbox

class TransferData:
    def __init__(self,access_token):
        self.access_token = access_token

    def upload_file(self,file_from,file_to):
        dbx = dropbox.Dropbox(self.access_token)

        f = open(file_from,'rb')
        dbx.files_upload(f.read(),file_to)

def main():
    access_token = 'sl.A4CehFS5MBTEaDGcGpjQqTpL4iYMkCM3JXAhxwrCql0I3LagxCs_kIuMqC4GwhsHY4n0Dw_YjaNBHKPhpTBb_aqh0KocZLTsCQ4j8dik0-cM5qQ07XYFlAg8NIPHzF1Vx-iB7W0'
    transferData = TransferData(access_token)

    file_from = input("Enter the file path to transfer: ")
    file_to = input("Enter the full path to upload to dropbox: ")

    transferData.upload_file(file_from, file_to)

    print ("File Successfully Uploaded.")


main()
            