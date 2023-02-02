# Le Monde dans la Pocket

<img src="https://user-images.githubusercontent.com/65445960/216357587-069e6154-8fb4-4c95-86ab-51378123dc92.png" alt="Le Monde" height="50"><img src="https://user-images.githubusercontent.com/65445960/216357659-cf699bf3-3f51-49c1-984f-26bb42ed38cf.png" alt="Pocket" height="50">

A small project that allows you to download Le Monde (a French newspaper) articles to Pocket, to read on any device.

Mainly useful for subscriber-only articles, which are not supported by Pocket. LMDLP fetches your selected (unlocked) articles from lemonde.fr, extracts the text and uploads them to a custom server (I used surge.sh). Finally, it uploads the new articles to Pocket via its [API](https://getpocket.com/developer/docs/overview)

## Run the project
- Install surge globally
- Set the variables in main.bat
- Run main.bat
