import os
import datetime
import random, glob

# Count days
current_day = datetime.datetime.today().weekday()


# Set the directory path for wallpapers
directory_primary = "/home/cyber-syntax/Pictures/justnow/"
directory_sunday = "/home/cyber-syntax/Pictures/Sunday/"

# Is it working day or holiday 
if current_day == 6:
        # If it's Sunday, run this codes
        files_sunday = os.listdir(directory_sunday)
        selected_sunday_wallpaper = random.choice(files_sunday)
        sunday_path = os.path.join(directory_sunday, selected_sunday_wallpaper)
        os.system(f"gsettings set org.gnome.desktop.background picture-uri-dark file:///{sunday_path}")
else:        
    # If it's weekdays and Saturdays, run this codes    
    files_primary = os.listdir(directory_primary)
    selected_primary_wallpaper = random.choice(files_primary)
    primary_path = os.path.join(directory_primary, selected_primary_wallpaper)
    os.system(f"gsettings set org.gnome.desktop.background picture-uri-dark file:///{primary_path}")
        
  
