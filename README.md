<p align="center"><a href="https://akkupy.tech"><img src="https://www.involve.me/assets/images/blog/how-to-create-a-simple-price-calculator-and-capture-more-leads/calculator-M.png" width="500"></a></p> 
<h1 align="center"><b>Calculator And Number Function </b></h1>
<h3 align="center">A Webapp Calculator!</h3>
<h4 align="center">Based on Python Flask</h4>



# Deploying To Heroku

[![Deploy To Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/akkupy/Calculator_Num_Function)


# Steps To Follow On Heroku

 * Click Deploy To Heroku
 * Fill up the App name
 * Deploy
 * Wait for the deployment
 * Check if your site works on going to https://{app-name}.herokuapp.com!


# Self-hosting (For Devs)

## Simply clone the repository and run the main file:
```sh
# Install Git First // (Else You Can Download And Upload to Your Local Server)
$ git clone https://github.com/akkupy/Calculator_Num_Function
# Open Git Cloned File
$ cd Calculator_Num_Function
# Config Virtual Env (Skip is already Done.)
$ virtualenv -p /usr/bin/python3 venv
$ . ./venv/bin/activate
# Install All Requirements.
$ pip(3) install -r requirements.txt
# Start Service
$ python(3) -m app
```
