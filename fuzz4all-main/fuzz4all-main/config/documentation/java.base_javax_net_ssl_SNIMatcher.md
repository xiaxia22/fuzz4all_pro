# Class SNIMatcher

**Source:** `java.base\javax\net\ssl\SNIMatcher.html`

### Class Description

```java
public abstract class
SNIMatcher

extends
Object
```

Instances of this class represent a matcher that performs match
operations on an

SNIServerName

instance.

Servers can use Server Name Indication (SNI) information to decide if
specific

SSLSocket

or

SSLEngine

instances should accept
a connection. For example, when multiple "virtual" or "name-based"
servers are hosted on a single underlying network address, the server
application can use SNI information to determine whether this server is
the exact server that the client wants to access. Instances of this
class can be used by a server to verify the acceptable server names of
a particular type, such as host names.

SNIMatcher

objects are immutable. Subclasses should not provide
methods that can change the state of an instance once it has been created.

**Since:** 1.8
**See Also:** SNIServerName

,

SNIHostName

,

SSLParameters.getSNIMatchers()

,

SSLParameters.setSNIMatchers(Collection)

---

### Field Details

*No entries found.*

### Constructor Details

#### protected SNIMatcher​(int type)

Creates an

SNIMatcher

using the specified server name type.

**Parameters:**
- type

- the type of the server name that this matcher performs on

**Throws:**
- IllegalArgumentException

- if

type

is not in the range
of 0 to 255, inclusive.

---

### Method Details

#### public final int getType()

Returns the server name type of this

SNIMatcher

object.

**Returns:**
- the server name type of this

SNIMatcher

object.

**See Also:**
- SNIServerName

---

#### public abstract boolean matches​(
SNIServerName
serverName)

Attempts to match the given

SNIServerName

.

**Parameters:**
- serverName

- the

SNIServerName

instance on which this matcher
performs match operations

**Returns:**
- true

if, and only if, the matcher matches the
given

serverName

**Throws:**
- NullPointerException

- if

serverName

is

null
- IllegalArgumentException

- if

serverName

is
not of the given server name type of this matcher

**See Also:**
- SNIServerName

---

### Additional Sections

#### Class SNIMatcher

java.lang.Object

- javax.net.ssl.SNIMatcher

javax.net.ssl.SNIMatcher

```java
public abstract class
SNIMatcher

extends
Object
```

Instances of this class represent a matcher that performs match
operations on an

SNIServerName

instance.

Servers can use Server Name Indication (SNI) information to decide if
specific

SSLSocket

or

SSLEngine

instances should accept
a connection. For example, when multiple "virtual" or "name-based"
servers are hosted on a single underlying network address, the server
application can use SNI information to determine whether this server is
the exact server that the client wants to access. Instances of this
class can be used by a server to verify the acceptable server names of
a particular type, such as host names.

SNIMatcher

objects are immutable. Subclasses should not provide
methods that can change the state of an instance once it has been created.

**Since:** 1.8
**See Also:** SNIServerName

,

SNIHostName

,

SSLParameters.getSNIMatchers()

,

SSLParameters.setSNIMatchers(Collection)

public abstract class

SNIMatcher

extends

Object

Instances of this class represent a matcher that performs match
operations on an

SNIServerName

instance.

Servers can use Server Name Indication (SNI) information to decide if
specific

SSLSocket

or

SSLEngine

instances should accept
a connection. For example, when multiple "virtual" or "name-based"
servers are hosted on a single underlying network address, the server
application can use SNI information to determine whether this server is
the exact server that the client wants to access. Instances of this
class can be used by a server to verify the acceptable server names of
a particular type, such as host names.

SNIMatcher

objects are immutable. Subclasses should not provide
methods that can change the state of an instance once it has been created.

Servers can use Server Name Indication (SNI) information to decide if
specific

SSLSocket

or

SSLEngine

instances should accept
a connection. For example, when multiple "virtual" or "name-based"
servers are hosted on a single underlying network address, the server
application can use SNI information to determine whether this server is
the exact server that the client wants to access. Instances of this
class can be used by a server to verify the acceptable server names of
a particular type, such as host names.

SNIMatcher

objects are immutable. Subclasses should not provide
methods that can change the state of an instance once it has been created.

SNIMatcher

objects are immutable. Subclasses should not provide
methods that can change the state of an instance once it has been created.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

SNIMatcher

​(int type)

Creates an

SNIMatcher

using the specified server name type.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

int

getType

()

Returns the server name type of this

SNIMatcher

object.

abstract boolean

matches

​(

SNIServerName

serverName)

Attempts to match the given

SNIServerName

.

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

Modifier

Constructor

Description

protected

SNIMatcher

​(int type)

Creates an

SNIMatcher

using the specified server name type.

---

#### Constructor Summary

Creates an

SNIMatcher

using the specified server name type.

Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

int

getType

()

Returns the server name type of this

SNIMatcher

object.

abstract boolean

matches

​(

SNIServerName

serverName)

Attempts to match the given

SNIServerName

.

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

Returns the server name type of this

SNIMatcher

object.

Attempts to match the given

SNIServerName

.

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

- SNIMatcher

```java
protected SNIMatcher​(int type)
```

Creates an

SNIMatcher

using the specified server name type.

**Parameters:** type

- the type of the server name that this matcher performs on
**Throws:** IllegalArgumentException

- if

type

is not in the range
of 0 to 255, inclusive.

============ METHOD DETAIL ==========

- Method Detail

- getType

```java
public final int getType()
```

Returns the server name type of this

SNIMatcher

object.

**Returns:** the server name type of this

SNIMatcher

object.
**See Also:** SNIServerName

- matches

```java
public abstract boolean matches​(
SNIServerName
serverName)
```

Attempts to match the given

SNIServerName

.

**Parameters:** serverName

- the

SNIServerName

instance on which this matcher
performs match operations
**Returns:** true

if, and only if, the matcher matches the
given

serverName
**Throws:** NullPointerException

- if

serverName

is

null
**Throws:** IllegalArgumentException

- if

serverName

is
not of the given server name type of this matcher
**See Also:** SNIServerName

Constructor Detail

- SNIMatcher

```java
protected SNIMatcher​(int type)
```

Creates an

SNIMatcher

using the specified server name type.

**Parameters:** type

- the type of the server name that this matcher performs on
**Throws:** IllegalArgumentException

- if

type

is not in the range
of 0 to 255, inclusive.

---

#### Constructor Detail

SNIMatcher

```java
protected SNIMatcher​(int type)
```

Creates an

SNIMatcher

using the specified server name type.

**Parameters:** type

- the type of the server name that this matcher performs on
**Throws:** IllegalArgumentException

- if

type

is not in the range
of 0 to 255, inclusive.

---

#### SNIMatcher

protected SNIMatcher​(int type)

Creates an

SNIMatcher

using the specified server name type.

Method Detail

- getType

```java
public final int getType()
```

Returns the server name type of this

SNIMatcher

object.

**Returns:** the server name type of this

SNIMatcher

object.
**See Also:** SNIServerName

- matches

```java
public abstract boolean matches​(
SNIServerName
serverName)
```

Attempts to match the given

SNIServerName

.

**Parameters:** serverName

- the

SNIServerName

instance on which this matcher
performs match operations
**Returns:** true

if, and only if, the matcher matches the
given

serverName
**Throws:** NullPointerException

- if

serverName

is

null
**Throws:** IllegalArgumentException

- if

serverName

is
not of the given server name type of this matcher
**See Also:** SNIServerName

---

#### Method Detail

getType

```java
public final int getType()
```

Returns the server name type of this

SNIMatcher

object.

**Returns:** the server name type of this

SNIMatcher

object.
**See Also:** SNIServerName

---

#### getType

public final int getType()

Returns the server name type of this

SNIMatcher

object.

matches

```java
public abstract boolean matches​(
SNIServerName
serverName)
```

Attempts to match the given

SNIServerName

.

**Parameters:** serverName

- the

SNIServerName

instance on which this matcher
performs match operations
**Returns:** true

if, and only if, the matcher matches the
given

serverName
**Throws:** NullPointerException

- if

serverName

is

null
**Throws:** IllegalArgumentException

- if

serverName

is
not of the given server name type of this matcher
**See Also:** SNIServerName

---

#### matches

public abstract boolean matches​(

SNIServerName

serverName)

Attempts to match the given

SNIServerName

.

---

