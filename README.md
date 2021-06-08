A Discord bot in Python that allows users to store and retrieve information from a cloud MySQL database using in-server commands.

Commands:

.addCollection "collection name" "category name..."
Creates a new collection. Requires 1 collection name and at least 1 category name (all collections are automatically created with a unique ID category).
Ex. .addCollection Waypoints Name

.lsCollection
Lists all the collections. Requires nothing.
Ex. .getItem Waypoints Name House X-Coordinate 30

.rmCollection "collection name"
Deletes the collection. Requires 1 collection name.
Ex. .rmCollection Waypoints

.addCat "collection name" "category name..."
Adds a new category to the collection. Requires 1 collection name and at least 1 category name.
Singular Ex. .addCat Waypoints X-Coordinate
Multiple Ex. .addCat Waypoints X-Coordinate Y-Coordinate Z-Coordinate

.lsCat "collection name"
Lists all categories in the collection. Requires 1 collection name.
Ex. .lsCat Waypoints

.rmCat "collection name" "category name..."
Removes a category from the collection. Requires 1 collection name and at least 1 category name (not recommended to remove ID category).
Singular Ex. .rmCat Waypoints X-Coordinate
Multiple Ex. .rmCat Waypoints X-Coordinate Y-Coordinate Z-Coordinate

.addItem "collection name" "Category Value..."
Adds item(s) to the collection. Requires 1 collection name and 1 category value for each category in the collection (excluding unique ID) for each item you are trying to add.
Singular Ex. .addItem Waypoints House 30 30 30
Multiple Ex. addItem Waypoints House 30 30 30 Farm 40 40 40

.lsItem "collection name"
Gets all items from the collection. Requires 1 collection name
Ex. .getAll Waypoints

.findItem "collection name" "category name" "category value"
Finds item(s) that meet certain search critera from the collection. Requires 1 collection name and at least 1 category name and corresponding category value.
Singular Ex. .getItem Waypoints Name House
Multiple Ex. .getItem Waypoints Name House X-Coordinate 30

.updItem "collection name" "ID" "category name..." "category value..."
Updates the category value(s) for specific item. Requires 1 collection name and at least 1 category name and corresponding category value. To find the ID, please use .findItem.
Singular Ex. .updItem Waypoints 1 X-Coordinate 35
Multiple Ex. .updItem Waypoints 1 X-Coordinate 35 Y-Coordinate 35

.rmItem "collection name" "ID"
Removes item(s) at the specified IDs. Requires 1 collection name and 1 ID for each item you are trying to remove. To find the ID, please use .findItem.
Singular Ex. .rmItem Waypoints 1
Multiple Ex. .rmItem Waypoints 1 3 5 7

.clearItem "collection name"
Removes all items in the collection. Requires 1 collection name.
Ex. .clearCollection Waypoints
