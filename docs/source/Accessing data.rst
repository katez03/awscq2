Accessing Data
==============

This section provides details about how to interact with the core data storage and retrieval system using the **lumache** module. The module is responsible for fetching and processing data, which can be accessed and manipulated using its functions.

The following functions in the **lumache** module are available for accessing and processing data:

.. autosummary::
   :toctree: generated

   lumache.get_data
   lumache.process_data

## Functions

### get_data()
The `get_data()` function retrieves data from the database. It is used to fetch stored data for analysis, reporting, or presentation in the application. This function supports various filters and queries to allow users to fetch exactly the data they need.

**Parameters**:
- `filter`: (optional) A dictionary containing conditions to filter the data.
- `limit`: (optional) Integer specifying the number of records to retrieve.
- `sort`: (optional) A field by which to sort the results.

**Returns**:
- A list of data records in JSON format, representing the fetched data from the database.

**Example**:
```python
from lumache import get_data

# Fetch all data with a limit of 10 records
data = get_data(limit=10)

# Fetch data with a filter for a specific category
data = get_data(filter={"category": "technology"})
