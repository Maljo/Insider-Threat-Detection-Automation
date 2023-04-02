import os
import logging
import time
import win32evtlogutil
import win32api
import win32file

def detect_usb_drive_file_copy():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s', handlers=[logging.FileHandler('usb_copy_log.txt'), logging.StreamHandler()])
    logging.info('Starting USB file copy detection...')
   
    drive_list = []
    drives = win32api.GetLogicalDriveStrings()
    drives = drives.split('\000')[:-1]
    for drive in drives:
        drive_type = win32file.GetDriveType(drive)
        if drive_type == win32file.DRIVE_REMOVABLE:
            drive_list.append(drive)
   
    while True:
        for drive in drive_list:
            if os.path.exists(drive):
                for dirpath, dirs, files in os.walk(drive):
                    for file in files:
                        if file.endswith('.docx') or file.endswith('.xlsx'):
                            file_path = os.path.join(dirpath, file)
                            modified_time = os.path.getmtime(file_path)
                            event_id = 100
                            event_log_type = 'Information'
                            event_source = 'USB File Copy Detection'
                            event_desc = f'File {file} copied to USB drive {drive} at {time.strftime("%c")}'
                            if modified_time > time.time() - 15:
                                win32evtlogutil.ReportEvent(event_source, event_id, event_log_type, event_desc)
                                logging.info(event_desc)
        time.sleep(10)

if __name__ == '__main__':
    detect_usb_drive_file_copy()
