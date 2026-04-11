# Class ConfigurationSpi

**Source:** `java.base\javax\security\auth\login\ConfigurationSpi.html`

### Class Description

```java
public abstract class
ConfigurationSpi

extends
Object
```

This class defines the

Service Provider Interface

(

SPI

)
for the

Configuration

class.
All the abstract methods in this class must be implemented by each
service provider who wishes to supply a Configuration implementation.

Subclass implementations of this abstract class must provide
a public constructor that takes a

Configuration.Parameters

object as an input parameter. This constructor also must throw
an IllegalArgumentException if it does not understand the

Configuration.Parameters

input.

**Since:** 1.6

---

### Field Details

*No entries found.*

### Constructor Details

#### public ConfigurationSpi()

*No description found.*

---

### Method Details

#### protected abstract
AppConfigurationEntry
[] engineGetAppConfigurationEntry​(
String
name)

Retrieve the AppConfigurationEntries for the specified

name

.

**Parameters:**
- name

- the name used to index the Configuration.

**Returns:**
- an array of AppConfigurationEntries for the specified

name

, or null if there are no entries.

---

#### protected void engineRefresh()

Refresh and reload the Configuration.

This method causes this Configuration object to refresh/reload its
contents in an implementation-dependent manner.
For example, if this Configuration object stores its entries in a file,
calling

refresh

may cause the file to be re-read.

The default implementation of this method does nothing.
This method should be overridden if a refresh operation is supported
by the implementation.

**Throws:**
- SecurityException

- if the caller does not have permission
to refresh its Configuration.

---

### Additional Sections

#### Class ConfigurationSpi

java.lang.Object

- javax.security.auth.login.ConfigurationSpi

javax.security.auth.login.ConfigurationSpi

```java
public abstract class
ConfigurationSpi

extends
Object
```

This class defines the

Service Provider Interface

(

SPI

)
for the

Configuration

class.
All the abstract methods in this class must be implemented by each
service provider who wishes to supply a Configuration implementation.

Subclass implementations of this abstract class must provide
a public constructor that takes a

Configuration.Parameters

object as an input parameter. This constructor also must throw
an IllegalArgumentException if it does not understand the

Configuration.Parameters

input.

**Since:** 1.6

public abstract class

ConfigurationSpi

extends

Object

This class defines the

Service Provider Interface

(

SPI

)
for the

Configuration

class.
All the abstract methods in this class must be implemented by each
service provider who wishes to supply a Configuration implementation.

Subclass implementations of this abstract class must provide
a public constructor that takes a

Configuration.Parameters

object as an input parameter. This constructor also must throw
an IllegalArgumentException if it does not understand the

Configuration.Parameters

input.

Subclass implementations of this abstract class must provide
a public constructor that takes a

Configuration.Parameters

object as an input parameter. This constructor also must throw
an IllegalArgumentException if it does not understand the

Configuration.Parameters

input.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

ConfigurationSpi

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

protected abstract

AppConfigurationEntry

[]

engineGetAppConfigurationEntry

​(

String

name)

Retrieve the AppConfigurationEntries for the specified

name

.

protected void

engineRefresh

()

Refresh and reload the Configuration.

- Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

Constructor Summary

Constructors

Constructor

Description

ConfigurationSpi

()

---

#### Constructor Summary

Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

protected abstract

AppConfigurationEntry

[]

engineGetAppConfigurationEntry

​(

String

name)

Retrieve the AppConfigurationEntries for the specified

name

.

protected void

engineRefresh

()

Refresh and reload the Configuration.

- Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

---

#### Method Summary

Retrieve the AppConfigurationEntries for the specified

name

.

Refresh and reload the Configuration.

Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- ConfigurationSpi

```java
public ConfigurationSpi()
```

============ METHOD DETAIL ==========

- Method Detail

- engineGetAppConfigurationEntry

```java
protected abstract
AppConfigurationEntry
[] engineGetAppConfigurationEntry​(
String
name)
```

Retrieve the AppConfigurationEntries for the specified

name

.

**Parameters:** name

- the name used to index the Configuration.
**Returns:** an array of AppConfigurationEntries for the specified

name

, or null if there are no entries.

- engineRefresh

```java
protected void engineRefresh()
```

Refresh and reload the Configuration.

This method causes this Configuration object to refresh/reload its
contents in an implementation-dependent manner.
For example, if this Configuration object stores its entries in a file,
calling

refresh

may cause the file to be re-read.

The default implementation of this method does nothing.
This method should be overridden if a refresh operation is supported
by the implementation.

**Throws:** SecurityException

- if the caller does not have permission
to refresh its Configuration.

Constructor Detail

- ConfigurationSpi

```java
public ConfigurationSpi()
```

---

#### Constructor Detail

ConfigurationSpi

```java
public ConfigurationSpi()
```

---

#### ConfigurationSpi

public ConfigurationSpi()

Method Detail

- engineGetAppConfigurationEntry

```java
protected abstract
AppConfigurationEntry
[] engineGetAppConfigurationEntry​(
String
name)
```

Retrieve the AppConfigurationEntries for the specified

name

.

**Parameters:** name

- the name used to index the Configuration.
**Returns:** an array of AppConfigurationEntries for the specified

name

, or null if there are no entries.

- engineRefresh

```java
protected void engineRefresh()
```

Refresh and reload the Configuration.

This method causes this Configuration object to refresh/reload its
contents in an implementation-dependent manner.
For example, if this Configuration object stores its entries in a file,
calling

refresh

may cause the file to be re-read.

The default implementation of this method does nothing.
This method should be overridden if a refresh operation is supported
by the implementation.

**Throws:** SecurityException

- if the caller does not have permission
to refresh its Configuration.

---

#### Method Detail

engineGetAppConfigurationEntry

```java
protected abstract
AppConfigurationEntry
[] engineGetAppConfigurationEntry​(
String
name)
```

Retrieve the AppConfigurationEntries for the specified

name

.

**Parameters:** name

- the name used to index the Configuration.
**Returns:** an array of AppConfigurationEntries for the specified

name

, or null if there are no entries.

---

#### engineGetAppConfigurationEntry

protected abstract

AppConfigurationEntry

[] engineGetAppConfigurationEntry​(

String

name)

Retrieve the AppConfigurationEntries for the specified

name

.

engineRefresh

```java
protected void engineRefresh()
```

Refresh and reload the Configuration.

This method causes this Configuration object to refresh/reload its
contents in an implementation-dependent manner.
For example, if this Configuration object stores its entries in a file,
calling

refresh

may cause the file to be re-read.

The default implementation of this method does nothing.
This method should be overridden if a refresh operation is supported
by the implementation.

**Throws:** SecurityException

- if the caller does not have permission
to refresh its Configuration.

---

#### engineRefresh

protected void engineRefresh()

Refresh and reload the Configuration.

This method causes this Configuration object to refresh/reload its
contents in an implementation-dependent manner.
For example, if this Configuration object stores its entries in a file,
calling

refresh

may cause the file to be re-read.

The default implementation of this method does nothing.
This method should be overridden if a refresh operation is supported
by the implementation.

This method causes this Configuration object to refresh/reload its
contents in an implementation-dependent manner.
For example, if this Configuration object stores its entries in a file,
calling

refresh

may cause the file to be re-read.

The default implementation of this method does nothing.
This method should be overridden if a refresh operation is supported
by the implementation.

The default implementation of this method does nothing.
This method should be overridden if a refresh operation is supported
by the implementation.

---

