# Class UnixSystem

**Source:** `jdk.security.auth\com\sun\security\auth\module\UnixSystem.html`

### Class Description

```java
public class
UnixSystem

extends
Object
```

This class implementation retrieves and makes available Unix
UID/GID/groups information for the current user.

---

### Field Details

#### protected
String
username

*No description found.*

---

#### protected long uid

*No description found.*

---

#### protected long gid

*No description found.*

---

#### protected long[] groups

*No description found.*

---

### Constructor Details

#### public UnixSystem()

Instantiate a

UnixSystem

and load
the native library to access the underlying system information.

---

### Method Details

#### public
String
getUsername()

Get the username for the current Unix user.

**Returns:**
- the username for the current Unix user.

---

#### public long getUid()

Get the UID for the current Unix user.

**Returns:**
- the UID for the current Unix user.

---

#### public long getGid()

Get the GID for the current Unix user.

**Returns:**
- the GID for the current Unix user.

---

#### public long[] getGroups()

Get the supplementary groups for the current Unix user.

**Returns:**
- the supplementary groups for the current Unix user.

---

### Additional Sections

#### Class UnixSystem

java.lang.Object

- com.sun.security.auth.module.UnixSystem

com.sun.security.auth.module.UnixSystem

```java
public class
UnixSystem

extends
Object
```

This class implementation retrieves and makes available Unix
UID/GID/groups information for the current user.

public class

UnixSystem

extends

Object

This class implementation retrieves and makes available Unix
UID/GID/groups information for the current user.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected long

gid

protected long[]

groups

protected long

uid

protected

String

username

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

UnixSystem

()

Instantiate a

UnixSystem

and load
the native library to access the underlying system information.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

long

getGid

()

Get the GID for the current Unix user.

long[]

getGroups

()

Get the supplementary groups for the current Unix user.

long

getUid

()

Get the UID for the current Unix user.

String

getUsername

()

Get the username for the current Unix user.

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

Field Summary

Fields

Modifier and Type

Field

Description

protected long

gid

protected long[]

groups

protected long

uid

protected

String

username

---

#### Field Summary

Constructor Summary

Constructors

Constructor

Description

UnixSystem

()

Instantiate a

UnixSystem

and load
the native library to access the underlying system information.

---

#### Constructor Summary

Instantiate a

UnixSystem

and load
the native library to access the underlying system information.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

long

getGid

()

Get the GID for the current Unix user.

long[]

getGroups

()

Get the supplementary groups for the current Unix user.

long

getUid

()

Get the UID for the current Unix user.

String

getUsername

()

Get the username for the current Unix user.

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

Get the GID for the current Unix user.

Get the supplementary groups for the current Unix user.

Get the UID for the current Unix user.

Get the username for the current Unix user.

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

============ FIELD DETAIL ===========

- Field Detail

- username

```java
protected
String
username
```

- uid

```java
protected long uid
```

- gid

```java
protected long gid
```

- groups

```java
protected long[] groups
```

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- UnixSystem

```java
public UnixSystem()
```

Instantiate a

UnixSystem

and load
the native library to access the underlying system information.

============ METHOD DETAIL ==========

- Method Detail

- getUsername

```java
public
String
getUsername()
```

Get the username for the current Unix user.

**Returns:** the username for the current Unix user.

- getUid

```java
public long getUid()
```

Get the UID for the current Unix user.

**Returns:** the UID for the current Unix user.

- getGid

```java
public long getGid()
```

Get the GID for the current Unix user.

**Returns:** the GID for the current Unix user.

- getGroups

```java
public long[] getGroups()
```

Get the supplementary groups for the current Unix user.

**Returns:** the supplementary groups for the current Unix user.

Field Detail

- username

```java
protected
String
username
```

- uid

```java
protected long uid
```

- gid

```java
protected long gid
```

- groups

```java
protected long[] groups
```

---

#### Field Detail

username

```java
protected
String
username
```

---

#### username

protected

String

username

uid

```java
protected long uid
```

---

#### uid

protected long uid

gid

```java
protected long gid
```

---

#### gid

protected long gid

groups

```java
protected long[] groups
```

---

#### groups

protected long[] groups

Constructor Detail

- UnixSystem

```java
public UnixSystem()
```

Instantiate a

UnixSystem

and load
the native library to access the underlying system information.

---

#### Constructor Detail

UnixSystem

```java
public UnixSystem()
```

Instantiate a

UnixSystem

and load
the native library to access the underlying system information.

---

#### UnixSystem

public UnixSystem()

Instantiate a

UnixSystem

and load
the native library to access the underlying system information.

Method Detail

- getUsername

```java
public
String
getUsername()
```

Get the username for the current Unix user.

**Returns:** the username for the current Unix user.

- getUid

```java
public long getUid()
```

Get the UID for the current Unix user.

**Returns:** the UID for the current Unix user.

- getGid

```java
public long getGid()
```

Get the GID for the current Unix user.

**Returns:** the GID for the current Unix user.

- getGroups

```java
public long[] getGroups()
```

Get the supplementary groups for the current Unix user.

**Returns:** the supplementary groups for the current Unix user.

---

#### Method Detail

getUsername

```java
public
String
getUsername()
```

Get the username for the current Unix user.

**Returns:** the username for the current Unix user.

---

#### getUsername

public

String

getUsername()

Get the username for the current Unix user.

getUid

```java
public long getUid()
```

Get the UID for the current Unix user.

**Returns:** the UID for the current Unix user.

---

#### getUid

public long getUid()

Get the UID for the current Unix user.

getGid

```java
public long getGid()
```

Get the GID for the current Unix user.

**Returns:** the GID for the current Unix user.

---

#### getGid

public long getGid()

Get the GID for the current Unix user.

getGroups

```java
public long[] getGroups()
```

Get the supplementary groups for the current Unix user.

**Returns:** the supplementary groups for the current Unix user.

---

#### getGroups

public long[] getGroups()

Get the supplementary groups for the current Unix user.

---

