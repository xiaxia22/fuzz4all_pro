# Class HttpPrincipal

**Source:** `jdk.httpserver\com\sun\net\httpserver\HttpPrincipal.html`

### Class Description

```java
public class
HttpPrincipal

extends
Object

implements
Principal
```

Represents a user authenticated by HTTP Basic or Digest
authentication.

**All Implemented Interfaces:** Principal

---

### Field Details

*No entries found.*

### Constructor Details

#### public HttpPrincipal​(
String
username,

String
realm)

creates a HttpPrincipal from the given username and realm

**Parameters:**
- username

- The name of the user within the realm
- realm

- The realm.

**Throws:**
- NullPointerException

- if either username or realm are null

---

### Method Details

#### public boolean equals​(
Object
another)

Compares two HttpPrincipal. Returns

true

if

another

is an instance of HttpPrincipal, and its
username and realm are equal to this object's username
and realm. Returns

false

otherwise.

**Specified by:**
- equals

in interface

Principal

**Overrides:**
- equals

in class

Object

**Parameters:**
- another

- the reference object with which to compare.

**Returns:**
- true

if this object is the same as the obj
argument;

false

otherwise.

**See Also:**
- Object.hashCode()

,

HashMap

---

#### public
String
getName()

returns the contents of this principal in the form

realm:username

**Specified by:**
- getName

in interface

Principal

**Returns:**
- the name of this principal.

---

#### public
String
getUsername()

returns the username this object was created with.

---

#### public
String
getRealm()

returns the realm this object was created with.

---

#### public int hashCode()

returns a hashcode for this HttpPrincipal. This is calculated
as

(getUsername()+getRealm().hashCode()

**Specified by:**
- hashCode

in interface

Principal

**Overrides:**
- hashCode

in class

Object

**Returns:**
- a hash code value for this object.

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### public
String
toString()

returns the same string as getName()

**Specified by:**
- toString

in interface

Principal

**Overrides:**
- toString

in class

Object

**Returns:**
- a string representation of the object.

---

### Additional Sections

#### Class HttpPrincipal

java.lang.Object

- com.sun.net.httpserver.HttpPrincipal

com.sun.net.httpserver.HttpPrincipal

**All Implemented Interfaces:** Principal

```java
public class
HttpPrincipal

extends
Object

implements
Principal
```

Represents a user authenticated by HTTP Basic or Digest
authentication.

public class

HttpPrincipal

extends

Object

implements

Principal

Represents a user authenticated by HTTP Basic or Digest
authentication.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

HttpPrincipal

​(

String

username,

String

realm)

creates a HttpPrincipal from the given username and realm

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

equals

​(

Object

another)

Compares two HttpPrincipal.

String

getName

()

returns the contents of this principal in the form

realm:username

String

getRealm

()

returns the realm this object was created with.

String

getUsername

()

returns the username this object was created with.

int

hashCode

()

returns a hashcode for this HttpPrincipal.

String

toString

()

returns the same string as getName()

- Methods declared in class java.lang.

Object

clone

,

finalize

,

getClass

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

- Methods declared in interface java.security.

Principal

implies

Constructor Summary

Constructors

Constructor

Description

HttpPrincipal

​(

String

username,

String

realm)

creates a HttpPrincipal from the given username and realm

---

#### Constructor Summary

creates a HttpPrincipal from the given username and realm

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

equals

​(

Object

another)

Compares two HttpPrincipal.

String

getName

()

returns the contents of this principal in the form

realm:username

String

getRealm

()

returns the realm this object was created with.

String

getUsername

()

returns the username this object was created with.

int

hashCode

()

returns a hashcode for this HttpPrincipal.

String

toString

()

returns the same string as getName()

- Methods declared in class java.lang.

Object

clone

,

finalize

,

getClass

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

- Methods declared in interface java.security.

Principal

implies

---

#### Method Summary

Compares two HttpPrincipal.

returns the contents of this principal in the form

realm:username

returns the realm this object was created with.

returns the username this object was created with.

returns a hashcode for this HttpPrincipal.

returns the same string as getName()

Methods declared in class java.lang.

Object

clone

,

finalize

,

getClass

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

Methods declared in interface java.security.

Principal

implies

---

#### Methods declared in interface java.security. Principal

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- HttpPrincipal

```java
public HttpPrincipal​(
String
username,

String
realm)
```

creates a HttpPrincipal from the given username and realm

**Parameters:** username

- The name of the user within the realm
**Parameters:** realm

- The realm.
**Throws:** NullPointerException

- if either username or realm are null

============ METHOD DETAIL ==========

- Method Detail

- equals

```java
public boolean equals​(
Object
another)
```

Compares two HttpPrincipal. Returns

true

if

another

is an instance of HttpPrincipal, and its
username and realm are equal to this object's username
and realm. Returns

false

otherwise.

**Specified by:** equals

in interface

Principal
**Overrides:** equals

in class

Object
**Parameters:** another

- the reference object with which to compare.
**Returns:** true

if this object is the same as the obj
argument;

false

otherwise.
**See Also:** Object.hashCode()

,

HashMap

- getName

```java
public
String
getName()
```

returns the contents of this principal in the form

realm:username

**Specified by:** getName

in interface

Principal
**Returns:** the name of this principal.

- getUsername

```java
public
String
getUsername()
```

returns the username this object was created with.

- getRealm

```java
public
String
getRealm()
```

returns the realm this object was created with.

- hashCode

```java
public int hashCode()
```

returns a hashcode for this HttpPrincipal. This is calculated
as

(getUsername()+getRealm().hashCode()

**Specified by:** hashCode

in interface

Principal
**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this object.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- toString

```java
public
String
toString()
```

returns the same string as getName()

**Specified by:** toString

in interface

Principal
**Overrides:** toString

in class

Object
**Returns:** a string representation of the object.

Constructor Detail

- HttpPrincipal

```java
public HttpPrincipal​(
String
username,

String
realm)
```

creates a HttpPrincipal from the given username and realm

**Parameters:** username

- The name of the user within the realm
**Parameters:** realm

- The realm.
**Throws:** NullPointerException

- if either username or realm are null

---

#### Constructor Detail

HttpPrincipal

```java
public HttpPrincipal​(
String
username,

String
realm)
```

creates a HttpPrincipal from the given username and realm

**Parameters:** username

- The name of the user within the realm
**Parameters:** realm

- The realm.
**Throws:** NullPointerException

- if either username or realm are null

---

#### HttpPrincipal

public HttpPrincipal​(

String

username,

String

realm)

creates a HttpPrincipal from the given username and realm

Method Detail

- equals

```java
public boolean equals​(
Object
another)
```

Compares two HttpPrincipal. Returns

true

if

another

is an instance of HttpPrincipal, and its
username and realm are equal to this object's username
and realm. Returns

false

otherwise.

**Specified by:** equals

in interface

Principal
**Overrides:** equals

in class

Object
**Parameters:** another

- the reference object with which to compare.
**Returns:** true

if this object is the same as the obj
argument;

false

otherwise.
**See Also:** Object.hashCode()

,

HashMap

- getName

```java
public
String
getName()
```

returns the contents of this principal in the form

realm:username

**Specified by:** getName

in interface

Principal
**Returns:** the name of this principal.

- getUsername

```java
public
String
getUsername()
```

returns the username this object was created with.

- getRealm

```java
public
String
getRealm()
```

returns the realm this object was created with.

- hashCode

```java
public int hashCode()
```

returns a hashcode for this HttpPrincipal. This is calculated
as

(getUsername()+getRealm().hashCode()

**Specified by:** hashCode

in interface

Principal
**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this object.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- toString

```java
public
String
toString()
```

returns the same string as getName()

**Specified by:** toString

in interface

Principal
**Overrides:** toString

in class

Object
**Returns:** a string representation of the object.

---

#### Method Detail

equals

```java
public boolean equals​(
Object
another)
```

Compares two HttpPrincipal. Returns

true

if

another

is an instance of HttpPrincipal, and its
username and realm are equal to this object's username
and realm. Returns

false

otherwise.

**Specified by:** equals

in interface

Principal
**Overrides:** equals

in class

Object
**Parameters:** another

- the reference object with which to compare.
**Returns:** true

if this object is the same as the obj
argument;

false

otherwise.
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

public boolean equals​(

Object

another)

Compares two HttpPrincipal. Returns

true

if

another

is an instance of HttpPrincipal, and its
username and realm are equal to this object's username
and realm. Returns

false

otherwise.

getName

```java
public
String
getName()
```

returns the contents of this principal in the form

realm:username

**Specified by:** getName

in interface

Principal
**Returns:** the name of this principal.

---

#### getName

public

String

getName()

returns the contents of this principal in the form

realm:username

getUsername

```java
public
String
getUsername()
```

returns the username this object was created with.

---

#### getUsername

public

String

getUsername()

returns the username this object was created with.

getRealm

```java
public
String
getRealm()
```

returns the realm this object was created with.

---

#### getRealm

public

String

getRealm()

returns the realm this object was created with.

hashCode

```java
public int hashCode()
```

returns a hashcode for this HttpPrincipal. This is calculated
as

(getUsername()+getRealm().hashCode()

**Specified by:** hashCode

in interface

Principal
**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this object.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public int hashCode()

returns a hashcode for this HttpPrincipal. This is calculated
as

(getUsername()+getRealm().hashCode()

toString

```java
public
String
toString()
```

returns the same string as getName()

**Specified by:** toString

in interface

Principal
**Overrides:** toString

in class

Object
**Returns:** a string representation of the object.

---

#### toString

public

String

toString()

returns the same string as getName()

---

