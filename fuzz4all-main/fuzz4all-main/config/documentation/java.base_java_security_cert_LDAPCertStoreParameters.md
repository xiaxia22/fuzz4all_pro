# Class LDAPCertStoreParameters

**Source:** `java.base\java\security\cert\LDAPCertStoreParameters.html`

### Class Description

```java
public class
LDAPCertStoreParameters

extends
Object

implements
CertStoreParameters
```

Parameters used as input for the LDAP

CertStore

algorithm.

This class is used to provide necessary configuration parameters (server
name and port number) to implementations of the LDAP

CertStore

algorithm. However, if you are retrieving certificates or CRLs from
an ldap URI as specified by RFC 5280, use the

URICertStoreParameters

instead as the URI may contain additional information such as the
distinguished name that will help the LDAP CertStore find the specific
certificates and CRLs.

Concurrent Access

Unless otherwise specified, the methods defined in this class are not
thread-safe. Multiple threads that need to access a single
object concurrently should synchronize amongst themselves and
provide the necessary locking. Multiple threads each manipulating
separate objects need not synchronize.

**All Implemented Interfaces:** Cloneable

,

CertStoreParameters

---

### Field Details

*No entries found.*

### Constructor Details

#### public LDAPCertStoreParameters​(
String
serverName,
int port)

Creates an instance of

LDAPCertStoreParameters

with the
specified parameter values.

**Parameters:**
- serverName

- the DNS name of the LDAP server
- port

- the port number of the LDAP server

**Throws:**
- NullPointerException

- if

serverName

is

null

---

#### public LDAPCertStoreParameters​(
String
serverName)

Creates an instance of

LDAPCertStoreParameters

with the
specified server name and a default port of 389.

**Parameters:**
- serverName

- the DNS name of the LDAP server

**Throws:**
- NullPointerException

- if

serverName

is

null

---

#### public LDAPCertStoreParameters()

Creates an instance of

LDAPCertStoreParameters

with the
default parameter values (server name "localhost", port 389).

---

### Method Details

#### public
String
getServerName()

Returns the DNS name of the LDAP server.

**Returns:**
- the name (not

null

)

---

#### public int getPort()

Returns the port number of the LDAP server.

**Returns:**
- the port number

---

#### public
Object
clone()

Returns a copy of this object. Changes to the copy will not affect
the original and vice versa.

Note: this method currently performs a shallow copy of the object
(simply calls

Object.clone()

). This may be changed in a
future revision to perform a deep copy if new parameters are added
that should not be shared.

**Specified by:**
- clone

in interface

CertStoreParameters

**Overrides:**
- clone

in class

Object

**Returns:**
- the copy

**See Also:**
- Cloneable

---

#### public
String
toString()

Returns a formatted string describing the parameters.

**Overrides:**
- toString

in class

Object

**Returns:**
- a formatted string describing the parameters

---

### Additional Sections

#### Class LDAPCertStoreParameters

java.lang.Object

- java.security.cert.LDAPCertStoreParameters

java.security.cert.LDAPCertStoreParameters

**All Implemented Interfaces:** Cloneable

,

CertStoreParameters

```java
public class
LDAPCertStoreParameters

extends
Object

implements
CertStoreParameters
```

Parameters used as input for the LDAP

CertStore

algorithm.

This class is used to provide necessary configuration parameters (server
name and port number) to implementations of the LDAP

CertStore

algorithm. However, if you are retrieving certificates or CRLs from
an ldap URI as specified by RFC 5280, use the

URICertStoreParameters

instead as the URI may contain additional information such as the
distinguished name that will help the LDAP CertStore find the specific
certificates and CRLs.

Concurrent Access

Unless otherwise specified, the methods defined in this class are not
thread-safe. Multiple threads that need to access a single
object concurrently should synchronize amongst themselves and
provide the necessary locking. Multiple threads each manipulating
separate objects need not synchronize.

**Since:** 1.4
**See Also:** CertStore

public class

LDAPCertStoreParameters

extends

Object

implements

CertStoreParameters

Parameters used as input for the LDAP

CertStore

algorithm.

This class is used to provide necessary configuration parameters (server
name and port number) to implementations of the LDAP

CertStore

algorithm. However, if you are retrieving certificates or CRLs from
an ldap URI as specified by RFC 5280, use the

URICertStoreParameters

instead as the URI may contain additional information such as the
distinguished name that will help the LDAP CertStore find the specific
certificates and CRLs.

Concurrent Access

Unless otherwise specified, the methods defined in this class are not
thread-safe. Multiple threads that need to access a single
object concurrently should synchronize amongst themselves and
provide the necessary locking. Multiple threads each manipulating
separate objects need not synchronize.

This class is used to provide necessary configuration parameters (server
name and port number) to implementations of the LDAP

CertStore

algorithm. However, if you are retrieving certificates or CRLs from
an ldap URI as specified by RFC 5280, use the

URICertStoreParameters

instead as the URI may contain additional information such as the
distinguished name that will help the LDAP CertStore find the specific
certificates and CRLs.

Concurrent Access

Unless otherwise specified, the methods defined in this class are not
thread-safe. Multiple threads that need to access a single
object concurrently should synchronize amongst themselves and
provide the necessary locking. Multiple threads each manipulating
separate objects need not synchronize.

Concurrent Access

Unless otherwise specified, the methods defined in this class are not
thread-safe. Multiple threads that need to access a single
object concurrently should synchronize amongst themselves and
provide the necessary locking. Multiple threads each manipulating
separate objects need not synchronize.

Unless otherwise specified, the methods defined in this class are not
thread-safe. Multiple threads that need to access a single
object concurrently should synchronize amongst themselves and
provide the necessary locking. Multiple threads each manipulating
separate objects need not synchronize.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

LDAPCertStoreParameters

()

Creates an instance of

LDAPCertStoreParameters

with the
default parameter values (server name "localhost", port 389).

LDAPCertStoreParameters

​(

String

serverName)

Creates an instance of

LDAPCertStoreParameters

with the
specified server name and a default port of 389.

LDAPCertStoreParameters

​(

String

serverName,
int port)

Creates an instance of

LDAPCertStoreParameters

with the
specified parameter values.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Object

clone

()

Returns a copy of this object.

int

getPort

()

Returns the port number of the LDAP server.

String

getServerName

()

Returns the DNS name of the LDAP server.

String

toString

()

Returns a formatted string describing the parameters.

- Methods declared in class java.lang.

Object

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

wait

,

wait

,

wait

Constructor Summary

Constructors

Constructor

Description

LDAPCertStoreParameters

()

Creates an instance of

LDAPCertStoreParameters

with the
default parameter values (server name "localhost", port 389).

LDAPCertStoreParameters

​(

String

serverName)

Creates an instance of

LDAPCertStoreParameters

with the
specified server name and a default port of 389.

LDAPCertStoreParameters

​(

String

serverName,
int port)

Creates an instance of

LDAPCertStoreParameters

with the
specified parameter values.

---

#### Constructor Summary

Creates an instance of

LDAPCertStoreParameters

with the
default parameter values (server name "localhost", port 389).

Creates an instance of

LDAPCertStoreParameters

with the
specified server name and a default port of 389.

Creates an instance of

LDAPCertStoreParameters

with the
specified parameter values.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Object

clone

()

Returns a copy of this object.

int

getPort

()

Returns the port number of the LDAP server.

String

getServerName

()

Returns the DNS name of the LDAP server.

String

toString

()

Returns a formatted string describing the parameters.

- Methods declared in class java.lang.

Object

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

wait

,

wait

,

wait

---

#### Method Summary

Returns a copy of this object.

Returns the port number of the LDAP server.

Returns the DNS name of the LDAP server.

Returns a formatted string describing the parameters.

Methods declared in class java.lang.

Object

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

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- LDAPCertStoreParameters

```java
public LDAPCertStoreParameters​(
String
serverName,
int port)
```

Creates an instance of

LDAPCertStoreParameters

with the
specified parameter values.

**Parameters:** serverName

- the DNS name of the LDAP server
**Parameters:** port

- the port number of the LDAP server
**Throws:** NullPointerException

- if

serverName

is

null

- LDAPCertStoreParameters

```java
public LDAPCertStoreParameters​(
String
serverName)
```

Creates an instance of

LDAPCertStoreParameters

with the
specified server name and a default port of 389.

**Parameters:** serverName

- the DNS name of the LDAP server
**Throws:** NullPointerException

- if

serverName

is

null

- LDAPCertStoreParameters

```java
public LDAPCertStoreParameters()
```

Creates an instance of

LDAPCertStoreParameters

with the
default parameter values (server name "localhost", port 389).

============ METHOD DETAIL ==========

- Method Detail

- getServerName

```java
public
String
getServerName()
```

Returns the DNS name of the LDAP server.

**Returns:** the name (not

null

)

- getPort

```java
public int getPort()
```

Returns the port number of the LDAP server.

**Returns:** the port number

- clone

```java
public
Object
clone()
```

Returns a copy of this object. Changes to the copy will not affect
the original and vice versa.

Note: this method currently performs a shallow copy of the object
(simply calls

Object.clone()

). This may be changed in a
future revision to perform a deep copy if new parameters are added
that should not be shared.

**Specified by:** clone

in interface

CertStoreParameters
**Overrides:** clone

in class

Object
**Returns:** the copy
**See Also:** Cloneable

- toString

```java
public
String
toString()
```

Returns a formatted string describing the parameters.

**Overrides:** toString

in class

Object
**Returns:** a formatted string describing the parameters

Constructor Detail

- LDAPCertStoreParameters

```java
public LDAPCertStoreParameters​(
String
serverName,
int port)
```

Creates an instance of

LDAPCertStoreParameters

with the
specified parameter values.

**Parameters:** serverName

- the DNS name of the LDAP server
**Parameters:** port

- the port number of the LDAP server
**Throws:** NullPointerException

- if

serverName

is

null

- LDAPCertStoreParameters

```java
public LDAPCertStoreParameters​(
String
serverName)
```

Creates an instance of

LDAPCertStoreParameters

with the
specified server name and a default port of 389.

**Parameters:** serverName

- the DNS name of the LDAP server
**Throws:** NullPointerException

- if

serverName

is

null

- LDAPCertStoreParameters

```java
public LDAPCertStoreParameters()
```

Creates an instance of

LDAPCertStoreParameters

with the
default parameter values (server name "localhost", port 389).

---

#### Constructor Detail

LDAPCertStoreParameters

```java
public LDAPCertStoreParameters​(
String
serverName,
int port)
```

Creates an instance of

LDAPCertStoreParameters

with the
specified parameter values.

**Parameters:** serverName

- the DNS name of the LDAP server
**Parameters:** port

- the port number of the LDAP server
**Throws:** NullPointerException

- if

serverName

is

null

---

#### LDAPCertStoreParameters

public LDAPCertStoreParameters​(

String

serverName,
int port)

Creates an instance of

LDAPCertStoreParameters

with the
specified parameter values.

LDAPCertStoreParameters

```java
public LDAPCertStoreParameters​(
String
serverName)
```

Creates an instance of

LDAPCertStoreParameters

with the
specified server name and a default port of 389.

**Parameters:** serverName

- the DNS name of the LDAP server
**Throws:** NullPointerException

- if

serverName

is

null

---

#### LDAPCertStoreParameters

public LDAPCertStoreParameters​(

String

serverName)

Creates an instance of

LDAPCertStoreParameters

with the
specified server name and a default port of 389.

LDAPCertStoreParameters

```java
public LDAPCertStoreParameters()
```

Creates an instance of

LDAPCertStoreParameters

with the
default parameter values (server name "localhost", port 389).

---

#### LDAPCertStoreParameters

public LDAPCertStoreParameters()

Creates an instance of

LDAPCertStoreParameters

with the
default parameter values (server name "localhost", port 389).

Method Detail

- getServerName

```java
public
String
getServerName()
```

Returns the DNS name of the LDAP server.

**Returns:** the name (not

null

)

- getPort

```java
public int getPort()
```

Returns the port number of the LDAP server.

**Returns:** the port number

- clone

```java
public
Object
clone()
```

Returns a copy of this object. Changes to the copy will not affect
the original and vice versa.

Note: this method currently performs a shallow copy of the object
(simply calls

Object.clone()

). This may be changed in a
future revision to perform a deep copy if new parameters are added
that should not be shared.

**Specified by:** clone

in interface

CertStoreParameters
**Overrides:** clone

in class

Object
**Returns:** the copy
**See Also:** Cloneable

- toString

```java
public
String
toString()
```

Returns a formatted string describing the parameters.

**Overrides:** toString

in class

Object
**Returns:** a formatted string describing the parameters

---

#### Method Detail

getServerName

```java
public
String
getServerName()
```

Returns the DNS name of the LDAP server.

**Returns:** the name (not

null

)

---

#### getServerName

public

String

getServerName()

Returns the DNS name of the LDAP server.

getPort

```java
public int getPort()
```

Returns the port number of the LDAP server.

**Returns:** the port number

---

#### getPort

public int getPort()

Returns the port number of the LDAP server.

clone

```java
public
Object
clone()
```

Returns a copy of this object. Changes to the copy will not affect
the original and vice versa.

Note: this method currently performs a shallow copy of the object
(simply calls

Object.clone()

). This may be changed in a
future revision to perform a deep copy if new parameters are added
that should not be shared.

**Specified by:** clone

in interface

CertStoreParameters
**Overrides:** clone

in class

Object
**Returns:** the copy
**See Also:** Cloneable

---

#### clone

public

Object

clone()

Returns a copy of this object. Changes to the copy will not affect
the original and vice versa.

Note: this method currently performs a shallow copy of the object
(simply calls

Object.clone()

). This may be changed in a
future revision to perform a deep copy if new parameters are added
that should not be shared.

Note: this method currently performs a shallow copy of the object
(simply calls

Object.clone()

). This may be changed in a
future revision to perform a deep copy if new parameters are added
that should not be shared.

toString

```java
public
String
toString()
```

Returns a formatted string describing the parameters.

**Overrides:** toString

in class

Object
**Returns:** a formatted string describing the parameters

---

#### toString

public

String

toString()

Returns a formatted string describing the parameters.

---

