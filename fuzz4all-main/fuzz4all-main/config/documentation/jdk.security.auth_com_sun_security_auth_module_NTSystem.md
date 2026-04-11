# Class NTSystem

**Source:** `jdk.security.auth\com\sun\security\auth\module\NTSystem.html`

### Class Description

```java
public class
NTSystem

extends
Object
```

This class implementation retrieves and makes available NT
security information for the current user.

---

### Field Details

*No entries found.*

### Constructor Details

#### public NTSystem()

Instantiate an

NTSystem

and load
the native library to access the underlying system information.

---

### Method Details

#### public
String
getName()

Get the username for the current NT user.

**Returns:**
- the username for the current NT user.

---

#### public
String
getDomain()

Get the domain for the current NT user.

**Returns:**
- the domain for the current NT user.

---

#### public
String
getDomainSID()

Get a printable SID for the current NT user's domain.

**Returns:**
- a printable SID for the current NT user's domain.

---

#### public
String
getUserSID()

Get a printable SID for the current NT user.

**Returns:**
- a printable SID for the current NT user.

---

#### public
String
getPrimaryGroupID()

Get a printable primary group SID for the current NT user.

**Returns:**
- the primary group SID for the current NT user.

---

#### public
String
[] getGroupIDs()

Get the printable group SIDs for the current NT user.

**Returns:**
- the group SIDs for the current NT user.

---

#### public long getImpersonationToken()

Get an impersonation token for the current NT user.

**Returns:**
- an impersonation token for the current NT user.

---

### Additional Sections

#### Class NTSystem

java.lang.Object

- com.sun.security.auth.module.NTSystem

com.sun.security.auth.module.NTSystem

```java
public class
NTSystem

extends
Object
```

This class implementation retrieves and makes available NT
security information for the current user.

public class

NTSystem

extends

Object

This class implementation retrieves and makes available NT
security information for the current user.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

NTSystem

()

Instantiate an

NTSystem

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

String

getDomain

()

Get the domain for the current NT user.

String

getDomainSID

()

Get a printable SID for the current NT user's domain.

String

[]

getGroupIDs

()

Get the printable group SIDs for the current NT user.

long

getImpersonationToken

()

Get an impersonation token for the current NT user.

String

getName

()

Get the username for the current NT user.

String

getPrimaryGroupID

()

Get a printable primary group SID for the current NT user.

String

getUserSID

()

Get a printable SID for the current NT user.

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

NTSystem

()

Instantiate an

NTSystem

and load
the native library to access the underlying system information.

---

#### Constructor Summary

Instantiate an

NTSystem

and load
the native library to access the underlying system information.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

String

getDomain

()

Get the domain for the current NT user.

String

getDomainSID

()

Get a printable SID for the current NT user's domain.

String

[]

getGroupIDs

()

Get the printable group SIDs for the current NT user.

long

getImpersonationToken

()

Get an impersonation token for the current NT user.

String

getName

()

Get the username for the current NT user.

String

getPrimaryGroupID

()

Get a printable primary group SID for the current NT user.

String

getUserSID

()

Get a printable SID for the current NT user.

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

Get the domain for the current NT user.

Get a printable SID for the current NT user's domain.

Get the printable group SIDs for the current NT user.

Get an impersonation token for the current NT user.

Get the username for the current NT user.

Get a printable primary group SID for the current NT user.

Get a printable SID for the current NT user.

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

- NTSystem

```java
public NTSystem()
```

Instantiate an

NTSystem

and load
the native library to access the underlying system information.

============ METHOD DETAIL ==========

- Method Detail

- getName

```java
public
String
getName()
```

Get the username for the current NT user.

**Returns:** the username for the current NT user.

- getDomain

```java
public
String
getDomain()
```

Get the domain for the current NT user.

**Returns:** the domain for the current NT user.

- getDomainSID

```java
public
String
getDomainSID()
```

Get a printable SID for the current NT user's domain.

**Returns:** a printable SID for the current NT user's domain.

- getUserSID

```java
public
String
getUserSID()
```

Get a printable SID for the current NT user.

**Returns:** a printable SID for the current NT user.

- getPrimaryGroupID

```java
public
String
getPrimaryGroupID()
```

Get a printable primary group SID for the current NT user.

**Returns:** the primary group SID for the current NT user.

- getGroupIDs

```java
public
String
[] getGroupIDs()
```

Get the printable group SIDs for the current NT user.

**Returns:** the group SIDs for the current NT user.

- getImpersonationToken

```java
public long getImpersonationToken()
```

Get an impersonation token for the current NT user.

**Returns:** an impersonation token for the current NT user.

Constructor Detail

- NTSystem

```java
public NTSystem()
```

Instantiate an

NTSystem

and load
the native library to access the underlying system information.

---

#### Constructor Detail

NTSystem

```java
public NTSystem()
```

Instantiate an

NTSystem

and load
the native library to access the underlying system information.

---

#### NTSystem

public NTSystem()

Instantiate an

NTSystem

and load
the native library to access the underlying system information.

Method Detail

- getName

```java
public
String
getName()
```

Get the username for the current NT user.

**Returns:** the username for the current NT user.

- getDomain

```java
public
String
getDomain()
```

Get the domain for the current NT user.

**Returns:** the domain for the current NT user.

- getDomainSID

```java
public
String
getDomainSID()
```

Get a printable SID for the current NT user's domain.

**Returns:** a printable SID for the current NT user's domain.

- getUserSID

```java
public
String
getUserSID()
```

Get a printable SID for the current NT user.

**Returns:** a printable SID for the current NT user.

- getPrimaryGroupID

```java
public
String
getPrimaryGroupID()
```

Get a printable primary group SID for the current NT user.

**Returns:** the primary group SID for the current NT user.

- getGroupIDs

```java
public
String
[] getGroupIDs()
```

Get the printable group SIDs for the current NT user.

**Returns:** the group SIDs for the current NT user.

- getImpersonationToken

```java
public long getImpersonationToken()
```

Get an impersonation token for the current NT user.

**Returns:** an impersonation token for the current NT user.

---

#### Method Detail

getName

```java
public
String
getName()
```

Get the username for the current NT user.

**Returns:** the username for the current NT user.

---

#### getName

public

String

getName()

Get the username for the current NT user.

getDomain

```java
public
String
getDomain()
```

Get the domain for the current NT user.

**Returns:** the domain for the current NT user.

---

#### getDomain

public

String

getDomain()

Get the domain for the current NT user.

getDomainSID

```java
public
String
getDomainSID()
```

Get a printable SID for the current NT user's domain.

**Returns:** a printable SID for the current NT user's domain.

---

#### getDomainSID

public

String

getDomainSID()

Get a printable SID for the current NT user's domain.

getUserSID

```java
public
String
getUserSID()
```

Get a printable SID for the current NT user.

**Returns:** a printable SID for the current NT user.

---

#### getUserSID

public

String

getUserSID()

Get a printable SID for the current NT user.

getPrimaryGroupID

```java
public
String
getPrimaryGroupID()
```

Get a printable primary group SID for the current NT user.

**Returns:** the primary group SID for the current NT user.

---

#### getPrimaryGroupID

public

String

getPrimaryGroupID()

Get a printable primary group SID for the current NT user.

getGroupIDs

```java
public
String
[] getGroupIDs()
```

Get the printable group SIDs for the current NT user.

**Returns:** the group SIDs for the current NT user.

---

#### getGroupIDs

public

String

[] getGroupIDs()

Get the printable group SIDs for the current NT user.

getImpersonationToken

```java
public long getImpersonationToken()
```

Get an impersonation token for the current NT user.

**Returns:** an impersonation token for the current NT user.

---

#### getImpersonationToken

public long getImpersonationToken()

Get an impersonation token for the current NT user.

---

