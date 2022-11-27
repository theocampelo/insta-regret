# insta-regret (python instagram tools)

Just messing around with Instagram web requests.

## Usage

Basic usage of the -c (comment) function. Do -h for help.

```bash
python3 main.py -c <post_url> "Comment goes here" 
```

### TO DO
* Maintain session logged in (logging in multiple times gets you banned)
* Re-implement "spam" function (multiple comments; e.g. for giveaways)

### Notes
* Storing & loading your current.session with pickle doesn't work
* To make a second request you must log in again (remove tokens/current.session file) - to be fixed