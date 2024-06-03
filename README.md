<!-- INSTRUCTIONS

*** The template is using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ].

To modify this Template README for your project follow these steps:
1. Do a search and replace `repo_name` with your repository name.
2. Update `thumbnail.png` image located in the root directory to represent your project.
3. Replace or remove content not relevant to your project.
5. Commit changes once you finish updating README.
-->

<!-- PROJECT LOGO -->

<br />
<div align="center">
  <a href="https://github.com/mottmacdonaldglobal/repo_name">
    <img src="caption.JPG" alt="Logo" >
  </a>

<h3 align="center">EA rainfall API querying tool</h3>

  <p align="center">
    <a href="https://github.com/mottmacdonaldglobal/repo_name"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/mottmacdonaldglobal/repo_name">View Demo</a>
    ·
    <a href="https://github.com/mottmacdonaldglobal/repo_name/issues">Report Bug</a>
    ·
    <a href="https://github.com/mottmacdonaldglobal/repo_name/issues">Request Feature</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#about-the-project">About The Project</a></li>
    <li><a href="#contact">Contact</a></li>
    <li>
      <a href="#getting-started">Getting Started</a>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#license">License</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

As part of the Eurotunnel project, landslide movement is compared to the daily rainfall recorded at the automated __Cherry Gardens__ rain gauge (station reference [_305111_](https://environment.data.gov.uk/flood-monitoring/id/stations/305111.html)), which is operated by the Environment Agency. Approximate gauge location is the blue placemark on aerial photo

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

Use [GitHub Issues](https://github.com/mottmacdonaldglobal/repo_name/issues) to share ideas, feedback, tasks, or spotted bugs in this Repository.
Or get in touch directly with [Yitan Lu](mailto:yitan.lu@mottmac.com) and [Richard Mellor](mailto:Richard.Mellor@mottmac.com).

Project Link: [https://github.com/YitanLu/ukea-rainfall-data-grabber](https://github.com/YitanLu/ukea-rainfall-data-grabber)

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- GETTING STARTED -->

## Repository structure

A jupyter notebook is created from source script in python [rain-maker](https://github.com/YitanLu/ukea-rainfall-data-grabber/rain-maker.py)

Data downloaded for this repository are saved in [data](https://github.com/YitanLu/ukea-rainfall-data-grabber/data)

## Getting Started

<!-- Add instructions specific to your project here. -->

1. Prerequisites - Python 3.9 and libraries

```
    datatime
    pandas
    requests
    csv
    json
```

2. Installation instruction:

    - Install [Git](https://git-scm.com/downloads) or [GitHub Desktop](https://desktop.github.com/)


3. Create a local copy

   Download [latest release](https://docs.github.com/en/repositories/releasing-projects-on-github/viewing-your-repositorys-releases-and-tags#viewing-releases), if none available [clone](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) the repository

 ```
    git clone https://github.com/YitanLu/ukea-rainfall-data-grabber.git
 ```

 4. API documentation

This tool kit is developed based on UK EA's [AIP reference](https://environment.data.gov.uk/flood-monitoring/doc/rainfall). Check regularly any update to the API to modify the script to adapt.

Notes the following implementation in data processing
- **NOTE 1**: the current API has 1000 records limit. Each data is for 15 mintues interval so 1000 records is roughly 10 days. 
- **NOTE 2**: assuming the script is triggered at regular interval <10 days, the new dataframe is appended to the existing dataframe (from csv) to form the data that includes both the new and the old. Also the new dataframe will replace any reading from the old (if any) at the same past recording time. It is expected that the station will take time to verify the latest data.
- **NOTE 2**: the raw data [rawdata.csv](https://github.com/YitanLu/ukea-rainfall-data-grabber/data/rawdata.csv) saves reading of 15mins;  a processed data file does the daily sum and present the cummulative rainfall by date [processe_ddata.csv](https://github.com/YitanLu/ukea-rainfall-data-grabber/data/processed_data.csv). The [processed_data.csv](https://github.com/YitanLu/ukea-rainfall-data-grabber/data/processed_data.csv) only contains data until 3 days ago due to the reason explained in **NOTE 2**.

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- Testing -->
## Testing

Unit testing to be decided

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- Scheduled Task -->
## Scheduled Task 

A `bat` file is prompt the python interpreter to execute the script. 

The `bat` file [scheduled_run.bat](https://github.com/YitanLu/ukea-rainfall-data-grabber/scheduled_run.bat) is included in the repo. User need to modify the bat file with the correct paths:
1. Path to the python interpreter (i.e. following `cd` command in the bat file)
2. Path to teh script (i.e. the local computer path to the [rain-maker](https://github.com/YitanLu/ukea-rainfall-data-grabber/rain-maker.py) script)

Within the windows environment use [Task Scheduler](https://learn.microsoft.com/en-us/windows/win32/taskschd/task-scheduler-start-page) to set the script running at regular interval (e.g., twice per week etc. ).  Answer at this [link](https://stackoverflow.com/a/68674814) provides step to step instructions for setting up a task. Briefly in 4 steps:
1. Setting up:
   
   ![step1](scheduled-task-step1.JPG)

2. Set an action (cmd to run bat file)
   
   ![step2](scheduled-task-step2.JPG)


3. Set trigger (frequecy of running the bat file)
   
   ![step3](scheduled-task-step3.JPG)

4. Check the task schedule is in place
   
   ![step4](scheduled-task-step4.JPG)



<p align="right">(<a href="#top">back to top</a>)</p>

<!-- LICENSE -->
## License

Distributed under the MM License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>
