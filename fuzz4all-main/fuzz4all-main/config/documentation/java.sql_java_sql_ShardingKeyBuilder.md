# Interface ShardingKeyBuilder

**Source:** `java.sql\java\sql\ShardingKeyBuilder.html`

### Class Description

```java
public interface
ShardingKeyBuilder
```

A builder created from a

DataSource

or

XADataSource

object,
used to create a

ShardingKey

with sub-keys of supported data types.
Implementations must
support JDBCType.VARCHAR and may also support additional data types.

The following example illustrates the use of

ShardingKeyBuilder

to
create a

ShardingKey

:

```java
DataSource ds = new MyDataSource();
ShardingKey shardingKey = ds.createShardingKeyBuilder()
.subkey("abc", JDBCType.VARCHAR)
.subkey(94002, JDBCType.INTEGER)
.build();
```

**Since:** 9

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### ShardingKeyBuilder
subkey​(
Object
subkey,

SQLType
subkeyType)

This method will be called to add a subkey into a Sharding Key object being
built. The order in which subkey method is called is important as it
indicates the order of placement of the subkey within the Sharding Key.

**Parameters:**
- subkey

- contains the object that needs to be part of shard sub key
- subkeyType

- sub-key data type of type java.sql.SQLType

**Returns:**
- this builder object

---

#### ShardingKey
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

#### Interface ShardingKeyBuilder

```java
public interface
ShardingKeyBuilder
```

A builder created from a

DataSource

or

XADataSource

object,
used to create a

ShardingKey

with sub-keys of supported data types.
Implementations must
support JDBCType.VARCHAR and may also support additional data types.

The following example illustrates the use of

ShardingKeyBuilder

to
create a

ShardingKey

:

```java
DataSource ds = new MyDataSource();
ShardingKey shardingKey = ds.createShardingKeyBuilder()
.subkey("abc", JDBCType.VARCHAR)
.subkey(94002, JDBCType.INTEGER)
.build();
```

**Since:** 9

public interface

ShardingKeyBuilder

A builder created from a

DataSource

or

XADataSource

object,
used to create a

ShardingKey

with sub-keys of supported data types.
Implementations must
support JDBCType.VARCHAR and may also support additional data types.

The following example illustrates the use of

ShardingKeyBuilder

to
create a

ShardingKey

:

```java
DataSource ds = new MyDataSource();
ShardingKey shardingKey = ds.createShardingKeyBuilder()
.subkey("abc", JDBCType.VARCHAR)
.subkey(94002, JDBCType.INTEGER)
.build();
```

The following example illustrates the use of

ShardingKeyBuilder

to
create a

ShardingKey

:

```java
DataSource ds = new MyDataSource();
ShardingKey shardingKey = ds.createShardingKeyBuilder()
.subkey("abc", JDBCType.VARCHAR)
.subkey(94002, JDBCType.INTEGER)
.build();
```

DataSource ds = new MyDataSource();
ShardingKey shardingKey = ds.createShardingKeyBuilder()
.subkey("abc", JDBCType.VARCHAR)
.subkey(94002, JDBCType.INTEGER)
.build();

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

ShardingKey

build

()

Returns an instance of the object defined by this builder.

ShardingKeyBuilder

subkey

​(

Object

subkey,

SQLType

subkeyType)

This method will be called to add a subkey into a Sharding Key object being
built.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

ShardingKey

build

()

Returns an instance of the object defined by this builder.

ShardingKeyBuilder

subkey

​(

Object

subkey,

SQLType

subkeyType)

This method will be called to add a subkey into a Sharding Key object being
built.

---

#### Method Summary

Returns an instance of the object defined by this builder.

This method will be called to add a subkey into a Sharding Key object being
built.

============ METHOD DETAIL ==========

- Method Detail

- subkey

```java
ShardingKeyBuilder
subkey​(
Object
subkey,

SQLType
subkeyType)
```

This method will be called to add a subkey into a Sharding Key object being
built. The order in which subkey method is called is important as it
indicates the order of placement of the subkey within the Sharding Key.

**Parameters:** subkey

- contains the object that needs to be part of shard sub key
**Parameters:** subkeyType

- sub-key data type of type java.sql.SQLType
**Returns:** this builder object

- build

```java
ShardingKey
build()
throws
SQLException
```

Returns an instance of the object defined by this builder.

**Returns:** The built object
**Throws:** SQLException

- If an error occurs building the object

Method Detail

- subkey

```java
ShardingKeyBuilder
subkey​(
Object
subkey,

SQLType
subkeyType)
```

This method will be called to add a subkey into a Sharding Key object being
built. The order in which subkey method is called is important as it
indicates the order of placement of the subkey within the Sharding Key.

**Parameters:** subkey

- contains the object that needs to be part of shard sub key
**Parameters:** subkeyType

- sub-key data type of type java.sql.SQLType
**Returns:** this builder object

- build

```java
ShardingKey
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

subkey

```java
ShardingKeyBuilder
subkey​(
Object
subkey,

SQLType
subkeyType)
```

This method will be called to add a subkey into a Sharding Key object being
built. The order in which subkey method is called is important as it
indicates the order of placement of the subkey within the Sharding Key.

**Parameters:** subkey

- contains the object that needs to be part of shard sub key
**Parameters:** subkeyType

- sub-key data type of type java.sql.SQLType
**Returns:** this builder object

---

#### subkey

ShardingKeyBuilder

subkey​(

Object

subkey,

SQLType

subkeyType)

This method will be called to add a subkey into a Sharding Key object being
built. The order in which subkey method is called is important as it
indicates the order of placement of the subkey within the Sharding Key.

build

```java
ShardingKey
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

ShardingKey

build()
throws

SQLException

Returns an instance of the object defined by this builder.

---

