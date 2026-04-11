# Interface PooledConnectionBuilder

**Source:** `java.sql\javax\sql\PooledConnectionBuilder.html`

### Class Description

```java
public interface
PooledConnectionBuilder
```

A builder created from a

ConnectionPoolDataSource

object,
used to establish a connection to the database that the

data source

object represents. The connection
properties that were specified for the

data source

are used as the
default values by the

PooledConnectionBuilder

.

The following example illustrates the use of

PooledConnectionBuilder

to create a

XAConnection

:

```java
ConnectionPoolDataSource ds = new MyConnectionPoolDataSource();
ShardingKey superShardingKey = ds.createShardingKeyBuilder()
.subkey("EASTERN_REGION", JDBCType.VARCHAR)
.build();
ShardingKey shardingKey = ds.createShardingKeyBuilder()
.subkey("PITTSBURGH_BRANCH", JDBCType.VARCHAR)
.build();
PooledConnection con = ds.createPooledConnectionBuilder()
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

#### PooledConnectionBuilder
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

PooledConnectionBuilder

instance

---

#### PooledConnectionBuilder
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

PooledConnectionBuilder

instance

---

#### PooledConnectionBuilder
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

PooledConnectionBuilder

instance

**See Also:**
- ShardingKey

,

ShardingKeyBuilder

---

#### PooledConnectionBuilder
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

PooledConnectionBuilder

instance

**See Also:**
- ShardingKey

,

ShardingKeyBuilder

---

#### PooledConnection
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

#### Interface PooledConnectionBuilder

```java
public interface
PooledConnectionBuilder
```

A builder created from a

ConnectionPoolDataSource

object,
used to establish a connection to the database that the

data source

object represents. The connection
properties that were specified for the

data source

are used as the
default values by the

PooledConnectionBuilder

.

The following example illustrates the use of

PooledConnectionBuilder

to create a

XAConnection

:

```java
ConnectionPoolDataSource ds = new MyConnectionPoolDataSource();
ShardingKey superShardingKey = ds.createShardingKeyBuilder()
.subkey("EASTERN_REGION", JDBCType.VARCHAR)
.build();
ShardingKey shardingKey = ds.createShardingKeyBuilder()
.subkey("PITTSBURGH_BRANCH", JDBCType.VARCHAR)
.build();
PooledConnection con = ds.createPooledConnectionBuilder()
.user("rafa")
.password("tennis")
.setShardingKey(shardingKey)
.setSuperShardingKey(superShardingKey)
.build();
```

**Since:** 9

public interface

PooledConnectionBuilder

A builder created from a

ConnectionPoolDataSource

object,
used to establish a connection to the database that the

data source

object represents. The connection
properties that were specified for the

data source

are used as the
default values by the

PooledConnectionBuilder

.

The following example illustrates the use of

PooledConnectionBuilder

to create a

XAConnection

:

```java
ConnectionPoolDataSource ds = new MyConnectionPoolDataSource();
ShardingKey superShardingKey = ds.createShardingKeyBuilder()
.subkey("EASTERN_REGION", JDBCType.VARCHAR)
.build();
ShardingKey shardingKey = ds.createShardingKeyBuilder()
.subkey("PITTSBURGH_BRANCH", JDBCType.VARCHAR)
.build();
PooledConnection con = ds.createPooledConnectionBuilder()
.user("rafa")
.password("tennis")
.setShardingKey(shardingKey)
.setSuperShardingKey(superShardingKey)
.build();
```

The following example illustrates the use of

PooledConnectionBuilder

to create a

XAConnection

:

```java
ConnectionPoolDataSource ds = new MyConnectionPoolDataSource();
ShardingKey superShardingKey = ds.createShardingKeyBuilder()
.subkey("EASTERN_REGION", JDBCType.VARCHAR)
.build();
ShardingKey shardingKey = ds.createShardingKeyBuilder()
.subkey("PITTSBURGH_BRANCH", JDBCType.VARCHAR)
.build();
PooledConnection con = ds.createPooledConnectionBuilder()
.user("rafa")
.password("tennis")
.setShardingKey(shardingKey)
.setSuperShardingKey(superShardingKey)
.build();
```

ConnectionPoolDataSource ds = new MyConnectionPoolDataSource();
ShardingKey superShardingKey = ds.createShardingKeyBuilder()
.subkey("EASTERN_REGION", JDBCType.VARCHAR)
.build();
ShardingKey shardingKey = ds.createShardingKeyBuilder()
.subkey("PITTSBURGH_BRANCH", JDBCType.VARCHAR)
.build();
PooledConnection con = ds.createPooledConnectionBuilder()
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

PooledConnection

build

()

Returns an instance of the object defined by this builder.

PooledConnectionBuilder

password

​(

String

password)

Specifies the password to be used when creating a connection

PooledConnectionBuilder

shardingKey

​(

ShardingKey

shardingKey)

Specifies a

shardingKey

to be used when creating a connection

PooledConnectionBuilder

superShardingKey

​(

ShardingKey

superShardingKey)

Specifies a

superShardingKey

to be used when creating a connection

PooledConnectionBuilder

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

PooledConnection

build

()

Returns an instance of the object defined by this builder.

PooledConnectionBuilder

password

​(

String

password)

Specifies the password to be used when creating a connection

PooledConnectionBuilder

shardingKey

​(

ShardingKey

shardingKey)

Specifies a

shardingKey

to be used when creating a connection

PooledConnectionBuilder

superShardingKey

​(

ShardingKey

superShardingKey)

Specifies a

superShardingKey

to be used when creating a connection

PooledConnectionBuilder

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
PooledConnectionBuilder
user​(
String
username)
```

Specifies the username to be used when creating a connection

**Parameters:** username

- the database user on whose behalf the connection is being
made
**Returns:** the same

PooledConnectionBuilder

instance

- password

```java
PooledConnectionBuilder
password​(
String
password)
```

Specifies the password to be used when creating a connection

**Parameters:** password

- the password to use for this connection. May be

null
**Returns:** the same

PooledConnectionBuilder

instance

- shardingKey

```java
PooledConnectionBuilder
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

PooledConnectionBuilder

instance
**See Also:** ShardingKey

,

ShardingKeyBuilder

- superShardingKey

```java
PooledConnectionBuilder
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

PooledConnectionBuilder

instance
**See Also:** ShardingKey

,

ShardingKeyBuilder

- build

```java
PooledConnection
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
PooledConnectionBuilder
user​(
String
username)
```

Specifies the username to be used when creating a connection

**Parameters:** username

- the database user on whose behalf the connection is being
made
**Returns:** the same

PooledConnectionBuilder

instance

- password

```java
PooledConnectionBuilder
password​(
String
password)
```

Specifies the password to be used when creating a connection

**Parameters:** password

- the password to use for this connection. May be

null
**Returns:** the same

PooledConnectionBuilder

instance

- shardingKey

```java
PooledConnectionBuilder
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

PooledConnectionBuilder

instance
**See Also:** ShardingKey

,

ShardingKeyBuilder

- superShardingKey

```java
PooledConnectionBuilder
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

PooledConnectionBuilder

instance
**See Also:** ShardingKey

,

ShardingKeyBuilder

- build

```java
PooledConnection
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
PooledConnectionBuilder
user​(
String
username)
```

Specifies the username to be used when creating a connection

**Parameters:** username

- the database user on whose behalf the connection is being
made
**Returns:** the same

PooledConnectionBuilder

instance

---

#### user

PooledConnectionBuilder

user​(

String

username)

Specifies the username to be used when creating a connection

password

```java
PooledConnectionBuilder
password​(
String
password)
```

Specifies the password to be used when creating a connection

**Parameters:** password

- the password to use for this connection. May be

null
**Returns:** the same

PooledConnectionBuilder

instance

---

#### password

PooledConnectionBuilder

password​(

String

password)

Specifies the password to be used when creating a connection

shardingKey

```java
PooledConnectionBuilder
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

PooledConnectionBuilder

instance
**See Also:** ShardingKey

,

ShardingKeyBuilder

---

#### shardingKey

PooledConnectionBuilder

shardingKey​(

ShardingKey

shardingKey)

Specifies a

shardingKey

to be used when creating a connection

superShardingKey

```java
PooledConnectionBuilder
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

PooledConnectionBuilder

instance
**See Also:** ShardingKey

,

ShardingKeyBuilder

---

#### superShardingKey

PooledConnectionBuilder

superShardingKey​(

ShardingKey

superShardingKey)

Specifies a

superShardingKey

to be used when creating a connection

build

```java
PooledConnection
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

PooledConnection

build()
throws

SQLException

Returns an instance of the object defined by this builder.

---

