# Interface Principal

**Source:** `java.base\java\security\Principal.html`

### Class Description

```java
public interface
Principal
```

This interface represents the abstract notion of a principal, which
can be used to represent any entity, such as an individual, a
corporation, and a login id.

**All Known Subinterfaces:** Group

,

GroupPrincipal

,

UserPrincipal

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### boolean equals​(
Object
another)

Compares this principal to the specified object. Returns true
if the object passed in matches the principal represented by
the implementation of this interface.

**Overrides:**
- equals

in class

Object

**Parameters:**
- another

- principal to compare with.

**Returns:**
- true if the principal passed in is the same as that
encapsulated by this principal, and false otherwise.

**See Also:**
- Object.hashCode()

,

HashMap

---

#### String
toString()

Returns a string representation of this principal.

**Overrides:**
- toString

in class

Object

**Returns:**
- a string representation of this principal.

---

#### int hashCode()

Returns a hashcode for this principal.

**Overrides:**
- hashCode

in class

Object

**Returns:**
- a hashcode for this principal.

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### String
getName()

Returns the name of this principal.

**Returns:**
- the name of this principal.

---

#### default boolean implies​(
Subject
subject)

Returns true if the specified subject is implied by this principal.

**Parameters:**
- subject

- the

Subject

**Returns:**
- true if

subject

is non-null and is
implied by this principal, or false otherwise.

**Since:**
- 1.8

**Implementation Requirements:**
- The default implementation of this method returns true if

subject

is non-null and contains at least one principal that
is equal to this principal.

Subclasses may override this with a different implementation, if
necessary.

---

### Additional Sections

#### Interface Principal

**All Known Subinterfaces:** Group

,

GroupPrincipal

,

UserPrincipal

**All Known Implementing Classes:** HttpPrincipal

,

Identity

,

IdentityScope

,

JMXPrincipal

,

KerberosPrincipal

,

LdapPrincipal

,

NTDomainPrincipal

,

NTSid

,

NTSidDomainPrincipal

,

NTSidGroupPrincipal

,

NTSidPrimaryGroupPrincipal

,

NTSidUserPrincipal

,

NTUserPrincipal

,

Signer

,

UnixNumericGroupPrincipal

,

UnixNumericUserPrincipal

,

UnixPrincipal

,

UserPrincipal

,

X500Principal

```java
public interface
Principal
```

This interface represents the abstract notion of a principal, which
can be used to represent any entity, such as an individual, a
corporation, and a login id.

**Since:** 1.1
**See Also:** X509Certificate

public interface

Principal

This interface represents the abstract notion of a principal, which
can be used to represent any entity, such as an individual, a
corporation, and a login id.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Default Methods

Modifier and Type

Method

Description

boolean

equals

​(

Object

another)

Compares this principal to the specified object.

String

getName

()

Returns the name of this principal.

int

hashCode

()

Returns a hashcode for this principal.

default boolean

implies

​(

Subject

subject)

Returns true if the specified subject is implied by this principal.

String

toString

()

Returns a string representation of this principal.

Method Summary

All Methods

Instance Methods

Abstract Methods

Default Methods

Modifier and Type

Method

Description

boolean

equals

​(

Object

another)

Compares this principal to the specified object.

String

getName

()

Returns the name of this principal.

int

hashCode

()

Returns a hashcode for this principal.

default boolean

implies

​(

Subject

subject)

Returns true if the specified subject is implied by this principal.

String

toString

()

Returns a string representation of this principal.

---

#### Method Summary

Compares this principal to the specified object.

Returns the name of this principal.

Returns a hashcode for this principal.

Returns true if the specified subject is implied by this principal.

Returns a string representation of this principal.

============ METHOD DETAIL ==========

- Method Detail

- equals

```java
boolean equals​(
Object
another)
```

Compares this principal to the specified object. Returns true
if the object passed in matches the principal represented by
the implementation of this interface.

**Overrides:** equals

in class

Object
**Parameters:** another

- principal to compare with.
**Returns:** true if the principal passed in is the same as that
encapsulated by this principal, and false otherwise.
**See Also:** Object.hashCode()

,

HashMap

- toString

```java
String
toString()
```

Returns a string representation of this principal.

**Overrides:** toString

in class

Object
**Returns:** a string representation of this principal.

- hashCode

```java
int hashCode()
```

Returns a hashcode for this principal.

**Overrides:** hashCode

in class

Object
**Returns:** a hashcode for this principal.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- getName

```java
String
getName()
```

Returns the name of this principal.

**Returns:** the name of this principal.

- implies

```java
default boolean implies​(
Subject
subject)
```

Returns true if the specified subject is implied by this principal.

**Implementation Requirements:** The default implementation of this method returns true if

subject

is non-null and contains at least one principal that
is equal to this principal.

Subclasses may override this with a different implementation, if
necessary.
**Parameters:** subject

- the

Subject
**Returns:** true if

subject

is non-null and is
implied by this principal, or false otherwise.
**Since:** 1.8

Method Detail

- equals

```java
boolean equals​(
Object
another)
```

Compares this principal to the specified object. Returns true
if the object passed in matches the principal represented by
the implementation of this interface.

**Overrides:** equals

in class

Object
**Parameters:** another

- principal to compare with.
**Returns:** true if the principal passed in is the same as that
encapsulated by this principal, and false otherwise.
**See Also:** Object.hashCode()

,

HashMap

- toString

```java
String
toString()
```

Returns a string representation of this principal.

**Overrides:** toString

in class

Object
**Returns:** a string representation of this principal.

- hashCode

```java
int hashCode()
```

Returns a hashcode for this principal.

**Overrides:** hashCode

in class

Object
**Returns:** a hashcode for this principal.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- getName

```java
String
getName()
```

Returns the name of this principal.

**Returns:** the name of this principal.

- implies

```java
default boolean implies​(
Subject
subject)
```

Returns true if the specified subject is implied by this principal.

**Implementation Requirements:** The default implementation of this method returns true if

subject

is non-null and contains at least one principal that
is equal to this principal.

Subclasses may override this with a different implementation, if
necessary.
**Parameters:** subject

- the

Subject
**Returns:** true if

subject

is non-null and is
implied by this principal, or false otherwise.
**Since:** 1.8

---

#### Method Detail

equals

```java
boolean equals​(
Object
another)
```

Compares this principal to the specified object. Returns true
if the object passed in matches the principal represented by
the implementation of this interface.

**Overrides:** equals

in class

Object
**Parameters:** another

- principal to compare with.
**Returns:** true if the principal passed in is the same as that
encapsulated by this principal, and false otherwise.
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

boolean equals​(

Object

another)

Compares this principal to the specified object. Returns true
if the object passed in matches the principal represented by
the implementation of this interface.

toString

```java
String
toString()
```

Returns a string representation of this principal.

**Overrides:** toString

in class

Object
**Returns:** a string representation of this principal.

---

#### toString

String

toString()

Returns a string representation of this principal.

hashCode

```java
int hashCode()
```

Returns a hashcode for this principal.

**Overrides:** hashCode

in class

Object
**Returns:** a hashcode for this principal.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

int hashCode()

Returns a hashcode for this principal.

getName

```java
String
getName()
```

Returns the name of this principal.

**Returns:** the name of this principal.

---

#### getName

String

getName()

Returns the name of this principal.

implies

```java
default boolean implies​(
Subject
subject)
```

Returns true if the specified subject is implied by this principal.

**Implementation Requirements:** The default implementation of this method returns true if

subject

is non-null and contains at least one principal that
is equal to this principal.

Subclasses may override this with a different implementation, if
necessary.
**Parameters:** subject

- the

Subject
**Returns:** true if

subject

is non-null and is
implied by this principal, or false otherwise.
**Since:** 1.8

---

#### implies

default boolean implies​(

Subject

subject)

Returns true if the specified subject is implied by this principal.

Subclasses may override this with a different implementation, if
necessary.

---

