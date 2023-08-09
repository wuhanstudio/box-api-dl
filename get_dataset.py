import os
from boxsdk import DevelopmentClient

import logging
logging.getLogger('boxsdk').setLevel(logging.CRITICAL)

client = DevelopmentClient()

root_folder = client.get_shared_item('https://utexas.app.box.com/s/evo96v5md4r8nooma3z17kcnfjzp2wed')
print('Downloading:', root_folder.id, root_folder.name)

folders = []
for folder in root_folder.get_items():
    folders.append(folder)

total_folders = len(folders)
print('Total Folders:', total_folders)

# Download all files individually
for idx, folder in enumerate(folders[:2]):
    os.mkdir(folder.name)
    print(f'Folder {idx+1} of {total_folders}: {folder.name}')
    for item in folder.get_items():
        with open(os.path.join(folder.name, item.name), 'wb') as open_file:
            item.download_to(open_file)
            open_file.close()

# Download all files as a zip
# Not working - Empty zip file
# for folder in folders:
    # name = folder.name
    # items = [item for item in folder.get_items()]

    # output_file = open(name + '.zip', 'wb')
    # status = client.download_zip(name, items, output_file)
    # print(f'The status of the zip download is {status["state"]}')
    # output_file.close()
