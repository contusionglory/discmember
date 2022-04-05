<div id="top"></div>


<h3 align="center">DiscMember</h3>
  <p align="center">
    PoC OSINT Discord user and guild information harvester 
    <br />
    <br />
    <br />
    ·
    <a href="https://github.com/contusionglory/discmember/issues">Report Bug</a>
    ·
    <a href="https://github.com/contusionglory/discmember/issues">Request Feature</a>
    ·
    <a href="https://github.com/contusionglory/discmember/pulls">Make a pull requests</a>
  </p>
</div>

<p align="center">
  <img src="https://img.shields.io/github/languages/top/contusionglory/discmember?style=flat-square" </a>
  <img src="https://img.shields.io/github/last-commit/contusionglory/discmember?style=flat-square" </a>
  <img src="https://img.shields.io/github/stars/contusionglory/discmember?color=7F9DE0&label=Stars&style=flat-square" </a>
  <img src="https://img.shields.io/github/forks/contusionglory/discmember?color=7F9DE0&label=Forks&style=flat-square" </a>
</p>

<!-- ABOUT THE PROJECT -->
## 🎯・About The Project

I tried to use [Darvester](https://github.com/V3ntus/darvester) but it was too slow so i made my own version from scratch.
<p align="right">(<a href="#top">back to top</a>)</p>


### Built With

* [python3](https://www.python.org/)

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- GETTING STARTED -->

## 🔥・Features
* Create tables for guild and member
* Scrape:
  * user id
  * avatar id 
  * username 
  * discriminator
  * badge
* Create a mutual guild array in the user tables database 
* Low risk of ban

## 🎇・Getting Started

### 📖・Prerequisites

* Install the requirements
  ```sh
  python3 -m pip install -r .\requirements.txt
  ```
* Edit .env file and put your own discord user token

### ⚙・Installation

1. Get your own discord user token putting this line of code in the dev console in your browser(you need to login to discord first)
  ```js
  (function(){let w=window.open();if(!w||!w.document)return console.error('Unable to get token: popup blocked!');window.dispatchEvent(new Event('beforeunload'));console.log(w.localStorage.token);w.close()}());
  ```
3. Put it in .env file
4. Join some server
5. Insert discord server id and channel id in the cfg.py like this
<img width="1080" alt="img1" src="https://user-images.githubusercontent.com/102427829/161811945-ebf6d7ce-0530-442b-8b9b-45dda3523c23.PNG">
<img width="673" alt="img2" src="https://user-images.githubusercontent.com/102427829/161811954-f25f8c2a-90a9-4f5f-8a8e-7fa9b4b9f84d.PNG">

  ```python
  GUILD_DICTIONARY = { #ID guild/id channel
      '100000000000000000':'11000000000000000',
      '200000000000000000':'220000000000000000',
  }
  ```

6. You can also edit in the same file (cfg.py) the default number of loop and time between loop

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## 🚀・Usage

* Start the program
  ```sh
  python3 main.py
  ```
* Start with argument
  ```sh
  usage: main.py [-h] [-db DATABASE] [-c CYCLE] [-t TIME]

  options:
    -h, --help            show this help message and exit
    -db DATABASE, --database DATABASE
                          Database file name(ex. mydb.db)
    -c CYCLE, --cycle CYCLE
                          Number of time to rescan(Default 0: no rescan)
    -t TIME, --time TIME  Time between rescan(Default 3600s between rescan)
  ```

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ROADMAP -->
## 🎉・Roadmap

- [ ] Find a way to scrape linked account too
- [ ] Fix some ui problem
- [ ] Create a user bot part to search trough the database
- [ ] Fix array of people to not scrape broken

See the [open issues](https://github.com/contusionglory/discmember/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## 🤝・Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
## 📄・License
This project is licensed under the GNU General Public License v3.0 License - see the LICENSE.md file for details


・Educational purpose only and all your consequences caused by you actions is your responsibility


・Selling this **Free** tool is forbidden


・If you make a copy of this/or fork it, it **must** be open-source and have credits linking to this repo



Distributed under the GNU General Public License v3.0 License. See `LICENSE` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>

## 💻・Screenshot

<img src="https://user-images.githubusercontent.com/102427829/161810259-89f0aebb-4dee-48b8-8866-1c4eb289e3b4.PNG">
<hr>
<img src="https://user-images.githubusercontent.com/102427829/161813860-1b820a87-4f15-428e-bbdf-164fcc3cc83b.PNG">
<hr>
<img src="https://user-images.githubusercontent.com/102427829/161813869-c65723f8-4d49-4dcc-a264-f0dee2330adb.PNG">
<hr>
<img src="https://user-images.githubusercontent.com/102427829/161813875-4d92be70-2b6b-4742-9c4c-412fcda893a2.PNG">
<hr>
<img src="https://user-images.githubusercontent.com/102427829/161813885-2b0aa831-8571-4cd0-b8ed-24179213d238.PNG">


## 🌱・Inspiration
DiscMemeber is inspired by V3ntus tool
* [V3ntus/darvester](https://github.com/V3ntus/darvester)



<!-- ACKNOWLEDGMENTS -->
## ❗・DISCLAIMER
Using this tool, you agree not to hold the contributors and developers accountable for any damages that occur. This tool violates Discord terms of service and may result in your access to Discord services terminated. **This tool is for education purpose only you should't use it**

<p align="right">(<a href="#top">back to top</a>)</p>
