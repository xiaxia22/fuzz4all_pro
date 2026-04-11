# Class NTNumericCredential

**Source:** `jdk.security.auth\com\sun\security\auth\NTNumericCredential.html`

### Class Description

```java
public class
NTNumericCredential

extends
Object
```

This class abstracts an NT security token
and provides a mechanism to do same-process security impersonation.

---

### Field Details

*No entries found.*

### Constructor Details

#### public NTNumericCredential​(long token)

Create an

NTNumericCredential

with an integer value.

**Parameters:**
- token

- the Windows NT security token for this user.

---

### Method Details

#### public long getToken()

Return an integer representation of this

NTNumericCredential

.

**Returns:**
- an integer representation of this

NTNumericCredential

.

---

#### public
String
toString()

Return a string representation of this

NTNumericCredential

.

**Overrides:**
- toString

in class

Object

**Returns:**
- a string representation of this

NTNumericCredential

.

---

#### public boolean equals​(
Object
o)

Compares the specified Object with this

NTNumericCredential

for equality. Returns true if the given object is also a

NTNumericCredential

and the two NTNumericCredentials
represent the same NT security token.

**Overrides:**
- equals

in class

Object

**Parameters:**
- o

- Object to be compared for equality with this

NTNumericCredential

.

**Returns:**
- true if the specified Object is equal to this

NTNumericCredential

.

**See Also:**
- Object.hashCode()

,

HashMap

---

#### public int hashCode()

Return a hash code for this

NTNumericCredential

.

**Overrides:**
- hashCode

in class

Object

**Returns:**
- a hash code for this

NTNumericCredential

.

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

### Additional Sections

#### Class NTNumericCredential

java.lang.Object

- com.sun.security.auth.NTNumericCredential

com.sun.security.auth.NTNumericCredential

```java
public class
NTNumericCredential

extends
Object
```

This class abstracts an NT security token
and provides a mechanism to do same-process security impersonation.

public class

NTNumericCredential

extends

Object

This class abstracts an NT security token
and provides a mechanism to do same-process security impersonation.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

NTNumericCredential

​(long token)

Create an

NTNumericCredential

with an integer value.

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

o)

Compares the specified Object with this

NTNumericCredential

for equality.

long

getToken

()

Return an integer representation of this

NTNumericCredential

.

int

hashCode

()

Return a hash code for this

NTNumericCredential

.

String

toString

()

Return a string representation of this

NTNumericCredential

.

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

Constructor Summary

Constructors

Constructor

Description

NTNumericCredential

​(long token)

Create an

NTNumericCredential

with an integer value.

---

#### Constructor Summary

Create an

NTNumericCredential

with an integer value.

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

o)

Compares the specified Object with this

NTNumericCredential

for equality.

long

getToken

()

Return an integer representation of this

NTNumericCredential

.

int

hashCode

()

Return a hash code for this

NTNumericCredential

.

String

toString

()

Return a string representation of this

NTNumericCredential

.

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

---

#### Method Summary

Compares the specified Object with this

NTNumericCredential

for equality.

Return an integer representation of this

NTNumericCredential

.

Return a hash code for this

NTNumericCredential

.

Return a string representation of this

NTNumericCredential

.

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

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- NTNumericCredential

```java
public NTNumericCredential​(long token)
```

Create an

NTNumericCredential

with an integer value.

**Parameters:** token

- the Windows NT security token for this user.

============ METHOD DETAIL ==========

- Method Detail

- getToken

```java
public long getToken()
```

Return an integer representation of this

NTNumericCredential

.

**Returns:** an integer representation of this

NTNumericCredential

.

- toString

```java
public
String
toString()
```

Return a string representation of this

NTNumericCredential

.

**Overrides:** toString

in class

Object
**Returns:** a string representation of this

NTNumericCredential

.

- equals

```java
public boolean equals​(
Object
o)
```

Compares the specified Object with this

NTNumericCredential

for equality. Returns true if the given object is also a

NTNumericCredential

and the two NTNumericCredentials
represent the same NT security token.

**Overrides:** equals

in class

Object
**Parameters:** o

- Object to be compared for equality with this

NTNumericCredential

.
**Returns:** true if the specified Object is equal to this

NTNumericCredential

.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Return a hash code for this

NTNumericCredential

.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code for this

NTNumericCredential

.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

Constructor Detail

- NTNumericCredential

```java
public NTNumericCredential​(long token)
```

Create an

NTNumericCredential

with an integer value.

**Parameters:** token

- the Windows NT security token for this user.

---

#### Constructor Detail

NTNumericCredential

```java
public NTNumericCredential​(long token)
```

Create an

NTNumericCredential

with an integer value.

**Parameters:** token

- the Windows NT security token for this user.

---

#### NTNumericCredential

public NTNumericCredential​(long token)

Create an

NTNumericCredential

with an integer value.

Method Detail

- getToken

```java
public long getToken()
```

Return an integer representation of this

NTNumericCredential

.

**Returns:** an integer representation of this

NTNumericCredential

.

- toString

```java
public
String
toString()
```

Return a string representation of this

NTNumericCredential

.

**Overrides:** toString

in class

Object
**Returns:** a string representation of this

NTNumericCredential

.

- equals

```java
public boolean equals​(
Object
o)
```

Compares the specified Object with this

NTNumericCredential

for equality. Returns true if the given object is also a

NTNumericCredential

and the two NTNumericCredentials
represent the same NT security token.

**Overrides:** equals

in class

Object
**Parameters:** o

- Object to be compared for equality with this

NTNumericCredential

.
**Returns:** true if the specified Object is equal to this

NTNumericCredential

.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Return a hash code for this

NTNumericCredential

.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code for this

NTNumericCredential

.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### Method Detail

getToken

```java
public long getToken()
```

Return an integer representation of this

NTNumericCredential

.

**Returns:** an integer representation of this

NTNumericCredential

.

---

#### getToken

public long getToken()

Return an integer representation of this

NTNumericCredential

.

toString

```java
public
String
toString()
```

Return a string representation of this

NTNumericCredential

.

**Overrides:** toString

in class

Object
**Returns:** a string representation of this

NTNumericCredential

.

---

#### toString

public

String

toString()

Return a string representation of this

NTNumericCredential

.

equals

```java
public boolean equals​(
Object
o)
```

Compares the specified Object with this

NTNumericCredential

for equality. Returns true if the given object is also a

NTNumericCredential

and the two NTNumericCredentials
represent the same NT security token.

**Overrides:** equals

in class

Object
**Parameters:** o

- Object to be compared for equality with this

NTNumericCredential

.
**Returns:** true if the specified Object is equal to this

NTNumericCredential

.
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

public boolean equals​(

Object

o)

Compares the specified Object with this

NTNumericCredential

for equality. Returns true if the given object is also a

NTNumericCredential

and the two NTNumericCredentials
represent the same NT security token.

hashCode

```java
public int hashCode()
```

Return a hash code for this

NTNumericCredential

.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code for this

NTNumericCredential

.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public int hashCode()

Return a hash code for this

NTNumericCredential

.

---

