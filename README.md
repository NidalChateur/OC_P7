<center>
AlgoInvest&Trade
</center> 

<p align="center">
  <img src="./icon.png" alt="icon">
</p>
## How do I run the Python script locally ?

#### 1. Install python and pip from the official website

    link : https://www.python.org/downloads/


#### 2. Open the shell

#### 3. Make sure pip is installed

```bash 
pip --version
# If you can see the pip version, then pip is installed correctly.
```


#### 4. Navigate into a work directory (ex "my documents) :

```bash 
# to navigate in a terminal:
  pwd               # print working directory
  ls                # list folder elements
  cd ..             # navigate to the parent folder
  cd 'name_dossier' # navigate to a son folder 
```

#### 5. Create a new folder "algo_invest_trade" where you could clone the repository :

```bash
  mkdir algo_invest_trade
```

#### 6. Navigate to algo_invest_trade/ :

```bash
  cd algo_invest_trade
```

#### 7. Clone the repository :

```bash
  git clone https://github.com/NidalChateur/OC_P7.git
```

#### 8. Create a new virtuel environment through the command :

```bash
  python -m venv env
```

#### 9. Switch on the new virtuel environment you just created it :
```bash
env/Scripts/activate # under Windows
source env/bin/activate # under Mac
```
#### 10. Install required Python packages :

```bash
pip install –r requirements.txt
```
#### 11. Navigate to flake8_report/ :

```bash
  cd flake8_report
```
#### 12. Consult the Flake8 error report :

```bash
  start index.html # under Windows
  open index.html # under Mac
```
#### 13. Generate a new flake8 report :

```bash
cd ..
rm -r ./flake8_report/*
flake8
```

#### 14. Run the script to start algo_invest_trade :

```bash
python main.py

```
#### 15. Notice :

This script reads a '.xlsx' or '.csv' file as input. It contains a list of stock market actions and then returns the most profitable stock portfolio for a given investment amount.

The constraints :
- Each stock can only be purchased once.
- The purchase of fractional shares is not possible.
- A maximum of 500 euros per customer.

The input file format :
- It must be a 'csv' or 'xlsx' file.
- The column A must be named : 'name', all stocks name must be unique
- The column B must be named : 'price', all prices must be numbers
- The column C must be named : 'profit', all profits must be numbers

Place your input file in the folder './input/' before running 'step 2' to be able to select it.

## Feedback/Question

If you have any feedback or questions, please reach out to me at nidalchateur@gmail.com
