# Interface ConnectionBuilder

**Source:** `java.sql\java\sql\ConnectionBuilder.html`

### Class Description

```java
public interface
ConnectionBuilder
```

A builder created from a

DataSource

object,
used to establish a connection to the database that the

data source

object represents. The connection
properties that were specified for the

data source

are used as the
default values by the

ConnectionBuilder

.

The following example illustrates the use of

ConnectionBuilder

to create a

Connection

:

```java
DataSource ds = new MyDataSource();
ShardingKey superShardingKey = ds.createShardingKeyBuilder()
.subkey("EASTERN_REGION", JDBCType.VARCHAR)
.build();
ShardingKey shardingKey = ds.createShardingKeyBuilder()
.subkey("PITTSBURGH_BRANCH", JDBCType.VARCHAR)
.build();
Connection con = ds.createConnectionBuilder()
.user("rafa")
.password("tennis")
.setShardingKey(shardingKey)
.setSuperShardingKey(superShardingKey)
.build();
```

**Since:** 9

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### ConnectionBuilder
user​(
String
username)

Specifies the username to be used when creating a connection

**Parameters:**
- username

- the database user on whose behalf the connection is being
made

**Returns:**
- the same

ConnectionBuilder

instance

---

#### ConnectionBuilder
password​(
String
password)

Specifies the password to be used when creating a connection

**Parameters:**
- password

- the password to use for this connection. May be

null

**Returns:**
- the same

ConnectionBuilder

instance

---

#### ConnectionBuilder
shardingKey​(
ShardingKey
shardingKey)

Specifies a

shardingKey

to be used when creating a connection

**Parameters:**
- shardingKey

- the ShardingKey. May be

null

**Returns:**
- the same

ConnectionBuilder

instance

**See Also:**
- ShardingKey

,

ShardingKeyBuilder

---

#### ConnectionBuilder
superShardingKey​(
ShardingKey
superShardingKey)

Specifies a

superShardingKey

to be used when creating a connection

**Parameters:**
- superShardingKey

- the SuperShardingKey. May be

null

**Returns:**
- the same

ConnectionBuilder

instance

**See Also:**
- ShardingKey

,

ShardingKeyBuilder

---

#### Connection
build()
throws
SQLException

Returns an instance of the object defined by this builder.

**Returns:**
- The built object

**Throws:**
- SQLException

- If an error occurs building the object

---

### Additional Sections

#### Interface ConnectionBuilder

```java
public interface
ConnectionBuilder
```

A builder created from a

DataSource

object,
used to establish a connection to the database that the

data source

object represents. The connection
properties that were specified for the

data source

are used as the
default values by the

ConnectionBuilder

.

The following example illustrates the use of

ConnectionBuilder

to create a

Connection

:

```java
DataSource ds = new MyDataSource();
ShardingKey superShardingKey = ds.createShardingKeyBuilder()
.subkey("EASTERN_REGION", JDBCType.VARCHAR)
.build();
ShardingKey shardingKey = ds.createShardingKeyBuilder()
.subkey("PITTSBURGH_BRANCH", JDBCType.VARCHAR)
.build();
Connection con = ds.createConnectionBuilder()
.user("rafa")
.password("tennis")
.setShardingKey(shardingKey)
.setSuperShardingKey(superShardingKey)
.build();
```

**Since:** 9

public interface

ConnectionBuilder

A builder created from a

DataSource

object,
used to establish a connection to the database that the

data source

object represents. The connection
properties that were specified for the

data source

are used as the
default values by the

ConnectionBuilder

.

The following example illustrates the use of

ConnectionBuilder

to create a

Connection

:

```java
DataSource ds = new MyDataSource();
ShardingKey superShardingKey = ds.createShardingKeyBuilder()
.subkey("EASTERN_REGION", JDBCType.VARCHAR)
.build();
ShardingKey shardingKey = ds.createShardingKeyBuilder()
.subkey("PITTSBURGH_BRANCH", JDBCType.VARCHAR)
.build();
Connection con = ds.createConnectionBuilder()
.user("rafa")
.password("tennis")
.setShardingKey(shardingKey)
.setSuperShardingKey(superShardingKey)
.build();
```

The following example illustrates the use of

ConnectionBuilder

to create a

Connection

:

```java
DataSource ds = new MyDataSource();
ShardingKey superShardingKey = ds.createShardingKeyBuilder()
.subkey("EASTERN_REGION", JDBCType.VARCHAR)
.build();
ShardingKey shardingKey = ds.createShardingKeyBuilder()
.subkey("PITTSBURGH_BRANCH", JDBCType.VARCHAR)
.build();
Connection con = ds.createConnectionBuilder()
.user("rafa")
.password("tennis")
.setShardingKey(shardingKey)
.setSuperShardingKey(superShardingKey)
.build();
```

DataSource ds = new MyDataSource();
ShardingKey superShardingKey = ds.createShardingKeyBuilder()
.subkey("EASTERN_REGION", JDBCType.VARCHAR)
.build();
ShardingKey shardingKey = ds.createShardingKeyBuilder()
.subkey("PITTSBURGH_BRANCH", JDBCType.VARCHAR)
.build();
Connection con = ds.createConnectionBuilder()
.user("rafa")
.password("tennis")
.setShardingKey(shardingKey)
.setSuperShardingKey(superShardingKey)
.build();

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Connection

build

()

Returns an instance of the object defined by this builder.

ConnectionBuilder

password

​(

String

password)

Specifies the password to be used when creating a connection

ConnectionBuilder

shardingKey

​(

ShardingKey

shardingKey)

Specifies a

shardingKey

to be used when creating a connection

ConnectionBuilder

superShardingKey

​(

ShardingKey

superShardingKey)

Specifies a

superShardingKey

to be used when creating a connection

ConnectionBuilder

user

​(

String

username)

Specifies the username to be used when creating a connection

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Connection

build

()

Returns an instance of the object defined by this builder.

ConnectionBuilder

password

​(

String

password)

Specifies the password to be used when creating a connection

ConnectionBuilder

shardingKey

​(

ShardingKey

shardingKey)

Specifies a

shardingKey

to be used when creating a connection

ConnectionBuilder

superShardingKey

​(

ShardingKey

superShardingKey)

Specifies a

superShardingKey

to be used when creating a connection

ConnectionBuilder

user

​(

String

username)

Specifies the username to be used when creating a connection

---

#### Method Summary

Returns an instance of the object defined by this builder.

Specifies the password to be used when creating a connection

Specifies a

shardingKey

to be used when creating a connection

Specifies a

superShardingKey

to be used when creating a connection

Specifies the username to be used when creating a connection

============ METHOD DETAIL ==========

- Method Detail

- user

```java
ConnectionBuilder
user​(
String
username)
```

Specifies the username to be used when creating a connection

**Parameters:** username

- the database user on whose behalf the connection is being
made
**Returns:** the same

ConnectionBuilder

instance

- password

```java
ConnectionBuilder
password​(
String
password)
```

Specifies the password to be used when creating a connection

**Parameters:** password

- the password to use for this connection. May be

null
**Returns:** the same

ConnectionBuilder

instance

- shardingKey

```java
ConnectionBuilder
shardingKey​(
ShardingKey
shardingKey)
```

Specifies a

shardingKey

to be used when creating a connection

**Parameters:** shardingKey

- the ShardingKey. May be

null
**Returns:** the same

ConnectionBuilder

instance
**See Also:** ShardingKey

,

ShardingKeyBuilder

- superShardingKey

```java
ConnectionBuilder
superShardingKey​(
ShardingKey
superShardingKey)
```

Specifies a

superShardingKey

to be used when creating a connection

**Parameters:** superShardingKey

- the SuperShardingKey. May be

null
**Returns:** the same

ConnectionBuilder

instance
**See Also:** ShardingKey

,

ShardingKeyBuilder

- build

```java
Connection
build()
throws
SQLException
```

Returns an instance of the object defined by this builder.

**Returns:** The built object
**Throws:** SQLException

- If an error occurs building the object

Method Detail

- user

```java
ConnectionBuilder
user​(
String
username)
```

Specifies the username to be used when creating a connection

**Parameters:** username

- the database user on whose behalf the connection is being
made
**Returns:** the same

ConnectionBuilder

instance

- password

```java
ConnectionBuilder
password​(
String
password)
```

Specifies the password to be used when creating a connection

**Parameters:** password

- the password to use for this connection. May be

null
**Returns:** the same

ConnectionBuilder

instance

- shardingKey

```java
ConnectionBuilder
shardingKey​(
ShardingKey
shardingKey)
```

Specifies a

shardingKey

to be used when creating a connection

**Parameters:** shardingKey

- the ShardingKey. May be

null
**Returns:** the same

ConnectionBuilder

instance
**See Also:** ShardingKey

,

ShardingKeyBuilder

- superShardingKey

```java
ConnectionBuilder
superShardingKey​(
ShardingKey
superShardingKey)
```

Specifies a

superShardingKey

to be used when creating a connection

**Parameters:** superShardingKey

- the SuperShardingKey. May be

null
**Returns:** the same

ConnectionBuilder

instance
**See Also:** ShardingKey

,

ShardingKeyBuilder

- build

```java
Connection
build()
throws
SQLException
```

Returns an instance of the object defined by this builder.

**Returns:** The built object
**Throws:** SQLException

- If an error occurs building the object

---

#### Method Detail

user

```java
ConnectionBuilder
user​(
String
username)
```

Specifies the username to be used when creating a connection

**Parameters:** username

- the database user on whose behalf the connection is being
made
**Returns:** the same

ConnectionBuilder

instance

---

#### user

ConnectionBuilder

user​(

String

username)

Specifies the username to be used when creating a connection

password

```java
ConnectionBuilder
password​(
String
password)
```

Specifies the password to be used when creating a connection

**Parameters:** password

- the password to use for this connection. May be

null
**Returns:** the same

ConnectionBuilder

instance

---

#### password

ConnectionBuilder

password​(

String

password)

Specifies the password to be used when creating a connection

shardingKey

```java
ConnectionBuilder
shardingKey​(
ShardingKey
shardingKey)
```

Specifies a

shardingKey

to be used when creating a connection

**Parameters:** shardingKey

- the ShardingKey. May be

null
**Returns:** the same

ConnectionBuilder

instance
**See Also:** ShardingKey

,

ShardingKeyBuilder

---

#### shardingKey

ConnectionBuilder

shardingKey​(

ShardingKey

shardingKey)

Specifies a

shardingKey

to be used when creating a connection

superShardingKey

```java
ConnectionBuilder
superShardingKey​(
ShardingKey
superShardingKey)
```

Specifies a

superShardingKey

to be used when creating a connection

**Parameters:** superShardingKey

- the SuperShardingKey. May be

null
**Returns:** the same

ConnectionBuilder

instance
**See Also:** ShardingKey

,

ShardingKeyBuilder

---

#### superShardingKey

ConnectionBuilder

superShardingKey​(

ShardingKey

superShardingKey)

Specifies a

superShardingKey

to be used when creating a connection

build

```java
Connection
build()
throws
SQLException
```

Returns an instance of the object defined by this builder.

**Returns:** The built object
**Throws:** SQLException

- If an error occurs building the object

---

#### build

Connection

build()
throws

SQLException

Returns an instance of the object defined by this builder.

---

