# Interface XAConnectionBuilder

**Source:** `java.sql\javax\sql\XAConnectionBuilder.html`

### Class Description

```java
public interface
XAConnectionBuilder
```

A builder created from a

XADataSource

object,
used to establish a connection to the database that the

data source

object represents. The connection
properties that were specified for the

data source

are used as the
default values by the

XAConnectionBuilder

.

The following example illustrates the use of

XAConnectionBuilder

to create a

XAConnection

:

```java
XADataSource ds = new MyXADataSource();
ShardingKey superShardingKey = ds.createShardingKeyBuilder()
.subkey("EASTERN_REGION", JDBCType.VARCHAR)
.build();
ShardingKey shardingKey = ds.createShardingKeyBuilder()
.subkey("PITTSBURGH_BRANCH", JDBCType.VARCHAR)
.build();
XAConnection con = ds.createXAConnectionBuilder()
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

#### XAConnectionBuilder
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

XAConnectionBuilder

instance

---

#### XAConnectionBuilder
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

XAConnectionBuilder

instance

---

#### XAConnectionBuilder
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

XAConnectionBuilder

instance

**See Also:**
- ShardingKey

,

ShardingKeyBuilder

---

#### XAConnectionBuilder
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

XAConnectionBuilder

instance

**See Also:**
- ShardingKey

,

ShardingKeyBuilder

---

#### XAConnection
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

#### Interface XAConnectionBuilder

```java
public interface
XAConnectionBuilder
```

A builder created from a

XADataSource

object,
used to establish a connection to the database that the

data source

object represents. The connection
properties that were specified for the

data source

are used as the
default values by the

XAConnectionBuilder

.

The following example illustrates the use of

XAConnectionBuilder

to create a

XAConnection

:

```java
XADataSource ds = new MyXADataSource();
ShardingKey superShardingKey = ds.createShardingKeyBuilder()
.subkey("EASTERN_REGION", JDBCType.VARCHAR)
.build();
ShardingKey shardingKey = ds.createShardingKeyBuilder()
.subkey("PITTSBURGH_BRANCH", JDBCType.VARCHAR)
.build();
XAConnection con = ds.createXAConnectionBuilder()
.user("rafa")
.password("tennis")
.setShardingKey(shardingKey)
.setSuperShardingKey(superShardingKey)
.build();
```

**Since:** 9

public interface

XAConnectionBuilder

A builder created from a

XADataSource

object,
used to establish a connection to the database that the

data source

object represents. The connection
properties that were specified for the

data source

are used as the
default values by the

XAConnectionBuilder

.

The following example illustrates the use of

XAConnectionBuilder

to create a

XAConnection

:

```java
XADataSource ds = new MyXADataSource();
ShardingKey superShardingKey = ds.createShardingKeyBuilder()
.subkey("EASTERN_REGION", JDBCType.VARCHAR)
.build();
ShardingKey shardingKey = ds.createShardingKeyBuilder()
.subkey("PITTSBURGH_BRANCH", JDBCType.VARCHAR)
.build();
XAConnection con = ds.createXAConnectionBuilder()
.user("rafa")
.password("tennis")
.setShardingKey(shardingKey)
.setSuperShardingKey(superShardingKey)
.build();
```

The following example illustrates the use of

XAConnectionBuilder

to create a

XAConnection

:

```java
XADataSource ds = new MyXADataSource();
ShardingKey superShardingKey = ds.createShardingKeyBuilder()
.subkey("EASTERN_REGION", JDBCType.VARCHAR)
.build();
ShardingKey shardingKey = ds.createShardingKeyBuilder()
.subkey("PITTSBURGH_BRANCH", JDBCType.VARCHAR)
.build();
XAConnection con = ds.createXAConnectionBuilder()
.user("rafa")
.password("tennis")
.setShardingKey(shardingKey)
.setSuperShardingKey(superShardingKey)
.build();
```

XADataSource ds = new MyXADataSource();
ShardingKey superShardingKey = ds.createShardingKeyBuilder()
.subkey("EASTERN_REGION", JDBCType.VARCHAR)
.build();
ShardingKey shardingKey = ds.createShardingKeyBuilder()
.subkey("PITTSBURGH_BRANCH", JDBCType.VARCHAR)
.build();
XAConnection con = ds.createXAConnectionBuilder()
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

XAConnection

build

()

Returns an instance of the object defined by this builder.

XAConnectionBuilder

password

​(

String

password)

Specifies the password to be used when creating a connection

XAConnectionBuilder

shardingKey

​(

ShardingKey

shardingKey)

Specifies a

shardingKey

to be used when creating a connection

XAConnectionBuilder

superShardingKey

​(

ShardingKey

superShardingKey)

Specifies a

superShardingKey

to be used when creating a connection

XAConnectionBuilder

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

XAConnection

build

()

Returns an instance of the object defined by this builder.

XAConnectionBuilder

password

​(

String

password)

Specifies the password to be used when creating a connection

XAConnectionBuilder

shardingKey

​(

ShardingKey

shardingKey)

Specifies a

shardingKey

to be used when creating a connection

XAConnectionBuilder

superShardingKey

​(

ShardingKey

superShardingKey)

Specifies a

superShardingKey

to be used when creating a connection

XAConnectionBuilder

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
XAConnectionBuilder
user​(
String
username)
```

Specifies the username to be used when creating a connection

**Parameters:** username

- the database user on whose behalf the connection is being
made
**Returns:** the same

XAConnectionBuilder

instance

- password

```java
XAConnectionBuilder
password​(
String
password)
```

Specifies the password to be used when creating a connection

**Parameters:** password

- the password to use for this connection. May be

null
**Returns:** the same

XAConnectionBuilder

instance

- shardingKey

```java
XAConnectionBuilder
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

XAConnectionBuilder

instance
**See Also:** ShardingKey

,

ShardingKeyBuilder

- superShardingKey

```java
XAConnectionBuilder
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

XAConnectionBuilder

instance
**See Also:** ShardingKey

,

ShardingKeyBuilder

- build

```java
XAConnection
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
XAConnectionBuilder
user​(
String
username)
```

Specifies the username to be used when creating a connection

**Parameters:** username

- the database user on whose behalf the connection is being
made
**Returns:** the same

XAConnectionBuilder

instance

- password

```java
XAConnectionBuilder
password​(
String
password)
```

Specifies the password to be used when creating a connection

**Parameters:** password

- the password to use for this connection. May be

null
**Returns:** the same

XAConnectionBuilder

instance

- shardingKey

```java
XAConnectionBuilder
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

XAConnectionBuilder

instance
**See Also:** ShardingKey

,

ShardingKeyBuilder

- superShardingKey

```java
XAConnectionBuilder
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

XAConnectionBuilder

instance
**See Also:** ShardingKey

,

ShardingKeyBuilder

- build

```java
XAConnection
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
XAConnectionBuilder
user​(
String
username)
```

Specifies the username to be used when creating a connection

**Parameters:** username

- the database user on whose behalf the connection is being
made
**Returns:** the same

XAConnectionBuilder

instance

---

#### user

XAConnectionBuilder

user​(

String

username)

Specifies the username to be used when creating a connection

password

```java
XAConnectionBuilder
password​(
String
password)
```

Specifies the password to be used when creating a connection

**Parameters:** password

- the password to use for this connection. May be

null
**Returns:** the same

XAConnectionBuilder

instance

---

#### password

XAConnectionBuilder

password​(

String

password)

Specifies the password to be used when creating a connection

shardingKey

```java
XAConnectionBuilder
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

XAConnectionBuilder

instance
**See Also:** ShardingKey

,

ShardingKeyBuilder

---

#### shardingKey

XAConnectionBuilder

shardingKey​(

ShardingKey

shardingKey)

Specifies a

shardingKey

to be used when creating a connection

superShardingKey

```java
XAConnectionBuilder
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

XAConnectionBuilder

instance
**See Also:** ShardingKey

,

ShardingKeyBuilder

---

#### superShardingKey

XAConnectionBuilder

superShardingKey​(

ShardingKey

superShardingKey)

Specifies a

superShardingKey

to be used when creating a connection

build

```java
XAConnection
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

XAConnection

build()
throws

SQLException

Returns an instance of the object defined by this builder.

---

