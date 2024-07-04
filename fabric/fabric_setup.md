## WSL - Windows Subsystem for Linux

## "Don't Take the Weights out of the Gym"

Can bring up the Ubuntu terminal in the START menu. Or in PowerShell:

```
wsl.exe -d Ubuntu-20.04

```

```
sudo apt update
sudo apt upgrade -y
```


```
sudo update-alternatives --config python3

```

Nasty error fix: https://superuser.com/questions/1803992/getting-this-error-failed-to-take-etc-passwd-lock-invalid-argument

```

sudo mv /var/lib/dpkg/info /var/lib/dpkg/info_silent

sudo mkdir /var/lib/dpkg/info

sudo apt-get update

sudo apt-get -f install

sudo mv /var/lib/dpkg/info/* /var/lib/dpkg/info_silent

sudo rm -rf /var/lib/dpkg/info

sudo mv /var/lib/dpkg/info_silent /var/lib/dpkg/info

sudo apt-get update

sudo apt-get upgrade

```

### Subscribed to ChatGPT & Anthropic

```
https://platform.openai.com/api-keys

https://platform.openai.com/playground/chat?models=gpt-4o

https://console.anthropic.com/dashboard

```

Created a YouTube API Key:

```

https://console.cloud.google.com

```

Did not create a "Google" API key as asked for in: 'fabric --setup'  I skipped it.

Following Network Chuck's tutorial - installed xcel to get pbpaste/pbcopy to work

```

sudo apt install xsel

```

### NOTE:  Use Windows Terminal (Microsoft Store) when using pbpaste - else no worky-worky


Use this command to copy my custom patterns ('sermon_expert') back into the 'patterns' when the get overwritten by an update.
```

cp -r ~/.config/fabric/my_patterns/* ~/.config/fabric/patterns

```

List all the patterns

```

fabric --list

```

Edit the environment file to tell Fabric to save to Obsidian

```

nano ~/.config/fabric/.env
FABRIC_OUTPUT_PATH="/mnt/d/PROJECTS/python/FirstThings/000-INBOX"


```

Export the VM (make a backup)

```

 wsl --export Ubuntu-24.04 "D:\WSL-backups\Ubuntu-24.04-02.tar"

```