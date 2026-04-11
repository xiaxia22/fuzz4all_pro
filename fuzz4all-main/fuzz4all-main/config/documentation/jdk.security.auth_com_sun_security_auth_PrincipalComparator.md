# Interface PrincipalComparator

**Source:** `jdk.security.auth\com\sun\security\auth\PrincipalComparator.html`

### Class Description

```java
public interface
PrincipalComparator
```

An object that implements the

java.security.Principal

interface typically also implements this interface to provide
a means for comparing that object to a specified

Subject

.

The comparison is achieved via the

implies

method.
The implementation of the

implies

method determines
whether this object "implies" the specified

Subject

.
One example application of this method may be for
a "group" object to imply a particular

Subject

if that

Subject

belongs to the group.
Another example application of this method would be for
"role" object to imply a particular

Subject

if that

Subject

is currently acting in that role.

Although classes that implement this interface typically
also implement the

java.security.Principal

interface,
it is not required. In other words, classes may implement the

java.security.Principal

interface by itself,
the

PrincipalComparator

interface by itself,
or both at the same time.

**See Also:** Principal

,

Subject

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### boolean implies​(
Subject
subject)

Check if the specified

Subject

is implied by
this object.

**Returns:**
- true if the specified

Subject

is implied by
this object, or false otherwise.

---

### Additional Sections

#### Interface PrincipalComparator

```java
public interface
PrincipalComparator
```

An object that implements the

java.security.Principal

interface typically also implements this interface to provide
a means for comparing that object to a specified

Subject

.

The comparison is achieved via the

implies

method.
The implementation of the

implies

method determines
whether this object "implies" the specified

Subject

.
One example application of this method may be for
a "group" object to imply a particular

Subject

if that

Subject

belongs to the group.
Another example application of this method would be for
"role" object to imply a particular

Subject

if that

Subject

is currently acting in that role.

Although classes that implement this interface typically
also implement the

java.security.Principal

interface,
it is not required. In other words, classes may implement the

java.security.Principal

interface by itself,
the

PrincipalComparator

interface by itself,
or both at the same time.

**See Also:** Principal

,

Subject

public interface

PrincipalComparator

An object that implements the

java.security.Principal

interface typically also implements this interface to provide
a means for comparing that object to a specified

Subject

.

The comparison is achieved via the

implies

method.
The implementation of the

implies

method determines
whether this object "implies" the specified

Subject

.
One example application of this method may be for
a "group" object to imply a particular

Subject

if that

Subject

belongs to the group.
Another example application of this method would be for
"role" object to imply a particular

Subject

if that

Subject

is currently acting in that role.

Although classes that implement this interface typically
also implement the

java.security.Principal

interface,
it is not required. In other words, classes may implement the

java.security.Principal

interface by itself,
the

PrincipalComparator

interface by itself,
or both at the same time.

The comparison is achieved via the

implies

method.
The implementation of the

implies

method determines
whether this object "implies" the specified

Subject

.
One example application of this method may be for
a "group" object to imply a particular

Subject

if that

Subject

belongs to the group.
Another example application of this method would be for
"role" object to imply a particular

Subject

if that

Subject

is currently acting in that role.

Although classes that implement this interface typically
also implement the

java.security.Principal

interface,
it is not required. In other words, classes may implement the

java.security.Principal

interface by itself,
the

PrincipalComparator

interface by itself,
or both at the same time.

Although classes that implement this interface typically
also implement the

java.security.Principal

interface,
it is not required. In other words, classes may implement the

java.security.Principal

interface by itself,
the

PrincipalComparator

interface by itself,
or both at the same time.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

boolean

implies

​(

Subject

subject)

Check if the specified

Subject

is implied by
this object.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

boolean

implies

​(

Subject

subject)

Check if the specified

Subject

is implied by
this object.

---

#### Method Summary

Check if the specified

Subject

is implied by
this object.

============ METHOD DETAIL ==========

- Method Detail

- implies

```java
boolean implies​(
Subject
subject)
```

Check if the specified

Subject

is implied by
this object.

**Returns:** true if the specified

Subject

is implied by
this object, or false otherwise.

Method Detail

- implies

```java
boolean implies​(
Subject
subject)
```

Check if the specified

Subject

is implied by
this object.

**Returns:** true if the specified

Subject

is implied by
this object, or false otherwise.

---

#### Method Detail

implies

```java
boolean implies​(
Subject
subject)
```

Check if the specified

Subject

is implied by
this object.

**Returns:** true if the specified

Subject

is implied by
this object, or false otherwise.

---

#### implies

boolean implies​(

Subject

subject)

Check if the specified

Subject

is implied by
this object.

---

