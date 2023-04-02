
USBFCD.py


currently there are no  methods within windows to detect or logs files transfered to external stroage devices, this script detects when a file is copied to a USB drive and outputs the relevant events to the Windows Event Log

Checks specifically for files that have been copied to a USB drive. It checks the modified time of each file in the USB drive and compares it to the current time to see if the file was recently modified (within the last 15 seconds).

When a file copy is detected, it logs the event to both a text file and the Windows Event Log using the win32evtlogutil module. The event ID is set to 100, the log type is 'Information', and the event source is 'USB File Copy Detection'.

Note that this code is for Windows systems only and requires the pywin32 library to be installed.
