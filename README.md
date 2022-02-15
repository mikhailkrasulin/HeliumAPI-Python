# HeliumAPIpy
Unofficial API for [Helium Explorer](https://explorer.helium.com/) written in Python 3.

See more information at: https://docs.helium.com/api       <p align="center"> <img src="https://dka575ofm4ao0.cloudfront.net/pages-transactional_logos/retina/17932/Roundel_blue.png" width="150" height="150" /></p>
# Installing HeliumAPIpy:

`pip install HeliumAPIpy`

# Basic usage:

Just create a `HeliumAPI` object after importing it.

All data is being returned in `json`.

```python
from HeliumAPIpy import HeliumAPI
api = HeliumAPI()
```
  
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

 ### Get block transactions:
```python
blocktransactions = api.getBlockTranscations('1000000')
  ```

 ### Get richest accounts:
```python
richestaccounts = api.getRichestAccounts()
  ```

 ### Get hotspots by owner address:
```python
gethotspots = api.getHotspotsByOwnerAddress('13AA8PcAZrsojsBVDy2JGEm242nWQeMmRoYaVndtkGy8dNfkn23')
  ```
  
  ### Get activities by address:
```python
getactivities = api.getActivitiesByAddress('13AA8PcAZrsojsBVDy2JGEm242nWQeMmRoYaVndtkGy8dNfkn23')
  ```

   