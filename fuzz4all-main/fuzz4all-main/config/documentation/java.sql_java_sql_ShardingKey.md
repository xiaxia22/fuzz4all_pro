# Interface ShardingKey

**Source:** `java.sql\java\sql\ShardingKey.html`

### Class Description

```java
public interface
ShardingKey
```

Interface used to indicate that this object represents a Sharding Key. A

ShardingKey

instance is only guaranteed to be compatible with the
data source instance that it was derived from. A

ShardingKey

is
created using

ShardingKeyBuilder

.

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

A

ShardingKey

may also be used for specifying a

superShardingKey

. Databases that support composite Sharding may use a

superShardingKey

to specify a additional level of partitioning within
the Shard.

The following example illustrates the use of

ShardingKeyBuilder

to
create a

superShardingKey

for an eastern region with a

ShardingKey

specified for the Pittsburgh branch office:

```java
DataSource ds = new MyDataSource();
ShardingKey superShardingKey = ds.createShardingKeyBuilder()
.subkey("EASTERN_REGION", JDBCType.VARCHAR)
.build();
ShardingKey shardingKey = ds.createShardingKeyBuilder()
.subkey("PITTSBURGH_BRANCH", JDBCType.VARCHAR)
.build();
Connection con = ds.createConnectionBuilder()
.superShardingKey(superShardingKey)
.shardingKey(shardingKey)
.build();
```

**Since:** 9

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

*No entries found.*

### Additional Sections

#### Interface ShardingKey

```java
public interface
ShardingKey
```

Interface used to indicate that this object represents a Sharding Key. A

ShardingKey

instance is only guaranteed to be compatible with the
data source instance that it was derived from. A

ShardingKey

is
created using

ShardingKeyBuilder

.

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

A

ShardingKey

may also be used for specifying a

superShardingKey

. Databases that support composite Sharding may use a

superShardingKey

to specify a additional level of partitioning within
the Shard.

The following example illustrates the use of

ShardingKeyBuilder

to
create a

superShardingKey

for an eastern region with a

ShardingKey

specified for the Pittsburgh branch office:

```java
DataSource ds = new MyDataSource();
ShardingKey superShardingKey = ds.createShardingKeyBuilder()
.subkey("EASTERN_REGION", JDBCType.VARCHAR)
.build();
ShardingKey shardingKey = ds.createShardingKeyBuilder()
.subkey("PITTSBURGH_BRANCH", JDBCType.VARCHAR)
.build();
Connection con = ds.createConnectionBuilder()
.superShardingKey(superShardingKey)
.shardingKey(shardingKey)
.build();
```

**Since:** 9

public interface

ShardingKey

Interface used to indicate that this object represents a Sharding Key. A

ShardingKey

instance is only guaranteed to be compatible with the
data source instance that it was derived from. A

ShardingKey

is
created using

ShardingKeyBuilder

.

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

A

ShardingKey

may also be used for specifying a

superShardingKey

. Databases that support composite Sharding may use a

superShardingKey

to specify a additional level of partitioning within
the Shard.

The following example illustrates the use of

ShardingKeyBuilder

to
create a

superShardingKey

for an eastern region with a

ShardingKey

specified for the Pittsburgh branch office:

```java
DataSource ds = new MyDataSource();
ShardingKey superShardingKey = ds.createShardingKeyBuilder()
.subkey("EASTERN_REGION", JDBCType.VARCHAR)
.build();
ShardingKey shardingKey = ds.createShardingKeyBuilder()
.subkey("PITTSBURGH_BRANCH", JDBCType.VARCHAR)
.build();
Connection con = ds.createConnectionBuilder()
.superShardingKey(superShardingKey)
.shardingKey(shardingKey)
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

A

ShardingKey

may also be used for specifying a

superShardingKey

. Databases that support composite Sharding may use a

superShardingKey

to specify a additional level of partitioning within
the Shard.

The following example illustrates the use of

ShardingKeyBuilder

to
create a

superShardingKey

for an eastern region with a

ShardingKey

specified for the Pittsburgh branch office:

```java
DataSource ds = new MyDataSource();
ShardingKey superShardingKey = ds.createShardingKeyBuilder()
.subkey("EASTERN_REGION", JDBCType.VARCHAR)
.build();
ShardingKey shardingKey = ds.createShardingKeyBuilder()
.subkey("PITTSBURGH_BRANCH", JDBCType.VARCHAR)
.build();
Connection con = ds.createConnectionBuilder()
.superShardingKey(superShardingKey)
.shardingKey(shardingKey)
.build();
```

DataSource ds = new MyDataSource();
ShardingKey shardingKey = ds.createShardingKeyBuilder()
.subkey("abc", JDBCType.VARCHAR)
.subkey(94002, JDBCType.INTEGER)
.build();

A

ShardingKey

may also be used for specifying a

superShardingKey

. Databases that support composite Sharding may use a

superShardingKey

to specify a additional level of partitioning within
the Shard.

The following example illustrates the use of

ShardingKeyBuilder

to
create a

superShardingKey

for an eastern region with a

ShardingKey

specified for the Pittsburgh branch office:

```java
DataSource ds = new MyDataSource();
ShardingKey superShardingKey = ds.createShardingKeyBuilder()
.subkey("EASTERN_REGION", JDBCType.VARCHAR)
.build();
ShardingKey shardingKey = ds.createShardingKeyBuilder()
.subkey("PITTSBURGH_BRANCH", JDBCType.VARCHAR)
.build();
Connection con = ds.createConnectionBuilder()
.superShardingKey(superShardingKey)
.shardingKey(shardingKey)
.build();
```

The following example illustrates the use of

ShardingKeyBuilder

to
create a

superShardingKey

for an eastern region with a

ShardingKey

specified for the Pittsburgh branch office:

```java
DataSource ds = new MyDataSource();
ShardingKey superShardingKey = ds.createShardingKeyBuilder()
.subkey("EASTERN_REGION", JDBCType.VARCHAR)
.build();
ShardingKey shardingKey = ds.createShardingKeyBuilder()
.subkey("PITTSBURGH_BRANCH", JDBCType.VARCHAR)
.build();
Connection con = ds.createConnectionBuilder()
.superShardingKey(superShardingKey)
.shardingKey(shardingKey)
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
.superShardingKey(superShardingKey)
.shardingKey(shardingKey)
.build();

---

