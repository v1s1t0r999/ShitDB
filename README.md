# ShitDB
> A json database to fix the persistence problem on Heroku using GitHub!!

---

## The problem:
***In Heroku's free dev plan, files are not saved for more than 24 hours (or so). So, a json file will reset, the way it was uploaded, vanishing all the stored data. Rad more [here](https://devcenter.heroku.com/articles/active-storage-on-heroku).***

## Solution:
***Using [ShitDB](https://github.com/v1s1t0r999/ShitDB) and your [GitHub](https://github.com) account, this problem can be fixed!!***
***But, there are other databases too. Using free add-ons like [PostgreSQL](https://elements.heroku.com/addons/heroku-postgresql) or using [MongoDB Atlas](https://www.mongodb.com/developer/how-to/use-atlas-on-heroku), is a way too, and is of-course free.***
***Using JSON storage is quite easy. For beginners, setting up MongoDB or Heroku Postgres addon can be quite a tricky task. This is an easier way!!***


## How?
***As your json file gets updated, it is simultaneously uploaded to a specified repository in your account. On restart of your Heroku Dynos, the data from the json file will be retrieved from your GitHub and saved to the local json file.***



---


## ***THIS WAS MADE BY ME FOR MY [DISCORD BOT](https://dsc.gg/letleaf-the-bot). DO INVITE IT!***


