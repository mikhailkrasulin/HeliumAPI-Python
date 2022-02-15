# HeliumAPI-Python
Unofficial API for [Helium Explorer](https://explorer.helium.com/) written in Python 3.

See more information at: https://docs.helium.com/api

# Installing HeliumAPI-Python:

`pip install HeliumAPI-Python`

# Basic usage:

Just create a `HeliumAPI` object after importing it.

  `from HeliumAPI-Python import HeliumAPI`<br/>
  `api = HeliumAPI()`
  
### Get token supply:
```python
tokensupply = api.getTokenSupply()
  ```
### Get block height:
```python
blockheight = api.getBlockHeight()
  ```
 ### Get block description:
```python
blockdescription = api.getBlockDescription()
  ```
